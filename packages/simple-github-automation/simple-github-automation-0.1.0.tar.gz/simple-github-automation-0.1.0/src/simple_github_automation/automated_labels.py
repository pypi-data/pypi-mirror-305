import requests
from simple_github_automation.config import GITHUB_TOKEN

# Helper function to get headers for API requests
def get_headers():
    return {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

# Function to add labels based on keywords
def add_labels_by_keywords(repo_name, issue_number, content, keyword_label_map):
    """
    Adds labels to an issue or pull request based on keywords in the content.

    Parameters:
    - repo_name (str): The repository name (e.g., "username/repo").
    - issue_number (int): The number of the issue or pull request.
    - content (str): The title or body of the issue/PR.
    - keyword_label_map (dict): A dictionary mapping keywords to labels.

    Returns:
    - dict: Response JSON from the GitHub API or error message if failed.
    """
    labels_to_add = []
    for keyword, label in keyword_label_map.items():
        if keyword.lower() in content.lower():
            labels_to_add.append(label)

    if labels_to_add:
        url = f"https://api.github.com/repos/{repo_name}/issues/{issue_number}/labels"
        response = requests.post(url, json={"labels": labels_to_add}, headers=get_headers())

        if response.status_code == 200:
            return response.json()  # Success, labels added
        else:
            return {"error": response.json().get("message", "Failed to add labels")}
    else:
        return {"message": "No matching keywords found for labeling"}

# Function to add labels based on user mentions
def add_labels_by_mentions(repo_name, issue_number, content, mention_label_map):
    """
    Adds labels to an issue or pull request based on user mentions in the content.

    Parameters:
    - repo_name (str): The repository name (e.g., "username/repo").
    - issue_number (int): The number of the issue or pull request.
    - content (str): The title or body of the issue/PR.
    - mention_label_map (dict): A dictionary mapping user mentions to labels.

    Returns:
    - dict: Response JSON from the GitHub API or error message if failed.
    """
    labels_to_add = []
    for mention, label in mention_label_map.items():
        if f"@{mention}" in content:
            labels_to_add.append(label)

    if labels_to_add:
        url = f"https://api.github.com/repos/{repo_name}/issues/{issue_number}/labels"
        response = requests.post(url, json={"labels": labels_to_add}, headers=get_headers())

        if response.status_code == 200:
            return response.json()  # Success, labels added
        else:
            return {"error": response.json().get("message", "Failed to add labels")}
    else:
        return {"message": "No matching mentions found for labeling"}
