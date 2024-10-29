import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta

from src.dhisana.utils.agent_tools import (
    search_google_maps,
    enrich_people_with_apollo,
    search_google,
    search_google_jobs,
    search_google_news,
    get_html_content_from_url,
    parse_html_content,
    extract_image_links,
    extract_head_section_from_html_content,
    get_email_if_exists,
    search_crunchbase,
    search_people_with_apollo,
    search_companies_with_apollo,
    enrich_company_with_apollo,
    get_job_postings_from_apollo,
    get_calendar_events_using_service_account,
    list_files_in_drive_folder_by_name,
    send_email_using_service_account,
    get_file_content_from_googledrive_by_name
)

class TestAgentTools(unittest.TestCase):

    @patch('requests.get')
    def test_search_google_maps(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {'results': 'some_data'}
        mock_get.return_value = mock_response

        result = search_google_maps('test query')
        self.assertEqual(result, {'results': 'some_data'})

    @patch('requests.post')
    def test_enrich_people_with_apollo(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {'people': 'some_data'}
        mock_post.return_value = mock_response

        lead_list = [{'first_name': 'John', 'last_name': 'Doe'}]
        result = enrich_people_with_apollo(lead_list)
        self.assertEqual(result, {'people': 'some_data'})

    @patch('requests.get')
    def test_search_google(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {'results': 'some_data'}
        mock_get.return_value = mock_response

        result = search_google('test query')
        self.assertEqual(result, {'results': 'some_data'})

    @patch('requests.get')
    def test_search_google_jobs(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {'results': 'some_data'}
        mock_get.return_value = mock_response

        result = search_google_jobs('test query')
        self.assertEqual(result, {'results': 'some_data'})

    @patch('requests.get')
    def test_search_google_news(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {'results': 'some_data'}
        mock_get.return_value = mock_response

        result = search_google_news('test query')
        self.assertEqual(result, {'results': 'some_data'})

    def test_parse_html_content(self):
        html_content = '<html><body><script>var a = 1;</script><p>Text</p></body></html>'
        result = parse_html_content(html_content)
        self.assertEqual(result, 'Text')

    def test_extract_image_links(self):
        html_content = '<html><body><img src="image1.jpg" alt="Image 1"><img src="image2.jpg"></body></html>'
        result = extract_image_links(html_content)
        self.assertEqual(result, [{'src': 'image1.jpg', 'alt': 'Image 1'}, {'src': 'image2.jpg', 'alt': ''}])

    def test_extract_head_section_from_html_content(self):
        html_content = '<html><head><title>Test</title></head><body></body></html>'
        result = extract_head_section_from_html_content(html_content)
        self.assertEqual(result, '<head><title>Test</title></head>')

    def test_get_email_if_exists(self):
        website_content = 'Contact us at email@example.com for more info.'
        result = get_email_if_exists(website_content)
        self.assertIn('email@example.com', result)

    @patch('requests.post')
    def test_search_crunchbase(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {'organizations': 'some_data'}
        mock_post.return_value = mock_response

        result = search_crunchbase('test query')
        self.assertEqual(result, {'organizations': 'some_data'})

    @patch('requests.post')
    def test_search_people_with_apollo(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {'people': 'some_data'}
        mock_post.return_value = mock_response

        result = search_people_with_apollo(person_titles='Engineer')
        self.assertEqual(result, {'people': 'some_data'})

    @patch('requests.post')
    def test_search_companies_with_apollo(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {'companies': 'some_data'}
        mock_post.return_value = mock_response

        result = search_companies_with_apollo(locations='San Jose')
        self.assertEqual(result, {'companies': 'some_data'})

    @patch('requests.get')
    def test_enrich_company_with_apollo(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {'company': 'some_data'}
        mock_get.return_value = mock_response

        result = enrich_company_with_apollo(company_domain='example.com')
        self.assertEqual(result, {'company': 'some_data'})

    @patch('requests.get')
    def test_get_job_postings_from_apollo(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {'organization_job_postings': 'some_data'}
        mock_get.return_value = mock_response

        result = get_job_postings_from_apollo(organization_id='123')
        self.assertEqual(result, 'some_data')
        
    @patch('requests.get')
    def test_get_calendar_events_using_service_account():
        # Calculate the start and end dates for the current week
        today = datetime.now()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        start_date = start_of_week.strftime('%Y-%m-%d')
        end_date = end_of_week.strftime('%Y-%m-%d')

        # Call the function with the calculated dates
        events = get_calendar_events_using_service_account(start_date, end_date)

        # Print the returned events
        print("Events for the current week:")
        for event in events:
            print(event)

    @patch('requests.get')
    def test_list_files_in_drive_folder_by_name():
        # Example usage
        folder_name = ''  # Provide folder name or leave it empty to list files in the root folder
        file_list = list_files_in_drive_folder_by_name(folder_name)
        print("Files in Drive folder:", file_list)


    @patch('requests.post')
    def test_send_email_using_service_account():
        recipient = "test@dhisana.co"
        subject = "Test Subject From Agent"
        body = "This is a test email body."
        
        try:
            message_id = send_email_using_service_account(recipient, subject, body)
            print(f"Email sent successfully with message ID: {message_id}")
        except Exception as e:
            print(f"Error sending email: {e}")

    @patch('requests.get')
    def test_get_file_content_from_googledrive_by_name():
        file_name = "inputs.csv"
        try:
            local_file_path = get_file_content_from_googledrive_by_name(file_name)
            print(f"File downloaded successfully to: {local_file_path}")
        except Exception as e:
            print(f"Error downloading file: {e}")
        
if __name__ == '__main__':
    unittest.main()