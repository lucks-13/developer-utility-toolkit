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
        
    }