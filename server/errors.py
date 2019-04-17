""" Module for implementing custom exceptions. """


class ApplicationError(Exception):
    """
    The base implementation for application-related errors.
    """

    def __init__(self, message, status_code=400):
        """
        Initialises the error instance with given message and status code.

        Args:
            message (str): error message.
            status_code (int): status code.
        """
        super().__init__(message)

        self.status_code = status_code
        self.message = message


class ClientError(ApplicationError):
    """
    Used to represent client errors. Client errors usually have 400 or 300
    status codes.
    """

    def __init__(self, message, status_code=400):
        """
        Initialises the error instance with given message and status code.

        Args:
            message (str): error message.
            status_code (int): status code.
        """
        super().__init__(message, status_code)
