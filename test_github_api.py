import unittest
from github_api import get_user_repositories

class TestGitHubAPI(unittest.TestCase):
    def test_valid_user(self):
        # Test with a valid user
        # Check if the expected output matches the actual output
        pass

    # Add more test cases for different scenarios

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import patch, MagicMock
from github_api import get_user_repositories

class TestGitHubAPI(unittest.TestCase):
    @patch('builtins.print')
    @patch('requests.get')
    def test_valid_user(self, mock_requests_get, mock_print):
        # Mocking the response for user repositories
        user_repos_response = MagicMock()
        user_repos_response.json.return_value = [{'name': 'Repo1'}, {'name': 'Repo2'}]
        mock_requests_get.return_value = user_repos_response

        # Mocking the response for commits in Repo1
        mock_commits_response_repo1 = MagicMock()
        mock_commits_response_repo1.json.return_value = [{'commit': 'Commit1'}, {'commit': 'Commit2'}]

        # Mocking the response for commits in Repo2
        mock_commits_response_repo2 = MagicMock()
        mock_commits_response_repo2.json.return_value = [{'commit': 'Commit3'}, {'commit': 'Commit4'}]

        # Mocking the requests.get method to return the appropriate responses
        with patch('requests.get', side_effect=[mock_commits_response_repo1, mock_commits_response_repo2]):
            # Call the function with a valid user
            get_user_repositories("KrizaMoradiya")

        # Assert that print was called with the expected results
        mock_print.assert_has_calls([
            unittest.mock.call("Repo: Repo1 Number of commits: 2"),
            unittest.mock.call("Repo: Repo2 Number of commits: 2")
        ])

    # Add more test cases for different scenarios

if __name__ == '__main__':
    unittest.main()
