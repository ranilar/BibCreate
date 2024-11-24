from config import db
from sqlalchemy import text
from entities.reference import Book, Article, Misc, Improceedings

def get_references_bytype(ref_type):
    sql = text(f"SELECT * FROM {ref_type}_references")
    result = db.session.execute(sql)
    references = result.fetchall()

    if ref_type == "book":
        return [
            Book(
                reference[0], reference[1], reference[2], reference[3], reference[4]
            )
            for reference in references
    ]

    elif ref_type == "article":
        #todo
        pass
    elif ref_type == "misc":
        #todo
        pass
    elif ref_type == "improceedings":
        #todo
        pass

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

def manage_bookreference(id):
    #todo
    pass

def delete_citation(id):
    #todo
    pass
        
