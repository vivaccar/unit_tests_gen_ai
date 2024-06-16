from ex_01 import get_username, get_email, get_sql_query, get_password
import unittest
from unittest.mock import patch

class TestUserInputValidation(unittest.TestCase):

    @patch('builtins.input', side_effect=['vivaccar'])
    def test_get_username_valid(self, mock_input):
        self.assertEqual(get_username(), 'vivaccar')

    @patch('builtins.input', side_effect=['invalid@username', 'username123'])
    def test_get_invalid_username_then_valid(self, mock_input):
        self.assertEqual(get_username(), 'username123')

    @patch('builtins.input', side_effect=['password123'])
    def test_get_password_valid(self, mock_input):
        self.assertEqual(get_password(), 'password123')

    @patch('builtins.input', side_effect=['1234567', 'password123'])
    def test_get_invalid_password_then_valid(self, mock_input):
        self.assertEqual(get_password(), 'password123')

    @patch('builtins.input', side_effect=['example@example.com'])
    def test_get_email_valid(self, mock_input):
        self.assertEqual(get_email(), 'example@example.com')

    @patch('builtins.input', side_effect=['invalid_email', 'example@example.com'])
    def test_get_invalid_email_then_valid(self, mock_input):
        self.assertEqual(get_email(), 'example@example.com')

    @patch('builtins.input', side_effect=['SELECT * FROM table'])
    def test_get_sql_query_valid(self, mock_input):
        self.assertEqual(get_sql_query(), 'SELECT * FROM table')

    @patch('builtins.input', side_effect=['DELETE FROM table', 'SELECT * FROM table'])
    def test_get_invalid_sql_query_then_valid(self, mock_input):
        self.assertEqual(get_sql_query(), 'SELECT * FROM table')

if __name__ == '__main__':
    unittest.main()