from config import db
from sqlalchemy import text

from entities.reference import Reference

def get_references():
    result = db.session.execute(
        text("SELECT id, ref_type, title, author, year, publisher, ISBN FROM book_references")
    )
    references = result.fetchall()
    return [
        Reference(reference[0], reference[1], reference[2], reference[3], reference[4], reference[5], reference[6])
        for reference in references
    ]


def create_reference(ref_type, title, author, year, publisher, ISBN):
    sql = text(
        """
        INSERT INTO book_references (ref_type, title, author, year, publisher, ISBN) 
        VALUES (:ref_type, :title, :author, :year, :publisher, :ISBN)
    """
    )

    db.session.execute(
        sql,
        {"ref_type": ref_type, "title": title, "author": author, "year": year, "publisher": publisher, "ISBN": ISBN},
    )
    db.session.commit()
