# Helper functions to call OpenAI Assistant

import logging
import os
import json
from typing import Dict, List

from fastapi import HTTPException
from openai import LengthFinishReasonError, OpenAI, OpenAIError
from pydantic import BaseModel

from dhisana.utils.agent_tools import GLOBAL_DATA_MODELS, GLOBAL_TOOLS_FUNCTIONS
from .tools_json import GLOBAL_ASSISTANT_TOOLS
from .openapi_spec_to_tools import OPENAPI_TOOL_CONFIGURATIONS, OPENAPI_GLOBAL_ASSISTANT_TOOLS, OPENAPI_CALLABALE_FUNCTIONS

def get_headers(toolname):
    headers = OPENAPI_TOOL_CONFIGURATIONS.get(toolname, {}).get("headers", {})
    return headers

def get_params(toolname):
    headers = OPENAPI_TOOL_CONFIGURATIONS.get(toolname, {}).get("params", {})
    return headers
        
async def run_assistant(client, assistant, thread, prompt, response_type, allowed_tools):
    """
    Runs the assistant with the given parameters.
    """
    send_initial_message(client, thread, prompt)
    allowed_tool_items = get_allowed_tool_items(allowed_tools)
    response_format = get_response_format(response_type)

    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id,
        response_format=response_format,
        tools=allowed_tool_items,
    )

    max_iterations = 5
    iteration_count = 0

    while run.status == 'requires_action':
        if iteration_count >= max_iterations:
            print("Exceeded maximum number of iterations for requires_action.")
            return "Error: Exceeded maximum number of iterations for requires_action."

        tool_outputs = await handle_required_action(run)
        if tool_outputs:
            run = submit_tool_outputs(client, thread, run, tool_outputs)

        iteration_count += 1

    return handle_run_completion(client, thread, run)


def send_initial_message(client, thread, prompt):
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt,
    )


def get_allowed_tool_items(allowed_tools):
    allowed_tool_items = [
        tool for tool in GLOBAL_ASSISTANT_TOOLS 
        if tool['type'] == 'function' and tool['function']['name'] in allowed_tools
    ]
    allowed_tool_items.extend([
        tool for tool in OPENAPI_GLOBAL_ASSISTANT_TOOLS 
        if tool['type'] == 'function' and tool['function']['name'] in allowed_tools
    ])
    return allowed_tool_items


def get_response_format(response_type):
    return {
        'type': 'json_schema',
        'json_schema': {
            "name": response_type.__class__.__name__,
            "schema": response_type.model_json_schema()
        }
    }


async def handle_required_action(run):
    tool_outputs = []
    current_batch_size = 0
    max_batch_size = 256 * 1024

    if hasattr(run, 'required_action') and hasattr(run.required_action, 'submit_tool_outputs'):
        for tool in run.required_action.submit_tool_outputs.tool_calls:
            function, openai_function = get_function(tool.function.name)
            if function:
                output_str, output_size = await invoke_function(function, tool, openai_function)
                if current_batch_size + output_size > max_batch_size:
                    tool_outputs.append({"tool_call_id": tool.id, "output": ""})
                else:
                    tool_outputs.append({"tool_call_id": tool.id, "output": output_str})
                    current_batch_size += output_size
            else:
                print(f"Function {tool.function.name} not found.")
                tool_outputs.append({"tool_call_id": tool.id, "output": "No results found"})

    return tool_outputs


def get_function(function_name):
    function = GLOBAL_TOOLS_FUNCTIONS.get(function_name)
    openai_function = False
    if not function:
        function = OPENAPI_CALLABALE_FUNCTIONS.get(function_name)
        openai_function = True
    return function, openai_function


async def invoke_function(function, tool, openai_function):
    try:
        function_args = json.loads(tool.function.arguments)
        print(f"Invoking function {tool.function.name} with args: {function_args}\n")
        if openai_function:
            output = invoke_openai_function(function, function_args, tool.function.name)
        else:
            output = await function(**function_args)
        output_str = json.dumps(output)
        output_size = len(output_str.encode('utf-8'))
        print(f"\nOutput from function {tool.function.name}: {output_str[:64]}\n")        
        return output_str, output_size
    except Exception as e:
        print(f"Error invoking function {tool.function.name}: {e}")
        return "No results found", 0


