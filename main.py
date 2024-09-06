from flask import Flask, render_template
import db

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html")


@app.route ("/categories")
def categories_list():
    return render_template("category_list.html", category_list=db.get_categories())

@app.route("/posts")
def posts():
    return render_template("post_list.html", post_list=db.get_posts())

@app.route("/categories/<id>")
def posts_by_category(id):
    return render_template("post_list.html", post_list =db.get_posts_by_category(id))

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")

