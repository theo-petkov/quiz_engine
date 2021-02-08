"""Initiating the Flask application and all of its extensions
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config


application = Flask(__name__)
application.config.from_object(Config)

# Enabling Flask extensions
db = SQLAlchemy(application)
migrate = Migrate(application, db)

# The below has been imported after a the declaration of the Flask app due
# to a circular import issue that would otherwise occur with this style of
# project structure. The reason for straying from the Python style conventions
# is to avoid this error.
from app import routes, models
