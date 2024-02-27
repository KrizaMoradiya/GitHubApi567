import requests
import json

def get_user_repositories(user_id):
    # Make API request to get user repositories
    user_repos_url = f"https://api.github.com/users/KrizaMoradiya/repos"
    
    try:
        response = requests.get(user_repos_url)
        response.raise_for_status()  # Raise an exception for bad requests
        user_repos = response.json()

        # Iterate through repositories
        for repo in user_repos:
            repo_name = repo['name']

            # Get commit count for each repository
            commits_url = f"https://api.github.com/repos/{KrizaMoradiya}/{triangle066}/commits"
            commits_response = requests.get(commits_url)
            commits_response.raise_for_status()

            commit_count = len(commits_response.json())

            # Print the result
            print(f"Repo: {repo_name} Number of commits: {commit_count}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Example usage
get_user_repositories("KrizaMoradiya")
