# Quiz Engine Plan

This denotes the blueprints for the quiz engine, to help during the building of the application, as well as to shed light on the features, and the reasoning behind them.

## Model

The database will be built on the SQLAlchemy ORM, and using an SQLite database. SQLite is great for testing, as it's just a file, and the database url can be pointed to a more heavyweight database server at a later time, when the features are deemed more complete, and with no further application changes required.

The changes of the database will be tracked using flask-migrate, to make sure migrations are relatively smooth.

The structure of the database, as well as the tables within, are defined in the `models.py` file.

The tables are: "users", "quizzes", "questions" and "answers".

The "users" table will hold user credentials, as well as permissions.

The "quizzes" table will hold quiz titles.

The "questions" table will hold the questions themselves, as well as the correct answer, and three incorrect options.

The "answers" table will have the answer to each question, provided 

Foreign keys should dictate that if a user, quiz, or question is deleted, then the respective answers connected to any of those should also be deleted, as it would seem redundant to keep records of answers that are not associated with one of these entities, although it may be required to keep those, in which case a different approach may be used.

Foreign keys should dictate that if a quiz is deleted, then the associated questions should also be deleted.

To improve speed of inter-user statistics, it may be useful to implement a summary table, whereby only the final score of a quiz, for a given user, is recorded. This can be done in a future migration.

## API Routes

- A basic home page should exist (GET request), just to be able to easily ping the server and see a valid response when it's running. It is only to be used for this purpose.

- A POST request to create a user with a hashed password.

- A GET request to obtain all available quizzes for a given user, provided an email and password have been correctly supplied. This should later be replaced with a token system that is attached to a user session, and is passed through a TLS1.2 protocol or higher (this applies to any user specific queries). To filter the correct quizzes, any quizzes with answers in the answers table, from this user, should be omitted from the selection.

- A GET request to send quiz results to user's email address.

- A POST request to submit all given answers for a quiz, for a user, which also determines the correct answers for each question.

- A GET request to obtain the total score for a given quiz, for a given user.

- A GET request to obtain all answers for a given quiz, for a given user.

- A GET request to obtain all quizzes, in order to simply display what's available overall.

- A POST request to create a quiz (admin only).

- A POST request to add questions to a quiz (admin only).

- A DELETE request to remove a quiz (admin only).

- A DELETE request to remove a question for a quiz (admin only).
