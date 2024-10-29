import requests
from simple_github_automation.config import GITHUB_TOKEN

# Helper function to get headers for API requests
def get_headers():
    return {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

# Function to get repository statistics
def get_repo_stats(repo_name):
    """
    Retrieves statistics for a given GitHub repository.

    Parameters:
    - repo_name (str): The name of the repository (e.g., "username/repo").

    Returns:
    - dict: Repository stats including stars, forks, and open issues count, or error message if failed.
    """
    url = f"https://api.github.com/repos/{repo_name}"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        data = response.json()
        return {
            "stars": data["stargazers_count"],
            "forks": data["forks_count"],
            "open_issues": data["open_issues_count"],
            "watchers": data["watchers_count"]
        }
    else:
        return {"error": response.json().get("message", "Failed to fetch repository stats")}

# Function to list contributors to a repository
def list_contributors(repo_name):
    """
    Retrieves a list of contributors for a given GitHub repository.

    Parameters:
    - repo_name (str): The name of the repository (e.g., "username/repo").

    Returns:
    - list: List of contributors or error message if failed.
    """
    url = f"https://api.github.com/repos/{repo_name}/contributors"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        contributors = response.json()
        return [{"login": contributor["login"], "contributions": contributor["contributions"]} for contributor in contributors]
    else:
        return {"error": response.json().get("message", "Failed to fetch contributors")}

# Function to get the count of open issues
def get_open_issues_count(repo_name):
    """
    Returns the count of open issues for a given GitHub repository.

    Parameters:
    - repo_name (str): The name of the repository (e.g., "username/repo").

    Returns:
    - int: Count of open issues or error message if failed.
    """
    url = f"https://api.github.com/repos/{repo_name}"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        return response.json().get("open_issues_count", 0)
    else:
        return {"error": response.json().get("message", "Failed to fetch open issues count")}
