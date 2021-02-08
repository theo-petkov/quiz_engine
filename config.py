import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = "".join([
        'sqlite:///', os.path.join(basedir, 'quiz.db')
        ])
    SQLALCHEMY_TRACK_MODIFICATIONS = False
