from unittest.mock import Mock, patch
from toolkit.github_api import get_repo

@patch("toolkit.github_api.requests.get")
def test_get_repo_success(mock_get):
    mock_response = Mock()

    mock_response.json.return_value = {
        "name" : "cpython",
        "owner" : {"login": "python"},
        "description" : "Python programming language",
        "language":
    }