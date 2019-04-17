base_url = 'http://localhost:5000'
api_url = f'{base_url}/api/v1'
requests_url = f'{api_url}/requests'


def request_comments_url(id):
    return f'{api_url}/requests/{id}/comments'


def requests_url(id=''):
    if id:
        return f'{api_url}/requests/{id}'
    return f'{api_url}/requests'


def clients_url(id):
    return f'{api_url}/clients/{id}'


def staff_url(id):
    return f'{api_url}/staff/{id}'
