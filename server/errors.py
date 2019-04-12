class ApplicationError(Exception):
    def __init__(self, message, status_code=400):
        super().__init__(message)

        self.status_code = status_code
        self.error = {'success': 'failure', 'message': message}


class ClientError(ApplicationError):
    def __init__(self, message, status_code=400):
        super().__init__(message, status_code)


class ServerError(ApplicationError):
    def __init__(self, message, status_code=500):
        super().__init__(message)
