import unittest
from unittest.mock import patch
from refactor_code import get_user_input, call_chat_gpt, handle_response, prompt_continue

class TestRefactorCode(unittest.TestCase):
    @patch('builtins.input', return_value='Hello, world!')
    def test_get_user_input(self, mock_input):
        self.assertEqual(get_user_input(), 'Hello, world!')

    @patch('requests.post')
    def test_call_chat_gpt(self, mock_post):
        mock_response = {
            "choices": [
                {
                    "text": "Hello, world!"
                }
            ]
        }
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response
        response = call_chat_gpt("Hello")
        self.assertEqual(response.json(), mock_response)

    def test_handle_response(self):
        mock_response = {
            "choices": [
                {
                    "text": "Hello, world!"
                }
            ]
        }
        self.assertEqual(handle_response(mock_response), "Hello, world!")

        mock_response = {
            "error": "Invalid API key"
        }
        self.assertIsNone(handle_response(mock_response))

    @patch('builtins.input', return_value='y')
    def test_prompt_continue(self, mock_input):
        self.assertTrue(prompt_continue())

    @patch('builtins.input', return_value='n')
    def test_prompt_continue_negative(self, mock_input):
        self.assertFalse(prompt_continue())

if __name__ == '__main__':
    unittest.main()