""" Module for serving static files. """
from flask import send_from_directory


def serve_index():
    """
    Serves `index.html` for root endpoints.
    """
    return send_from_directory('../client', 'index.html')


def serve_files(path):
    """
    Serves files using the path provided.

    Args:
        path (str): resource path.
    """
    return send_from_directory('../client/dist', path)
