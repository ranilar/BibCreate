from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.reference_repository import get_references, create_reference
from config import app, test_env
from util import validate_reference

@app.route("/")
def index():
    references = get_references()
    return render_template("index.html", references=references)

@app.route("/new_reference")
def new():
    return render_template("new_reference.html")

@app.route("/create_reference", methods=["POST"])
def reference_creation():
    ref_type = request.form.get("ref_type")
    title = request.form.get("title")
    author = request.form.get("author")
    year = request.form.get("year")
    publisher = request.form.get("publisher")
    ISBN = request.form.get("ISBN")


    try:
        validate_reference(title, author, year, publisher, ISBN )
        create_reference(ref_type, title, author, year, publisher, ISBN )
        flash("Book citation added successfully", "success") 
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/new_reference")

@app.route("/update_reference/<reference_id>", methods=["POST"])
def update_reference(reference_id):
    #set_done(todo_id)
    return redirect("/")


# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
