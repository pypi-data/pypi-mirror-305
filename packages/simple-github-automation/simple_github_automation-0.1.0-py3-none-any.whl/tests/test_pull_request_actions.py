import unittest
from unittest.mock import patch
from src.simple_github_automation.pull_request_actions import create_pull_request, add_label_to_pr, post_comment_to_pr

class TestPullRequestActions(unittest.TestCase):

    @patch("src.github_automation.pull_request_actions.requests.post")
    def test_create_pull_request(self, mock_post):
        # Mock response for creating a pull request
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {
            "number": 3,
            "title": "Test Pull Request",
            "html_url": "https://github.com/Vikranth3140/GitHub-Automation-Tools/pull/3"
        }

        # Call the function
        response = create_pull_request("test_repo", "feature-branch", "main", "Test Pull Request", "Test body")

        # Assertions
        self.assertEqual(response["number"], 3)
        self.assertEqual(response["title"], "Test Pull Request")
        mock_post.assert_called_once()

    @patch("src.github_automation.pull_request_actions.requests.post")
    def test_add_label_to_pr(self, mock_post):
        # Mock response for adding labels to a pull request
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = [
            {"name": "bug", "color": "d73a4a"},
            {"name": "enhancement", "color": "a2eeef"}
        ]

        # Call the function
        response = add_label_to_pr("test_repo", 3, ["bug", "enhancement"])

        # Assertions
        self.assertEqual(len(response), 2)
        self.assertEqual(response[0]["name"], "bug")
        self.assertEqual(response[1]["name"], "enhancement")
        mock_post.assert_called_once()

    @patch("src.github_automation.pull_request_actions.requests.post")
    def test_post_comment_to_pr(self, mock_post):
        # Mock response for posting a comment on a pull request
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {
            "id": 2442856040,
            "body": "This is a test comment.",
            "html_url": "https://github.com/Vikranth3140/GitHub-Automation-Tools/pull/3#issuecomment-2442856040"
        }

        # Call the function
        response = post_comment_to_pr("test_repo", 3, "This is a test comment.")

        # Assertions
        self.assertEqual(response["body"], "This is a test comment.")
        self.assertEqual(response["id"], 2442856040)
        mock_post.assert_called_once()

if __name__ == "__main__":
    unittest.main()
