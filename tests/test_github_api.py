import pytest
from unittest.mock import Mock
from ..app import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = "https://avatars.githubusercontent.com/u/62815553?v=4"
    resp_mock.json.return_value = {
        "login": "uadson",
        "id": 62815553,
        "avatar_url": url,
    }
    get_mock=mocker.patch('testing.app.github_api.requests.get')
    get_mock.return_value=resp_mock
    return url
    

def test_get_github_avatar(avatar_url):
    url = github_api.get_github_avatar('uadson')
    assert avatar_url == url


def test_get_github_avatar_integration():
    url = github_api.get_github_avatar('uadson')
    assert 'https://avatars.githubusercontent.com/u/62815552?v=4' == url
