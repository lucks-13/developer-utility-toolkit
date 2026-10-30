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
    
