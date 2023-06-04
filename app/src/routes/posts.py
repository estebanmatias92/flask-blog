from flask import Blueprint, render_template

# posts = Blueprint("posts", __name__, url_prefix="/posts")
posts = Blueprint("posts", __name__)


@posts.route("/")
def home():
    return render_template("posts.html")
