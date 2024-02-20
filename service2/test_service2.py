import unittest
from unittest.mock import patch, Mock
import requests
import subprocess
from entrypoint import call_service1

class TestCallService1(unittest.TestCase):
    @patch('requests.post')
    def test_call_service1_success(self, mock_post):
        mock_response = Mock()
        mock_response.text = "Hash: 12345"
        mock_post.return_value = mock_response

        hash_func = "md5"
        message = "Test message"

        expected_url = "http://localhost:8080"
        expected_data = "md5\nTest message"

        result = call_service1(hash_func, message)

        mock_post.assert_called_once_with(expected_url, data=expected_data)
        self.assertEqual(result, "12345")

    @patch('requests.post', side_effect=requests.RequestException)
    def test_call_service1_failure(self, mock_post):
        hash_func = "md5"
        message = "Test message"

        with self.assertRaises(Exception) as context:
            call_service1(hash_func, message)

        self.assertIn("Error calling Service 1:", str(context.exception))


if __name__ == '__main__':
    unittest.main()
