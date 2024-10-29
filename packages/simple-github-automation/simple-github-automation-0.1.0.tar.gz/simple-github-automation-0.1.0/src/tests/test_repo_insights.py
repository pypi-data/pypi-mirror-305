import unittest
from unittest.mock import patch
from src.simple_github_automation.repo_insights import get_repo_stats, list_contributors, get_open_issues_count

class TestRepoInsights(unittest.TestCase):

    @patch("src.github_automation.repo_insights.requests.get")
    def test_get_repo_stats(self, mock_get):
        # Mock response for repository statistics
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "stargazers_count": 5,
            "forks_count": 3,
            "open_issues_count": 2,
            "watchers_count": 5
        }

        # Call the function
        response = get_repo_stats("test_repo")

        # Assertions
        self.assertEqual(response["stars"], 5)
        self.assertEqual(response["forks"], 3)
        self.assertEqual(response["open_issues"], 2)
        self.assertEqual(response["watchers"], 5)
        mock_get.assert_called_once()

    @patch("src.github_automation.repo_insights.requests.get")
    def test_list_contributors(self, mock_get):
        # Mock response for contributors
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"login": "contributor1", "contributions": 10},
            {"login": "contributor2", "contributions": 5}
        ]

        # Call the function
        response = list_contributors("test_repo")

        # Assertions
        self.assertEqual(len(response), 2)
        self.assertEqual(response[0]["login"], "contributor1")
        self.assertEqual(response[1]["contributions"], 5)
        mock_get.assert_called_once()

    @patch("src.github_automation.repo_insights.requests.get")
    def test_get_open_issues_count(self, mock_get):
        # Mock response for open issues count
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"open_issues_count": 4}

        # Call the function
        response = get_open_issues_count("test_repo")

        # Assertions
        self.assertEqual(response, 4)
        mock_get.assert_called_once()

if __name__ == "__main__":
    unittest.main()
