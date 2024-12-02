class UserInputError(Exception):
    pass


def validate_reference(ref_type, **fields):
    errors = {}

    required_fields = {
        "book": ["author", "title", "publisher", "year"],
        "article": ["author", "title", "journal", "year"],
        "inproceeding": ["author", "title", "booktitle", "year"],
        "misc": ["title"]
    }

    for field in required_fields.get(ref_type, []):
        if not fields.get(field):
            errors[field] = f"{field.capitalize()} is required."

    fields_with_limits = {
        "title": (1, 100),
        "author": (1, 100),
        "publisher": (1, 100),
        "journal": (1, 100),
        "booktitle": (1, 100),
        "note": (0, 100),
        "address": (0, 100),
        "month": (0, 100),
        "organization": (0, 100),
        "DOI": (0, 100),
    }

    for field, (min_length, max_length) in fields_with_limits.items():
        value = fields.get(field)
        if value:
            if len(value) < min_length:
                errors[field] = f"{field.capitalize()} must be at least {min_length} characters long."
            if len(value) > max_length:
                errors[field] = f"{field.capitalize()} must not exceed {max_length} characters."

    if ref_type == "book":
        isbn_value = fields.get("ISBN")
        if isbn_value:
            if len(isbn_value) != 13:
                errors["ISBN"] = "ISBN must be exactly 13 characters long."
            elif not isbn_value.isdigit():
                errors["ISBN"] = "ISBN must contain only numeric characters."

    numeric_fields = ["year", "volume"]
    for field in numeric_fields:
        value = fields.get(field)
        if value and not value.isdigit():
            errors[field] = f"{field.capitalize()} must be a valid number."

    if errors:
        raise UserInputError(errors)
