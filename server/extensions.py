""" Module for initializing flask extensions. """
from flask_migrate import Migrate
from flask_cors import CORS

# Enable cross-origin requests
cors = CORS()

# Needed from creating and managing migration files
migrate = Migrate()
