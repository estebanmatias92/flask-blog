from utils.db import db
from base import Base


class User(Base):
    """User model for the blog user's accounts

    Args:
        db (SQLAlchemy): This model inherits from the SQLAlchemy Model
    """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    posts = db.relationship("Post", backref="users", lazy=True)
    comments = db.relationship("Comment", backref="users", lazy=True)