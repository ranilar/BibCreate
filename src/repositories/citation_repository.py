from db import db
from sqlalchemy import text

def add_book_citation(title, author, year, publisher, editor, volume, pages, month, note):
    sql = text("""
        INSERT INTO book_citation (title, author, year, publisher, editor, volume, pages, month, note) 
        VALUES (:title, :author, :year, :publisher, :editor, :volume, :pages, :month, :note)
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
        "note": note
    })
    db.session.commit()
