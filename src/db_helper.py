# Tiedostossa SQL injektio mahdollisuuksia

from config import db, app
from sqlalchemy import text

table_name = "book_citation"

def table_exists(name):
    sql_table_existence = text(
        "SELECT EXISTS ("
        "  SELECT 1"
        "  FROM information_schema.tables"
        f" WHERE table_name = '{name}'"
        ")"
    )

    print(f"Checking if table {name} exists")
    result = db.session.execute(sql_table_existence)
    return result.fetchall()[0][0]

def reset_db():
    print(f"Clearing contents from table {table_name}")
    sql = text(f"DELETE FROM {table_name}")
    db.session.execute(sql)
    db.session.commit()

def setup_db():
    if table_exists(table_name):
        print(f"Table {table_name} exists, dropping it")
        sql = text(f"DROP TABLE {table_name}")
        db.session.execute(sql)
        db.session.commit()

    print(f"Creating table {table_name}")
    sql = text(
        f"""
        CREATE TABLE "{table_name}" (
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL,
            publisher TEXT NOT NULL,
            editor TEXT,
            volume INTEGER,
            pages TEXT,
            month INTEGER,
            isbn TEXT,
            note TEXT
        )
        """
    )

    db.session.execute(sql)
    db.session.commit()

if __name__ == "__main__":
    app = create_app()
    setup_db(app, db)
