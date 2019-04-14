""" Module for serving static files """
from flask import send_from_directory


def serve_index():
    """
    Serves `index.html` for root endpoints 

    Arguments:
        message (str): error message
        status_code (int): status code
    """
    return send_from_directory('../client', 'index.html')


def serve_files(path):
    """
    Serves files using the path provided

    Arguments:
        path (str): file path
    """
    return send_from_directory('../client/dist', path)
