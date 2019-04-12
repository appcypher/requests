from flask_migrate import Migrate
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension

cors = CORS()
migrate = Migrate()
debug_toolbar = DebugToolbarExtension()
