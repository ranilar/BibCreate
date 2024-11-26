from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.reference_repository import *
from config import app, test_env
from util import validate_reference, UserInputError

@app.route("/")
def index():
    books = get_references_bytype("book")
    #todo muut
    return render_template("index.html", books=books)

@app.route("/new_reference")
def new():
    return render_template("new_reference.html")

@app.route("/create_reference", methods=["POST"])
def reference_creation():
    title = request.form.get("title")
    author = request.form.get("author")
    year = request.form.get("year")
    publisher = request.form.get("publisher")
    ISBN = request.form.get("ISBN")


    try:
        validate_reference(title, author, year, publisher, ISBN )
        create_book(title, author, year, publisher, ISBN )
        flash("Book citation added successfully", "success") 
        return redirect("/")
    except UserInputError as error:
        errors = error.args[0]
        for field, message in errors.items():
            flash(f"{field}: {message}", "error")
        return redirect("/new_reference")

@app.route("/delete/<id>", methods=["POST"])
def update_reference(reference_id):
    #set_done(todo_id)
    return redirect("/")


@app.route("/edit_book/<book_id>", methods=["POST"])
def edit_book(book_id):
    pass



# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })   
