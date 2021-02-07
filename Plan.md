# Quiz Engine Plan

This denotes the blueprints for the quiz engine, to help during the building of the application, as well as to shed light on the features, and the reasoning behind them.

## Model

The database will be built on the SQLAlchemy ORM, and using a SQLite database. SQLite is great for testing, as it's just a file, and the database url can be pointed to a more heavyweight database server at a later time, when the features are deemed more complete, and with no application changes.

The changes of the database will be tracked using flask-migrate, to make sure migrations are relatively smooth.

The structure of the database, as well as the tables within, are in the `models.py` file.

## API Routes


