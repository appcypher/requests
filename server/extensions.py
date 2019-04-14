""" Module for initializing flask extensions """
from flask_migrate import Migrate
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension

# Create flask extensions instances
cors = CORS()
migrate = Migrate()
debug_toolbar = DebugToolbarExtension()
