import unittest
from unittest.mock import patch
from src.simple_github_automation.issue_management import create_issue, update_issue, close_issue

class TestIssueManagement(unittest.TestCase):

    @patch("src.github_automation.issue_management.requests.post")
    def test_create_issue(self, mock_post):
        # Mock response from GitHub API
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {"number": 1, "title": "Test Issue"}

        # Call function
        response = create_issue("test_repo", "Test Issue", "This is a test.")

        # Assertions
        self.assertEqual(response["number"], 1)
        self.assertEqual(response["title"], "Test Issue")
        mock_post.assert_called_once()

    @patch("src.github_automation.issue_management.requests.patch")
    def test_update_issue(self, mock_patch):
        # Mock response from GitHub API
        mock_patch.return_value.status_code = 200
        mock_patch.return_value.json.return_value = {"number": 1, "title": "Updated Issue"}

        # Call function
        response = update_issue("test_repo", 1, title="Updated Issue", body="Updated body.")

        # Assertions
        self.assertEqual(response["title"], "Updated Issue")
        mock_patch.assert_called_once()

    @patch("src.github_automation.issue_management.requests.patch")
    def test_close_issue(self, mock_patch):
        # Mock response from GitHub API
        mock_patch.return_value.status_code = 200
        mock_patch.return_value.json.return_value = {"number": 1, "state": "closed"}

        # Call function
        response = close_issue("test_repo", 1)

        # Assertions
        self.assertEqual(response["state"], "closed")
        mock_patch.assert_called_once()

if __name__ == "__main__":
    unittest.main()
