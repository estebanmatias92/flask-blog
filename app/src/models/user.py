from utils.db import db


class User(db.Model):
    """User model for the blog user's accounts

    Args:
        db (SQLAlchemy): This model inherits from the SQLAlchemy module
    """

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    es_admin = db.Column(db.Boolean, default=False)

    posts = db.relationship("Post", backref="user", lazy=True)
    comments = db.relationship("Comment", backref="user", lazy=True)
