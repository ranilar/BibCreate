from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.reference_repository import *
from config import app, test_env
from util import *


@app.route("/")
def index():
    all_references = get_all_references()
    return render_template(
        "index.html",
        all_references=all_references
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

    tag_name = request.form.get("tag_name", "").strip()

    try:
        validate_reference(ref_type, **fields)
        validate_tag(tag_name)

        # valinnaisten kenttien kohdalla tyhjä merkkijono muutetaan None
        optional_fields = ["publisher", "ISBN", "volume", "DOI",
                           "url", "note", "address", "month", "organization"]
        fields = {key: (value if key not in optional_fields or value !=
                        "" else None) for key, value in fields.items()}

        if ref_type == "book":
            ref_id = create_book(fields["title"], fields["author"],
                                 fields["year"], fields["publisher"], fields["ISBN"])
        elif ref_type == "article":
            ref_id = create_article(fields["title"], fields["author"], fields["journal"],
                                    fields["year"], fields["volume"], fields["DOI"])
        elif ref_type == "misc":
            ref_id = create_misc(fields["title"], fields["author"],
                                 fields["year"], fields["url"], fields["note"])
        elif ref_type == "inproceeding":
            ref_id = create_inproceeding(
                fields["title"], fields["author"], fields["year"], fields["booktitle"],
                fields["DOI"], fields["address"], fields["month"], fields["url"], fields["organization"]
            )
        if tag_name:
            tag_id = create_or_get_tag(tag_name)
            link_tag_to_reference(tag_id, ref_id, ref_type)
            flash(f"Tag '{tag_name}' added successfully", "success")

        flash(f"{ref_type.capitalize()} citation added successfully", "success")
    except UserInputError as error:
        for message in error.error_fields:
            flash(message, "error")
        return render_template("new_reference.html", ref_type=ref_type, form_data=fields)

    return redirect("/")


@app.route("/delete/<ref_id>", methods=["POST"])
def delete_reference(ref_id):
    ref_type = request.form.get("ref_type")
    delete_reference_by_type(ref_type, ref_id)
    flash(f"{ref_type} reference deleted successfully", "success")

    return redirect("/")


@app.route("/edit_reference/<reference_id>", methods=["GET", "POST"])
def edit_reference(reference_id):

    ref_type = request.args.get(
        "ref_type") if request.method == "GET" else request.form.get("ref_type")
    reference_obj = get_reference(ref_type, reference_id)

    if not reference_obj:
        flash("Reference not found.", "error")
        return redirect("/")

    tags = get_tags_for_reference(reference_id, ref_type)

    if request.method == "GET":
        return render_template("edit_reference.html", reference=reference_obj, ref_type=ref_type, tags=tags)


    if request.method == "POST":
        reference_obj.title = request.form.get("title")

        try:
            fields = {
                "title": request.form.get("title"),
                "author": request.form.get("author"),
                "journal": request.form.get("journal"),
                "year": request.form.get("year"),
                "volume": request.form.get("volume"),
                "DOI": request.form.get("DOI"),
                "publisher": request.form.get("publisher"),
                "ISBN": request.form.get("ISBN"),
                "booktitle": request.form.get("booktitle"),
                "address": request.form.get("address"),
                "month": request.form.get("month"),
                "organization": request.form.get("organization"),
                "url": request.form.get("url"),
                "note": request.form.get("note"),
            }

            validate_reference(ref_type, **fields)

            reference_obj.author = request.form.get("author")
            reference_obj.year = int(request.form.get(
                "year")) if request.form.get("year") else None
            reference_obj.publisher = request.form.get("publisher")
            reference_obj.ISBN = request.form.get("ISBN")
            reference_obj.journal = request.form.get("journal")
            reference_obj.volume = request.form.get("volume")
            reference_obj.DOI = request.form.get("DOI")
            reference_obj.url = request.form.get("url")
            reference_obj.note = request.form.get("note")
            reference_obj.booktitle = request.form.get("booktitle")
            reference_obj.address = request.form.get("address")
            reference_obj.month = request.form.get("month")
            reference_obj.organization = request.form.get("organization")

            save_reference(reference_obj, reference_id, ref_type)

            flash("Reference updated successfully!", "success")
            return redirect("/")

        except UserInputError as error:
            for message in error.error_fields:
                flash(message, "error")
            return render_template("edit_reference.html", reference=reference_obj, ref_type=ref_type, tags=tags)


# Reitti viitehakutuloksien hakemiseen
@app.route("/search_for_reference", methods=["GET"])
def search_for_reference():

    # Lyhyt validointi
    query = request.args.get("query")
    if not query:
        flash("Search query cannot be empty", "error")
        return redirect("/")
    if len(query) < 2:
        flash("Search query must be at least 2 characters long.", "error")
        return redirect("/")
    if len(query) > 30:
        flash("Search query is limited to 30 characters.", "error")
        return redirect("/")

    # Kutsu hakumetodia ja palauta
    results = search_all_references(query)
    print(results)
    return render_template(
        "index.html",
        all_references=results, query=query
    )


@app.route("/add_tag", methods=["POST"])
def add_tag_in_edit():
    tag_name = request.form.get("tag_name")
    ref_id = request.form.get("ref_id")
    ref_type = request.form.get("ref_type")

    if not tag_name or not ref_id or not ref_type:
        flash("Missing required information for adding a tag.", "error")
        return redirect(f"/edit_reference/{ref_id}?ref_type={ref_type}")

    try:
        validate_tag(tag_name)
        tag_id = create_or_get_tag(tag_name)
        link_tag_to_reference(tag_id, ref_id, ref_type)
        flash(f"Tag '{tag_name}' added successfully", "success")
    except ValueError as ve:
        flash(f"Error: {str(ve)}", "error")
    except Exception as e:
        flash(f"Error adding tag: {str(e)}", "error")

    return redirect(f"/edit_reference/{ref_id}?ref_type={ref_type}")


@app.route("/delete_tag", methods=["POST"])
def delete_tag():
    tag_id = request.form.get("tag_id")
    ref_id = request.form.get("ref_id")
    ref_type = request.form.get("ref_type")

    if not tag_id or not ref_id or not ref_type:
        flash("Missing required information to delete a tag.", "error")
        return redirect(f"/edit_reference/{ref_id}?ref_type={ref_type}")

    try:
        sql = text("""
            DELETE FROM tags_references
            WHERE tag_id = :tag_id AND reference_id = :ref_id AND reference_type = :ref_type
        """)
        db.session.execute(
            sql, {"tag_id": tag_id, "ref_id": ref_id, "ref_type": ref_type})
        db.session.commit()

        orphan_check_sql = text("""
            SELECT COUNT(*) FROM tags_references WHERE tag_id = :tag_id
        """)
        orphan_count = db.session.execute(
            orphan_check_sql, {"tag_id": tag_id}).scalar()

        if orphan_count == 0:
            db.session.execute(text("DELETE FROM tags WHERE id = :tag_id"), {
                               "tag_id": tag_id})
            db.session.commit()

        flash("Tag deleted successfully.", "success")
    except Exception as e:
        flash(f"Error deleting tag: {str(e)}", "error")

    return redirect(f"/edit_reference/{ref_id}?ref_type={ref_type}")


# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({'message': "db reset"})
