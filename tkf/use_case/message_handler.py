def get_user_session_id(user_dict: dict) -> str:
    """Gets a dict and returns the associated value with the
    key called - `cookieid`

    """
    return user_dict['cookieid']
