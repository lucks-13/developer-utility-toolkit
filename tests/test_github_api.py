import requests
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
        "stargazers_count" : 100,
        "forks_count" : 20,
        "html_url" :  "https://github.com/python/cpython"
    }

    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response
    result = get_repo("python", "cpython")
    assert result["Repository"] == "cpython"
    assert result["Owner"] == "python"
    assert result["Stars"] == 100
    mock_get.assert_called_once_with("https://api.github.com/repos/python/cpython",timeout=10)

@patch("toolkit.github_api.requests.get")
def test_get_repo_not_found(mock_get):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
    mock_get.return_value = mock_response
    result = get_repo("fakeuser", "fake-repo")
    assert result is None

@patch("toolkit.github_api.requests.get")
def test_get_repo_timeout(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout
    result = get_repo("python","cpython")
    assert result is None

@patch("toolkit.github_api.requests.get")
def test_get_repo_connection_error(mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError
    result = get_repo("python","cpython")
    assert result is None