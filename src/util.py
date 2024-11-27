class UserInputError(Exception):
    pass


def validate_reference(ref_type, **fields):
    errors = {}

    # Yhteiset kentät
    if ref_type != "misc":
        if not fields.get("title") or len(fields["title"]) < 1:
            errors["title"] = "Title must include at least 1 character."
        if fields.get("title") and len(fields["title"]) > 100:
            errors["title"] = "Title length must not be more than 100 characters."
        if not fields.get("author") or len(fields["author"]) < 1:
            errors["author"] = "Author must include at least 1 character."
        if fields.get("author") and len(fields["author"]) > 100:
            errors["author"] = "Author length must not be more than 100 characters."

    if ref_type == "book":
        if fields.get("publisher") and len(fields["publisher"]) < 2:
            errors["publisher"] = "Publisher must be at least 2 characters long."
        if not fields.get("ISBN") or len(fields["ISBN"]) != 13:
            errors["ISBN"] = "ISBN must be exactly 13 digits."
    elif ref_type == "article":
        if not fields.get("journal") or len(fields["journal"]) < 2:
            errors["journal"] = "Journal must be at least 2 characters long."
        if fields.get("volume") and not fields["volume"].isdigit():
            errors["volume"] = "Volume must be a number."
    elif ref_type == "inproceedings":
        if not fields.get("booktitle") or len(fields["booktitle"]) < 1:
            errors["booktitle"] = "Booktitle must include at least 1 character."
        if fields.get("DOI") and len(fields["DOI"]) < 5:
            errors["DOI"] = "DOI must be at least 5 characters long."
    elif ref_type == "misc":
        if not any(fields.values()):
            errors["misc"] = "At least one field must be filled for a Misc reference."

    if errors:
        raise UserInputError(errors)
