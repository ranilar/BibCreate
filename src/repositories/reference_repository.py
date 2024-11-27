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


def manage_bookreference(id):
    # todo
    pass

# deletions by reference type (maybe joined together later??? )


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
