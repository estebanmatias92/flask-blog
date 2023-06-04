import os
from flask import Flask
from routes.posts import posts

# Create the app
app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Register the routes
app.register_blueprint(posts)
