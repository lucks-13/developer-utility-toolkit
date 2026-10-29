from unittest.mock import Mock, patch
from toolkit.github_api import get_repo

@patch("toolkit.github_api.requests.get")
def test_get_repo_success(mock_get):
    mock_response = Mock()

    mock_response.json.return_value = {
        "name" : "cpython",
        "owner" : {"login" : "python"},
        "description" : "Python programming language",
        "language" : "Python",
        "stargazers_count" : 20,
        "html_url" :  "https://github.com/python/cpython"
    }

    mock_response.raise_for_status.return_value = None
    mock_get.re