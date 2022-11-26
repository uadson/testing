import requests


def get_github_avatar(user):
    """
    Get github avatar user and return a str with avatar link

    Args:
        user (str): github username
    """
    url = f"https://api.github.com/users/{user}"
    response = requests.get(url)
    return response.json()['avatar_url']
