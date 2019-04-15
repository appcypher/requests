""" Module for initializing flask extensions. """
from flask_migrate import Migrate
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension

# Enable cross-origin requests
cors = CORS()

# Needed from creating and managing migration files
migrate = Migrate()

# Toolbar for getting debug information about flask app
debug_toolbar = DebugToolbarExtension()
