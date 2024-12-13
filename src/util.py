class UserInputError(Exception):
    def __init__(self, error_fields):
        self.error_fields = error_fields
        super().__init__(error_fields)


def validate_reference(ref_type, **fields):
    error_fields = []

    required_fields = {
        "book": ["author", "title", "publisher", "year"],
        "article": ["author", "title", "journal", "year"],
        "inproceeding": ["author", "title", "booktitle", "year"],
        "misc": ["title"]
    }

    for field in required_fields.get(ref_type, []):
        if not fields.get(field):
            error_fields.append(f"{field.capitalize()} is required.")

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
                error_fields.append(f"{field.capitalize()} must be at least {min_length} characters long.")
            if len(value) > max_length:
               error_fields.append(f"{field.capitalize()} must not exceed {max_length} characters.")

    if ref_type == "book":
        isbn_value = fields.get("ISBN")
        if isbn_value:
            if len(isbn_value) != 13:
                error_fields.append("ISBN must be exactly 13 characters long.")
            if not isbn_value.isdigit():
                error_fields.append("ISBN must contain only numeric characters.")

    numeric_fields = ["year", "volume"]
    for field in numeric_fields:
        value = fields.get(field)
        if value and not value.isdigit():
            error_fields.append(f"{field.capitalize()} must be a valid number.")
    

    if error_fields:
        raise UserInputError(error_fields)


def validate_tag(tag_name):
    if not tag_name:
        return True
    if len(tag_name) < 1 or len(tag_name) > 50:
        raise ValueError("Tag name must be between 1 and 50 characters.")
    return True
