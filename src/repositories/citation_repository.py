from config import db
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy


class BibtexRepo:
    def __init__(self, database: SQLAlchemy):
        self._db = database

    def add_book_citation(self, title, author, year, publisher, editor, volume, pages, month, isbn, note):
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

    def get_all_books(self):
        sql = text("SELECT * FROM book_citation")
        result = self._db.session.execute(sql)
        return result.fetchall()
