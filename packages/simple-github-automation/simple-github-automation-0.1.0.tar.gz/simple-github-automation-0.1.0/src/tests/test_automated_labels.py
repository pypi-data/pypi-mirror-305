import unittest
from unittest.mock import patch
from src.simple_github_automation.automated_labels import add_labels_by_keywords, add_labels_by_mentions

class TestAutomatedLabels(unittest.TestCase):

    @patch("src.github_automation.automated_labels.requests.post")
    def test_add_labels_by_keywords(self, mock_post):
        # Mock response for adding labels based on keywords
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = [
            {"name": "bug", "color": "d73a4a"},
            {"name": "priority", "color": "ededed"}
        ]

        # Set up test inputs
        repo_name = "test_repo"
        issue_number = 1
        content = "This is an urgent bug report."
        keyword_label_map = {
            "bug": "bug",
            "urgent": "priority"
        }

        # Call the function
        response = add_labels_by_keywords(repo_name, issue_number, content, keyword_label_map)

        # Assertions
        self.assertEqual(len(response), 2)
        self.assertEqual(response[0]["name"], "bug")
        self.assertEqual(response[1]["name"], "priority")
        mock_post.assert_called_once()

    @patch("src.github_automation.automated_labels.requests.post")
    def test_add_labels_by_mentions(self, mock_post):
        # Mock response for adding labels based on mentions
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = [
            {"name": "assigned", "color": "ededed"}
        ]

        # Set up test inputs
        repo_name = "test_repo"
        issue_number = 1
        content = "Assigning this task to @Vikranth3140."
        mention_label_map = {
            "Vikranth3140": "assigned"
        }

        # Call the function
        response = add_labels_by_mentions(repo_name, issue_number, content, mention_label_map)

        # Assertions
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0]["name"], "assigned")
        mock_post.assert_called_once()

if __name__ == "__main__":
    unittest.main()
