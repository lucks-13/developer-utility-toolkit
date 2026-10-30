import requests
from unittest.mock import Mock, patch

from toolkit.github_user import get_user

@patch("toolkit.github_user.requests.get")
