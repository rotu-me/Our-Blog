from flask import Flask, render_template
from database import get_posts
app = Flask(__name__)


@app.route("/")
def homepage():
  posts = get_posts()
  return render_template("index.html",
                        posts = posts)

@app.route("/api/posts")
def list_posts():
  return jsonify(posts)


if (__name__) == "__main__":
  app.run(host="0.0.0.0", debug="True")
