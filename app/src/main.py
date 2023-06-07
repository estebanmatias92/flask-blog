from flask import Flask
from utils.db import configure_db
from models import User
from routes import posts

# Create the app
app = Flask(__name__)

# Configure DB
configure_db(app)

# Register the routes
app.register_blueprint(posts)
