import requests
from simple_github_automation.config import GITHUB_TOKEN

# Helper function to get headers for API requests
def get_headers():
    return {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

# Function to create a new pull request
def create_pull_request(repo_name, head, base, title, body=""):
    """
    Creates a new pull request in the specified GitHub repository.

    Parameters:
    - repo_name (str): The name of the repository (e.g., "username/repo").
    - head (str): The branch name where changes are implemented.
    - base (str): The branch name you want to merge changes into.
    - title (str): The title of the pull request.
    - body (str): The body or description of the pull request (optional).

    Returns:
    - dict: Response JSON from the GitHub API, or error message if failed.
    """
    url = f"https://api.github.com/repos/{repo_name}/pulls"
    payload = {
        "title": title,
        "head": head,
        "base": base,
        "body": body
    }
    response = requests.post(url, json=payload, headers=get_headers())

    if response.status_code == 201:
        return response.json()  # Success, PR created
    else:
        error_message = response.json().get("message", "Failed to create pull request")
        errors = response.json().get("errors", [])
        return {"error": error_message, "details": errors}

# Function to add a label to an existing pull request
def add_label_to_pr(repo_name, pr_number, labels):
    """
    Adds labels to an existing pull request.

    Parameters:
    - repo_name (str): The name of the repository (e.g., "username/repo").
    - pr_number (int): The number of the pull request.
    - labels (list): A list of labels to add.

    Returns:
    - dict: Response JSON from the GitHub API, or error message if failed.
    """
    url = f"https://api.github.com/repos/{repo_name}/issues/{pr_number}/labels"
    payload = {"labels": labels}
    response = requests.post(url, json=payload, headers=get_headers())

    if response.status_code == 200:
        return response.json()  # Success, labels added
    else:
        return {"error": response.json().get("message", "Failed to add labels to pull request")}

# Function to post a comment on a pull request
def post_comment_to_pr(repo_name, pr_number, comment):
    """
    Posts a comment on a specified pull request.

    Parameters:
    - repo_name (str): The name of the repository (e.g., "username/repo").
    - pr_number (int): The number of the pull request.
    - comment (str): The content of the comment to post.

    Returns:
    - dict: Response JSON from the GitHub API, or error message if failed.
    """
    url = f"https://api.github.com/repos/{repo_name}/issues/{pr_number}/comments"
    payload = {"body": comment}
    response = requests.post(url, json=payload, headers=get_headers())

    if response.status_code == 201:
        return response.json()  # Success, comment posted
    else:
        return {"error": response.json().get("message", "Failed to post comment on pull request")}
