from config import db
from sqlalchemy import text
from entities.reference import Book, Article, Misc, Inproceedings


def get_references_bytype(ref_type):
    sql = text(f"SELECT * FROM {ref_type}_references")
    result = db.session.execute(sql)
    references = result.fetchall()

    if ref_type == "book":
        return [Book(*reference) for reference in references]
    if ref_type == "article":
        return [Article(*reference) for reference in references]
    if ref_type == "misc":
        return [Misc(*reference) for reference in references]
    if ref_type == "inproceedings":
        return [Inproceedings(*reference) for reference in references]


def create_book(title, author, year, publisher, ISBN):
    sql = text(
        """
        INSERT INTO book_references (title, author, year, publisher, ISBN)
        VALUES (:title, :author, :year, :publisher, :ISBN)
    """
    )
    db.session.execute(
        sql,
        {
            "title": title,
            "author": author,
            "year": year,
            "publisher": publisher,
            "ISBN": ISBN,
        },
    )
    db.session.commit()


def create_article(title, author, journal, year, volume, DOI):
    sql = text(
        """
        INSERT INTO article_references (title, author, journal, year, volume, DOI)
        VALUES (:title, :author, :journal, :year, :volume, :DOI)
        """
    )
    db.session.execute(
        sql,
        {
            "title": title,
            "author": author,
            "journal": journal,
            "year": year,
            "volume": volume,
            "DOI": DOI,
        },
    )
    db.session.commit()


def create_misc(title, author, year, url, note):
    sql = text(
        """
        INSERT INTO misc_references (title, author, year, url, note)
        VALUES (:title, :author, :year, :url, :note)
        """
    )
    db.session.execute(
        sql,
        {
            "title": title,
            "author": author if author else None,
            "year": int(year) if year and year.isdigit() else None,
            "url": url if url else None,
            "note": note if note else None,
        },
    )
    db.session.commit()


def create_inproceedings(title, author, year, booktitle, DOI, address, month, url, organization):
    sql = text(
        """
        INSERT INTO inproceedings_references (title, author, year, booktitle, DOI, address, month, url, organization)
        VALUES (:title, :author, :year, :booktitle, :DOI, :address, :month, :url, :organization)
        """
    )
    db.session.execute(
        sql,
        {
            "title": title,
            "author": author,
            "year": year,
            "booktitle": booktitle,
            "DOI": DOI,
            "address": address,
            "month": month,
            "url": url,
            "organization": organization,
        },
    )
    db.session.commit()


def get_reference(ref_type, ref_id):
    if ref_type == "book":
        sql = text("SELECT * FROM book_references WHERE id = :id")
        result = db.session.execute(sql, {"id": ref_id})
        reference = result.fetchall()
        return Book(*reference[0])

    elif ref_type == "article":
        sql = text("SELECT * FROM article_references WHERE id = :id")
        result = db.session.execute(sql, {"id": ref_id})
        reference = result.fetchall()
        return Article(*reference[0])

    elif ref_type == "misc":
        sql = text("SELECT * FROM misc_references WHERE id = :id")
        result = db.session.execute(sql, {"id": ref_id})
        reference = result.fetchall()
        return Misc(*reference[0])

    elif ref_type == "inproceedings":
        sql = text("SELECT * FROM inproceedings_references WHERE id = :id")
        result = db.session.execute(sql, {"id": ref_id})
        reference = result.fetchall()
        return Inproceedings(*reference[0])


def delete_reference_bytype(ref_type, ref_id):
    if ref_type == "book":
        sql = text("DELETE FROM book_references WHERE id = :id")
        db.session.execute(sql, {"id": ref_id})
        db.session.commit()

    elif ref_type == "article":
        sql = text("DELETE FROM article_references WHERE id = :id")
        db.session.execute(sql, {"id": ref_id})
        db.session.commit()

    elif ref_type == "misc":
        sql = text("DELETE FROM misc_references WHERE id = :id")
        db.session.execute(sql, {"id": ref_id})
        db.session.commit()

    elif ref_type == "inproceedings":
        sql = text("DELETE FROM inproceedings_references WHERE id = :id")
        db.session.execute(sql, {"id": ref_id})
        db.session.commit()


def save_reference(reference, reference_id, ref_type):
    if ref_type == "book":
        sql = text("""
            UPDATE book_references
            SET title = :title, author = :author, year = :year, publisher = :publisher, ISBN = :ISBN
            WHERE id = :id
        """)
        db.session.execute(
            sql,
            {
                "id": reference_id,
                "title": reference.title,
                "author": reference.author,
                "year": reference.year,
                "publisher": reference.publisher,
                "ISBN": reference.ISBN,
            },
        )

    elif ref_type == "article":
        sql = text("""
            UPDATE article_references
            SET title = :title, author = :author, journal = :journal, year = :year, volume = :volume, DOI = :DOI
            WHERE id = :id
        """)
        db.session.execute(
            sql,
            {
                "id": reference_id,
                "title": reference.title,
                "author": reference.author,
                "journal": reference.journal,
                "year": reference.year,
                "volume": reference.volume,
                "DOI": reference.DOI,
            },
        )

    elif ref_type == "misc":
        sql = text("""
            UPDATE misc_references
            SET title = :title, author = :author, year = :year, url = :url, note = :note
            WHERE id = :id
        """)
        db.session.execute(
            sql,
            {
                "id": reference_id,
                "title": reference.title,
                "author": reference.author,
                "year": reference.year,
                "url": reference.url,
                "note": reference.note,
            },
        )

    elif ref_type == "inproceedings":
        sql = text("""
            UPDATE inproceedings_references
            SET title = :title, author = :author, year = :year, booktitle = :booktitle, DOI = :DOI,
                address = :address, month = :month, url = :url, organization = :organization
            WHERE id = :id
        """)
        db.session.execute(
            sql,
            {
                "id": reference_id,
                "title": reference.title,
                "author": reference.author,
                "year": reference.year,
                "booktitle": reference.booktitle,
                "DOI": reference.DOI,
                "address": reference.address,
                "month": reference.month,
                "url": reference.url,
                "organization": reference.organization,
            },
        )

    db.session.commit()
