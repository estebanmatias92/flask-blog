import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure_db(app: Flask):
    """Settings for the ORM module to configure itself.
    Shares the configuration to the APP context also.

    Args:
        app (Flask): Uses the APP context
    """
    
    # Settings
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # Pass the APP instance to the ORM
    db.init_app(app)


def init_db(app: Flask):
    """Creates all the tables if not exist

    Args:
        app (Flask): Uses the APP context
    """
    # Create the database schema before anything
    with app.app_context():
        db.create_all()
