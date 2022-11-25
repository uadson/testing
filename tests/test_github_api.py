import pytest
from unittest.mock import Mock
from ..app import github_api


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = "https://avatars.githubusercontent.com/u/62815552?v=4"
    resp_mock.json.return_value = {
        "login": "uadson",
        "id": 62815552,
        "avatar_url": url,
    }
    get_main = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = get_main
    

def test_get_github_avatar(avatar_url):
    url = github_api.get_github_avatar('uadson')
    assert avatar_url == url


def test_get_github_avatar_integration():
    url = github_api.get_github_avatar('uadson')
    assert 'https://avatars.githubusercontent.com/u/62815552?v=4' == url
