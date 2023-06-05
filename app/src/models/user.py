from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    es_admin = Column(Boolean, default=False)
    
    posts = relationship('Post', backref='users', lazy=True)
    comments = relationship('Comment', backref='users', lazy=True)
