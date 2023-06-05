from main import app
from utils.db import init_db

# Create the database schema before anything
init_db(app)

if __name__ == "__main__":
    app.run()
