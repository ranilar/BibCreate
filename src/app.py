from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.reference_repository import *
from config import app, test_env
from util import *


@app.route("/")
def index():
    books = get_references_bytype("book")
    articles = get_references_bytype("article")
    miscs = get_references_bytype("misc")
    inproceedings = get_references_bytype("inproceedings")

    return render_template(
        "index.html",
        books=books,
        articles=articles,
        miscs=miscs,
        inproceedings=inproceedings
    )


@app.route("/new_reference")
def new():
    return render_template("new_reference.html")

@app.route("/create_reference", methods=["POST"])
def reference_creation():
    ref_type = request.form.get("ref_type")
    fields = {
        "title": request.form.get("title"),
        "author": request.form.get("author"),
        "year": request.form.get("year"),
        "publisher": request.form.get("publisher"),
        "ISBN": request.form.get("ISBN"),
        "journal": request.form.get("journal"),
        "volume": request.form.get("volume"),
        "DOI": request.form.get(f"DOI-{ref_type}"),
        "url": request.form.get(f"url-{ref_type}"),
        "note": request.form.get("note"),
        "booktitle": request.form.get("booktitle"),
        "address": request.form.get("address"),
        "month": request.form.get("month"),
        "organization": request.form.get("organization"),
    }

    try:
        validate_reference(ref_type, **fields)
        if ref_type == "book":
            create_book(fields["title"], fields["author"], fields["year"], fields["publisher"], fields["ISBN"])
        elif ref_type == "article":
            create_article(fields["title"], fields["author"], fields["journal"], fields["year"], fields["volume"], fields["DOI"])
        elif ref_type == "misc":
            create_misc(fields["title"], fields["author"], fields["year"], fields["url"], fields["note"])
        elif ref_type == "inproceedings":
            create_inproceedings(
                fields["title"], fields["author"], fields["year"], fields["booktitle"],
                fields["DOI"], fields["address"], fields["month"], fields["url"], fields["organization"]
            )
        flash(f"{ref_type.capitalize()} citation added successfully", "success")
    except UserInputError as error:
        for field, message in error.args[0].items():
            flash(f"{field}: {message}", "error")
        return render_template("new_reference.html", ref_type=ref_type, form_data=fields)

    except Exception as error:
        flash(str(error), "error")
        return redirect("/new_reference")
    return redirect("/")

@app.route("/delete/<id>", methods=["POST"])
def delete_reference(id):
    ref_type = request.form.get("ref_type")
    delete_reference_bytype(ref_type, id)
    flash(f"{ref_type} reference deleted successfully", "success")
    # except Exception:
    #     flash(f"Failed to delete {ref_type} reference")
    return redirect("/")

@app.route("/edit_reference/<reference_id>", methods=["GET", "POST"])
def edit_reference(reference_id):
    
    ref_type = request.args.get("ref_type") if request.method == "GET" else request.form.get("ref_type")
    print(ref_type)
    reference_obj = get_reference(ref_type, reference_id)
    print("works")
    if not reference_obj:
        flash("Reference not found.", "error")
        return redirect("/") 

    if request.method == "GET":
        return render_template("edit_reference.html", reference=reference_obj, ref_type=ref_type)

    elif request.method == "POST":
        reference_obj.title = request.form.get("title")
        if isinstance(reference_obj, Book):
            reference_obj.author = request.form.get("author")
            reference_obj.year = int(request.form.get("year")) if request.form.get("year") else None
            reference_obj.publisher = request.form.get("publisher")
            reference_obj.ISBN = request.form.get("ISBN")
        elif isinstance(reference_obj, Article):
            reference_obj.author = request.form.get("author")
            reference_obj.journal = request.form.get("journal")
            reference_obj.year = int(request.form.get("year")) if request.form.get("year") else None
            reference_obj.volume = request.form.get("volume")
            reference_obj.DOI = request.form.get("DOI")
        elif isinstance(reference_obj, Misc):
            reference_obj.author = request.form.get("author")
            reference_obj.year = int(request.form.get("year")) if request.form.get("year") else None
            reference_obj.url = request.form.get("url")
            reference_obj.note = request.form.get("note")
        elif isinstance(reference_obj, Inproceedings):
            reference_obj.author = request.form.get("author")
            reference_obj.year = int(request.form.get("year")) if request.form.get("year") else None
            reference_obj.booktitle = request.form.get("booktitle")
            reference_obj.DOI = request.form.get("DOI")
            reference_obj.address = request.form.get("address")
            reference_obj.month = request.form.get("month")
            reference_obj.url = request.form.get("url")
            reference_obj.organization = request.form.get("organization")

        flash("Reference updated successfully!", "success")
        return redirect("/")



# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })   
