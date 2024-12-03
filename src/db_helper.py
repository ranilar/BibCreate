from config import db, app
from sqlalchemy import text

# Define your table names and their schemas
tables = {
    "book_references": (
        "id SERIAL PRIMARY KEY, "
        "title TEXT NOT NULL, "
        "author TEXT NOT NULL, "
        "year INTEGER NOT NULL, "
        "publisher TEXT NOT NULL, "
        "ISBN TEXT"
    ),
    "article_references": (
        "id SERIAL PRIMARY KEY, "
        "title TEXT NOT NULL, "
        "author TEXT NOT NULL, "
        "journal TEXT NOT NULL, "
        "year INTEGER NOT NULL, "
        "volume INTEGER, "
        "DOI TEXT "
    ),
    "misc_references": (
        "id SERIAL PRIMARY KEY, "
        "title TEXT NOT NULL, "
        "author TEXT, "
        "year INTEGER, "
        "url TEXT, "
        "note TEXT "
    ),
    "inproceeding_references": (
        "id SERIAL PRIMARY KEY, "
        "title TEXT NOT NULL, "
        "author TEXT NOT NULL, "
        "year INTEGER NOT NULL, "
        "booktitle TEXT NOT NULL, "
        "DOI TEXT, "
        "address TEXT, "
        "month TEXT, "
        "url TEXT, "
        "organization TEXT "
    ),
    "tags": (
        "id SERIAL PRIMARY KEY, "
        "name TEXT NOT NULL UNIQUE"
    ),
    "tags_references": (
        "id SERIAL PRIMARY KEY, "
        "tag_id INT NOT NULL, "
        "reference_id INT NOT NULL, "
        "reference_type TEXT NOT NULL CHECK (reference_type IN ('book', 'article', 'misc', 'inproceedings')), "
        "FOREIGN KEY (tag_id) REFERENCES tags (id) ON DELETE CASCADE, "
        "UNIQUE (tag_id, reference_id, reference_type)"
    )
}


def table_exists(name):
    """Check if a table exists in the database."""
    sql_table_existence = text(
        "SELECT EXISTS ("
        "  SELECT 1"
        "  FROM information_schema.tables"
        f" WHERE table_name = '{name}'"
        ")"
    )
    result = db.session.execute(sql_table_existence)
    return result.fetchone()[0]


def setup_tables():
    """Create multiple tables defined in the `tables` dictionary."""
    for table_name, schema in tables.items():
        if table_exists(table_name):
            print(f"Table {table_name} exists, dropping it.")
            sql = text(f"DROP TABLE {table_name} CASCADE")
            db.session.execute(sql)

        print(f"Creating table {table_name}")
        sql = text(f"CREATE TABLE {table_name} ({schema})")
        db.session.execute(sql)

    db.session.commit()
    print("All tables have been created successfully.")

# Reset all tables


def reset_db():
    for table_name in tables.keys():
        print(f"Clearing contents from table {table_name}")
        sql = text(f"DELETE FROM {table_name} CASCADE")
        db.session.execute(sql)
        # db.session.commit()

    setup_tables()

    # db.session.execute(sql)
    db.session.commit()
    print("All tables have been created successfully.")


if __name__ == "__main__":
    with app.app_context():
        setup_tables()
