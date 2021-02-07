from flask import Flask

application = Flask(__name__)

# The below has been imported after a variable declaration due to a circular
# import issue that would otherwise occur with this style of project structure.
# The reason for straying from the Python style conventions is to avoid this
# error.
from app import routes
