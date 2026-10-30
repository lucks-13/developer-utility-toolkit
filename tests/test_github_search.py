import requests

from unittest.mock import Mock, patch
from toolkit.github_search import search_repos

@patch("toolkit.github_search.requests.get")
def test_search_repos_success(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "total_count" : 100,
        "items" : [
            {
                "name" : "cpython",
                "full_name" : "python/cpython",
                "owner" : {"login" : "python"},
                "description" : "Python programming language",
                "language" : "Python",
                "stargazers_count" : 100,
                "forks_count" : 20,
                "html_url" : "https://github.com/python/cpython"
            }
        ]
    }

    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = search_repos("python", "Python", 5)
    assert result["Total Results"] == 100
    repo
    