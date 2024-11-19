from app import app
from flask import render_template, request

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        year = request.form["year"]
        publisher = request.form["publisher"]
        ISBN_number = request.form["ISBN_number"]

    return render_template(index.html)