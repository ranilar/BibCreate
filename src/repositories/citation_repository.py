from db import db
from sqlalchemy import text


def add_book_citation(title, author, year, publisher, editor, volume, pages, month, isbn, note):
    sql = text("""
        INSERT INTO book_citation (title, author, year, publisher, editor, volume, pages, month, isbn, note) 
        VALUES (:title, :author, :year, :publisher, :editor, :volume, :pages, :month, :isbn, :note)
    """)
    db.session.execute(sql, {
        "title": title,
        "author": author,
        "year": year,
        "publisher": publisher,
        "editor": editor,
        "volume": volume,
        "pages": pages,
        "month": month,
        "isbn": isbn,
        "note": note
    })
    db.session.commit()

