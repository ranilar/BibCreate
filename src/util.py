class UserInputError(Exception):
    pass

def validate_reference(title, author, year, publisher, ISBN):
    if len(title) < 5:
        raise UserInputError("Title length must be at least 5 characters.")
    if len(title) > 100:
        raise UserInputError("Title length must be smaller than 100 characters.")
    if len(author) < 5:
        raise UserInputError("Author length must be at least 5 characters.")
    if len(author) > 100:
        raise UserInputError("Author length must be smaller than 100 characters.")
    if not year.isdigit() or int(year) < 0:
        raise UserInputError("Year must be a valid positive number.")
    if len(publisher) < 5:
        raise UserInputError("Publisher length must be at least 5 characters.")
    if len(publisher) > 100:
        raise UserInputError("Publisher length must be smaller than 100 characters.")
    if len(ISBN) != 13 or not ISBN.isdigit():
        raise UserInputError("ISBN must be a 13-digit number.")