"""This module defines the database and table structures.

SQLAlchemy uses the table classes below to initiate and operate on any
connected database, or SQLite file.

It also houses methods to create and
check hashed user passwords.
"""

from werkzeug.security import generate_password_hash, check_password_hash

from app import db

# Constants
ANSWER_LENGTH = 200


class Users(db.Model):
    """Users table, containing basic fields to identify unique users, store
    their hashed passwords, and hold any permissions they may have.
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created_unix = db.Column(db.Integer)
    # Manually insert a 1 in the admin column for desired user
    # to have admin access. Cannot allow automatic access for
    # this kind of feature, especially since there will be
    # very few administrators.
    admin = db.Column(db.Boolean, default=0)
    answers = db.relationship('Answers', backref='users', lazy='dynamic')

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
    questions = db.relationship('Questions', backref='quizzes', lazy='dynamic')
    answers = db.relationship('Answers', backref='quizzes', lazy='dynamic')

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
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'))
    answers = db.relationship('Answers', backref='questions', lazy='dynamic')


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
