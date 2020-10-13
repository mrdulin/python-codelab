def get_json_data(url, session):
    response = session.get(url)
    response.raise_for_status()
    return response.json()
