import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure_db(app: Flask):
    """_summary_

    Args:
        app (Flask): _description_
    """
    
    # Settings
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # Pass the APP instance to the ORM
    db.init_app(app)


def init_db(app: Flask):
    """_summary_

    Args:
        app (Flask): _description_
    """
    # Create the database schema before anything
    with app.app_context():
        db.create_all()
