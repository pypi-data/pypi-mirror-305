import requests
from simple_github_automation.config import GITHUB_TOKEN

# Helper function to get headers for API requests
def get_headers():
    return {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

# Function to create a new issue
def create_issue(repo_name, title, body=""):
    """
    Creates a new issue in the specified GitHub repository.

    Parameters:
    - repo_name (str): The name of the repository (e.g., "username/repo").
    - title (str): The title of the issue.
    - body (str): The body or description of the issue (optional).

    Returns:
    - dict: Response JSON from the GitHub API, or error message if failed.
    """
    url = f"https://api.github.com/repos/{repo_name}/issues"
    payload = {"title": title, "body": body}
    response = requests.post(url, json=payload, headers=get_headers())

    if response.status_code == 201:
        return response.json()  # Success, issue created
    else:
        return {"error": response.json().get("message", "Failed to create issue")}

# Function to update an existing issue
def update_issue(repo_name, issue_number, title=None, body=None):
    """
    Updates an existing issue in the specified GitHub repository.

    Parameters:
    - repo_name (str): The name of the repository (e.g., "username/repo").
    - issue_number (int): The number of the issue to update.
    - title (str): The new title of the issue (optional).
    - body (str): The new body or description of the issue (optional).

    Returns:
    - dict: Response JSON from the GitHub API, or error message if failed.
    """
    url = f"https://api.github.com/repos/{repo_name}/issues/{issue_number}"
    payload = {k: v for k, v in [("title", title), ("body", body)] if v is not None}
    response = requests.patch(url, json=payload, headers=get_headers())

    if response.status_code == 200:
        return response.json()  # Success, issue updated
    else:
        return {"error": response.json().get("message", "Failed to update issue")}

# Function to close an issue
def close_issue(repo_name, issue_number):
    """
    Closes an existing issue in the specified GitHub repository.

    Parameters:
    - repo_name (str): The name of the repository (e.g., "username/repo").
    - issue_number (int): The number of the issue to close.

    Returns:
    - dict: Response JSON from the GitHub API, or error message if failed.
    """
    url = f"https://api.github.com/repos/{repo_name}/issues/{issue_number}"
    payload = {"state": "closed"}
    response = requests.patch(url, json=payload, headers=get_headers())

    if response.status_code == 200:
        return response.json()  # Success, issue closed
    else:
        return {"error": response.json().get("message", "Failed to close issue")}