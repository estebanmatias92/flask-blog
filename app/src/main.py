from flask import Flask
from routes.posts import posts

# Create the app
app = Flask(__name__)


# Register the routes
app.register_blueprint(posts)
