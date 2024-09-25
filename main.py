from flask import Flask, render_template, request, redirect
import db

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html")


@app.route ("/categories")
def categories_list():
    return render_template("category_list.html", category_list=db.get_categories())

@app.route("/posts", methods=["GET","POST"])
def posts():
    if request.method == "POST":
        category_id = request.form.get("category_id")
        text = request.form.get("text")
        #validate category_id
        db.addPost(category_id, text)
         
        return redirect(f"/posts")
    return render_template("post_list.html", post_list=db.get_posts())

@app.route("/categories/<id>", methods=["GET","POST"])
def posts_by_category(id):



    if request.method == "POST":
        category_id = request.form.get("category_id")
        text = request.form.get("text")
        #validate category_id
        db.add_post(category_id, text)
         
        return redirect(f"/categories/{id}")
    return render_template("post_list.html", post_list =db.get_posts_by_category(id), 
                           category_page=True
                           )

@app.route("/post/delete/<id>")
@app.route("/post/delete/<id>/<category_id>")
def delete_post(id, category_id=None):

    db.deletePost(id)

    if category_id:
        return redirect(f"/categories/{category_id}")
    return redirect("/posts")


@app.route("/post/view/<id>")
def post_view(id):
    return render_template("post_view.html", 
                           post= db.getOnePost(id)
                           
                           )




if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")


