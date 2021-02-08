"""This module defines the database and table structures.

SQLAlchemy uses the table classes below to initiate and operate on any
connected database, or SQLite file.

It also houses methods to create and
check hashed user passwords.
"""


from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from app import db


# Constants
ANSWER_LENGTH = 200
EMAIL_LENGTH = 120


class Users(db.Model):
    """Users table, containing basic fields to identify unique users, store
    their hashed passwords, and hold any permissions they may have.
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(EMAIL_LENGTH), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # When user was created as a utc datetime
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # Manually insert a 1 in the admin column for desired user
    # to have admin access. Cannot allow automatic access for
    # this kind of feature, especially since there will be
    # very few administrators.
    admin = db.Column(db.Boolean, default=0)
    answers = db.relationship('Answers', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.email)


class Quizzes(db.Model):
    """A simple table to hold quiz ids, and their titles
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    questions = db.relationship('Questions', backref='quiz', lazy='dynamic')
    answers = db.relationship('Answers', backref='quiz', lazy='dynamic')

    def __repr__(self):
        return '<Quiz {}>'.format(self.title)


class Questions(db.Model):
    """This table holds the questions, their answers, and the
    quizzes they belong to.
    """
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(600))
    correct_choice = db.Column(db.String(ANSWER_LENGTH))
    false_first = db.Column(db.String(ANSWER_LENGTH))
    false_second = db.Column(db.String(ANSWER_LENGTH))
    false_third = db.Column(db.String(ANSWER_LENGTH))
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'))
    answers = db.relationship('Answers', backref='question', lazy='dynamic')

    def __repr__(self):
        return '<Question {}>'.format(self.question)


class Answers(db.Model):
    """This table will hold all the answers for questions,
    for each user, for each quiz, and will be where any
    statistics are derived from.

    If a user has entries for a quiz within this table, then this quiz
    should no longer be able to be accessed by that user.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    # A record of the chosen answer by the user
    answer = db.Column(db.String(ANSWER_LENGTH))
    # 1 for correct answer, 0 for wrong answer
    correct = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
