import requests
from unittest.mock import Mock, patch

from toolkit.github_user import get_user

@patch("toolkit.github_user.requests.get")
def test_get_user_success(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "login" : "torvalds",
        "name" : "Linus Torvalds",
        "bio" : None,
        "location" : "Portland",
        "company" : None,
        "public_repos" : 7,
        "followers" : 200000,
        "following" : 0,
        "type" : "User",
        "created_at" : "2011-09-03T15:26:22Z",
        "html_url" : "https://github.com/torvalds"
    }

    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = get_user("torvalds")
    assert result["Username"] == "torvalds"
    assert result["Name"] == "Linus Torvalds"
    assert result["Bio"] == "Not Available"
    assert result["Location"] == "Portland"
    assert result["Public Repos"] == 7
    assert result["Followers"] == 200000
    assert result["following"] == 0

    mock_get.assert_called_once_with("https://api.github.com/users/torvalds",timeout=10)

@patch("toolkit.github_user.requests.get")
def test_get_user_not_found(mock_get):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = (requests.exceptions.HTTPError("404 Not Found"))
    mock_get.return_value = mock_response
    result = get_user("fake-user")
    assert result is None

@patch("toolkit.github_user.requests.get")
def test_get_user_timeout(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout
    result = get_user("torvalds")
    assert result is None

@patch("toolkit.github_user.requests.get")
def test_get_user_connection_error(mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError
    result = get_user("torvalds")
    assert result is None