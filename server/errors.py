""" Module for implementing custom exceptions """


class ApplicationError(Exception):
    """
    The base implementation for other types od errord
    """
    def __init__(self, message, status_code=400):
        """
        Initialises the error instance with given message and status code

        Arguments:
            message (str): error message
            status_code (int): status code
        """
        super().__init__(message)

        self.status_code = status_code
        self.error = {'success': 'failure', 'message': message}


class ClientError(ApplicationError):
    """
    Used to represent client errors. Client errors usually have 400 or 300
    status codes
    """
    def __init__(self, message, status_code=400):
        """
        Initialises the error instance with given message and status code

        Arguments:
            message (str): error message
            status_code (int): status code
        """
        super().__init__(message, status_code)


class ServerError(ApplicationError):
    """
    Used to represent server errors. Server errors usually have 500
    status codes
    """
    def __init__(self, message, status_code=500):
        """
        Initialises the error instance with given message and status code

        Arguments:
            message (str): error message
            status_code (int): status code
        """
        super().__init__(message, status_code)
