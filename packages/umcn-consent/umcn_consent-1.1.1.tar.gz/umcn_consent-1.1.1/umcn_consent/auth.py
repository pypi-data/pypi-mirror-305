import requests


def authenticate(username, password, client_id, auth_token):
    """
    Initializes an authenticated requests session based on configuration data.

    Returns
    -------
    requests.Session or None
        An authenticated session if the data is correct, or None if required
        configuration data is missing or in case of an error.

    """
    if not username or not password:
        raise ValueError("Username or password cannot be empty")

    if not client_id or not auth_token:
        raise ValueError("Client ID or Auth Token cannot be empty")

    try:
        session = requests.sessions.Session()
        session.auth = (username, password)
        session.headers.update(
            {
                "Client-ID": client_id,
                "Authorization": auth_token,
            }
        )
        return session
    except requests.RequestException as e:
        raise requests.RequestException(f"Failed to create a session: {e}") from e
