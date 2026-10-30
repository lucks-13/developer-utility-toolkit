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
    repo = result["Repositories"][0]

    assert repo["Repository"] == "cpython"
    assert repo["Full Name"] == "python/cpython"
    assert repo["Language"] == "Python"
    assert repo["Stars"] == 100
    mock_get.assert_called_once_with(
        "https://api.github.com/search/repositories",
        params = {
            "q": "python language:Python",
            "sort": "stars",
            "order": "desc",
            "per_page": 5
        },
        timeout=10
        )

@patch("toolkit.github_search.requests.get")
def test_search_repos_empty_results(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "total_count" : 0,
        "items" : []
    }

    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response
    result = search_repos("search-me")
    assert result["Total Results"] == 0
    assert result["Repositories"] == []

@patch("toolkit.github_search.requests.get")
def test_search_repos_not_found(mock_get):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = (requests.exceptions.HTTPError("404 Not Found"))
    mock_get.return_value = mock_response
    result = search_repos("python")
    assert result is None

@patch("toolkit.github_search.requests.get")
def test_search_repos_timeout(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout
    result = search_repos("python")
    assert result is None

@patch("toolkit.github_search.requests.get")
def test_search_repos_connection_error(mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError
    result = search_repos("python")
    assert result is None