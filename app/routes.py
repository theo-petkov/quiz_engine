"""This module defines the routes for the API of the quiz engine.

This would be connected to the frontend in order to accept user inputs
from both admins, and regular users, and retreive, or act on the
database accordingly.
"""


from app import application


@application.route('/')
def index():
    """A simple homepage to easily know if the server is running
    when deployed.
    """
    return 'Quiz Engine'
