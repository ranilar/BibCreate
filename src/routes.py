from app import app
from flask import render_template, request, flash

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
        
        # Validation.
        errors = []
        
        # Check for empty fields and correct number inputs.
        if not title:
            errors.append("Title required")
        if not author:
            errors.append("Author required")
        if not year:
            errors.append("Year required")
        elif not year.isdigit() or int(year) < 0:
            errors.append("Year must be a positive number.")
        if not publisher:
            errors.append("Publisher required")
        if not ISBN_number:
            errors.append("ISBN number required")
        elif not ISBN_number.isdigit() or len(ISBN_number) not in [10, 13]:
            errors.append("ISBN number must be 10 or 13 digits.")
        
        # Display errors if found.
        if errors:
            for error in errors:
                flash(error, 'danger')
            return render_template("index.html")
            

    return render_template(index.html)