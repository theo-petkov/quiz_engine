"""This module defines the routes for the API of the quiz engine.

This would be connected to the frontend in order to accept user inputs
from both admins, and regular users, and retreive, or act on the
database accordingly.
"""


import re

from flask import request
from flask_api import status

from app import application, db
from app.models import Users, Quizzes, Questions, Answers, EMAIL_LENGTH


# Constants
EMAIL_VALIDATION = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'


@application.route('/')
def index():
    """A simple homepage to easily know if the server is running
    when deployed.
    """
    return 'Quiz Engine', status.HTTP_200_OK


@application.route('/api/v1/create_user', methods=['POST'])
def create_user():
    """Create a user, once supplied with a JSON payload that
    includes an email and a password.

    The JSON should be in the format:
    {
        "email": "example@example.com",
        "password": "examplepass"
    }

    The response will be a short message and an HTTP status code
    """
    user_data = request.get_json()
    # Make sure the correct payload is received.
    if 'email' not in user_data or 'password' not in user_data:
        return 'User data not provided.', status.HTTP_400_BAD_REQUEST
    email = user_data['email']
    # Check that email length is acceptable.
    if len(email) > EMAIL_LENGTH:
        return (
            'The email provided was too long',
            status.HTTP_400_BAD_REQUEST
        )
    # Verify email structure using regex, else fail.
    if not bool(re.match(EMAIL_VALIDATION, email)):
        return (
            'The email provided was not valid',
            status.HTTP_400_BAD_REQUEST
            )
    # Check that email has not been previously used.
    if Users.query.filter_by(email=email).first() is not None:
        return (
            'This email is already in use',
            status.HTTP_400_BAD_REQUEST
            )
    password = user_data['password']
    # Create user in database.
    user = Users(email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return 'User created successfully', status.HTTP_201_CREATED


@application.route('/api/v1/create_quiz', methods=['POST'])
def create_quiz():
    """Create a quiz, once supplied with a JSON payload that
    includes the email and a password of an administrator,
    as well as a quiz name.

    The JSON should be in the format:
    {
        "email": "example.admin@example.com",
        "password": "examplepass",
        "quiz": "example title"
    }

    The response will be a short message and an HTTP status code
    """
    quiz_data = request.get_json()
    if (
            'email' not in quiz_data
            and 'password'not in quiz_data
            and 'quiz' not in quiz_data
            ):
        return 'Quiz data not provided.', status.HTTP_400_BAD_REQUEST
    user = Users.query.filter_by(email=quiz_data['email']).first()
    if user is None or not user.check_password(quiz_data['password']):
        return 'Wrong credentials', status.HTTP_400_BAD_REQUEST
    if user.admin != 1:
        return (
            'This user cannot perform this action',
            status.HTTP_403_FORBIDDEN
            )
    quiz = Quizzes(title=quiz_data['quiz'])
    db.session.add(quiz)
    db.session.commit()
    return 'Quiz created successfully', status.HTTP_201_CREATED
