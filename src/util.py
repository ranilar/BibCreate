class UserInputError(Exception):
    pass

def validate_reference(title, author, year, publisher, ISBN):
    errors= {}
    if len(title) < 5:
        errors["title"] = "Title length must be at least 5 characters."
    if len(title) > 100:
        errors["title"] = "Title length must be smaller than 100 characters."
    if len(author) < 5:
        errors["author"] = "Author length must be at least 5 characters."
    if len(author) > 100:
        errors["author"] = "Author length must be smaller than 100 characters."
    if not year.isdigit() or int(year) < 0:
        errors["author"] = "Year must be a valid positive number."
    if len(publisher) < 5:
        errors["publisher"] = "Publisher length must be at least 5 characters."
    if len(publisher) > 100:
        errors["publisher"] = "Publisher length must be smaller than 100 characters."
    if len(ISBN) != 13 or not ISBN.isdigit():
        errors["ISBN"] = "ISBN must be a 13-digit number."

    if errors:
        raise UserInputError(errors)