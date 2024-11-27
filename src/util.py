class UserInputError(Exception):
    pass

def validate_reference(ref_type, **fields):
    errors = {}

    # Yhteiset kentät
    if ref_type != "misc":
        if not fields.get("title") or len(fields["title"]) < 5:
            errors["title"] = "Title must be at least 5 characters long."
        if fields.get("title") and len(fields["title"]) > 100:
            errors["title"] = "Title length must be smaller than 100 characters."
        if not fields.get("author") or len(fields["author"]) < 5:
            errors["author"] = "Author must be at least 5 characters long."
        if fields.get("author") and len(fields["author"]) > 100:
            errors["author"] = "Author length must be smaller than 100 characters."

    if ref_type == "book":
        if not fields.get("publisher") or len(fields["publisher"]) < 5:
            errors["publisher"] = "Publisher must be at least 5 characters long."
        if not fields.get("ISBN") or len(fields["ISBN"]) != 13:
            errors["ISBN"] = "ISBN must be exactly 13 digits."
    elif ref_type == "article":
        if not fields.get("journal") or len(fields["journal"]) < 5:
            errors["journal"] = "Journal must be at least 5 characters long."
        if fields.get("volume") and not fields["volume"].isdigit():
            errors["volume"] = "Volume must be a valid number."
    elif ref_type == "inproceedings":
        if not fields.get("booktitle") or len(fields["booktitle"]) < 5:
            errors["booktitle"] = "Booktitle must be at least 5 characters long."
        if fields.get("DOI") and len(fields["DOI"]) < 5:
            errors["DOI"] = "DOI must be at least 5 characters long."
    elif ref_type == "misc":
        if not any(fields.values()):
            errors["misc"] = "At least one field must be filled for a Misc reference."

    if errors:
        raise UserInputError(errors)