def invoke_openai_function(function, function_args, function_name):
    
    json_body = function_args.get("json", None)
    path_params = function_args.get("path_params", None)
    fn_args = {"path_params": path_params, "data": json_body}
    headers = get_headers(function_name)
    
    query_params = function_args.get("params", {})
    params = get_params(function_name)
    query_params.update(params)

    output_fn = function(
        name=function_name,
        fn_args=fn_args,
        headers=headers,
        params=query_params,
    )
    print(f"\nOutput from function {function_name}: {output_fn.status_code} {output_fn.reason}\n")
    return {
        "status_code": output_fn.status_code,
        "text": output_fn.text,
        "reason": output_fn.reason,
    }


def submit_tool_outputs(client, thread, run, tool_outputs):
    try:
        return client.beta.threads.runs.submit_tool_outputs_and_poll(
            thread_id=thread.id,
            run_id=run.id,
            tool_outputs=tool_outputs
        )
    except Exception as e:
        print("Failed to submit tool outputs:", e)
        return run


def handle_run_completion(client, thread, run):
    if run.status == 'completed':
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        return messages.data[0].content[0].text.value
    else:
        print("Failed to run assistant:", run.status)
        return run.status

async def extract_and_structure_data(client, assistant, thread, prompt, user_provider_data, response_type, allowed_tools):
    formatted_prompt = prompt.format(input=user_provider_data)
    output = await run_assistant(client, assistant, thread, formatted_prompt, response_type, allowed_tools)
    return output

# Function to get structured output from OpenAI API
def get_structured_output(message: str, response_type):
    try:
        client = OpenAI()
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": "Extract structured content from input. Output is in JSON Format."},
                {"role": "user", "content": message},
            ],
            response_format=response_type,
        )

        response = completion.choices[0].message
        if response.parsed:
            return response.parsed, 'SUCCESS'
        elif response.refusal:
            logging.warning("ERROR: Refusal response: %s", response.refusal)
            return response.refusal, 'FAIL'
        
    except LengthFinishReasonError as e:
        logging.error(f"Too many tokens: {e}")
        raise HTTPException(status_code=502, detail="The request exceeded the maximum token limit.")
    except OpenAIError as e:
        logging.error(f"OpenAI API error: {e}")
        raise HTTPException(status_code=502, detail="Error communicating with the OpenAI API.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred while processing your request.")

class RowItem(BaseModel):
    column_value: str
    
class ResponseList(BaseModel):
    rows: List[RowItem]

def lookup_response_type(name: str):
        for model in GLOBAL_DATA_MODELS:
            if model.__name__ == name:
                return model
        return None
    
# Function to process a batch request
async def process_agent_request(row_batch: List[Dict], steps: Dict, custom_instructions: str) -> List[Dict]:
    """
    Process agent request using the OpenAI client.
    """
    try:
        client = OpenAI()
        assistant = client.beta.assistants.create(
            name="AI Assistant",
            instructions=f"Hi, You are an AI Assistant. Help the user with their tasks.\n\n{custom_instructions}\n\n",
            tools=[],
            model="gpt-4o-2024-08-06"
        )
        thread = client.beta.threads.create()

        parsed_outputs = []
        for row in row_batch:
            try:
                input_data = json.dumps(row)
                output = {}
                for step in steps['steps']:
                    type = step.get("response_type", None)
                    if not type:
                        type = "ResponseList"
                        response_type = ResponseList
                    else:
                        response_type = lookup_response_type(step.get("response_type", None))                    
                    if not response_type:
                        response_type = ResponseList
                    allowed_tools = step.get("allowed_tools", [])
                    output = await extract_and_structure_data(client, assistant, thread, step["prompt"], input_data, response_type, allowed_tools)
                    output_obj = json.loads(output)
                    if 'ID' in row:
                        output_obj['INPUT_ID'] = row['ID']
                    input_data = output
                parsed_outputs.append(output_obj)
            except Exception as e:
                print(f"Error processing lead {row}: {e}")
        return parsed_outputs
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error Processing Leads"
    finally:
        try:
            client.beta.assistants.delete(assistant.id)
        except Exception as e:
            print(f"Error deleting assistant: {e}")
