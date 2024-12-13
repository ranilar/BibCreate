from sqlalchemy import text
from config import db, app

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
        "reference_type TEXT NOT NULL CHECK (reference_type IN ('book', 'article', 'misc', 'inproceeding')), "
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

    setup_tables()

    db.session.commit()
    print("All tables have been created successfully.")


def create_examples():
    print("Creating example entries for demonstration...")

    book_references = [
        ("The Lady Tasting Tea: How Statistics Revolutionized Science in the Twentieth Century",
         "ADavid Salsburg", 2002, "Holt Paperbacks", "9780805071344"),
        ("Clean Code", "Robert C. Martin", 2009, "Prentice Hall", "9780132350884"),
        ("Introduction to Algorithms", "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein",
         2022, "The MIT Press", "9780262046305")
    ]
    article_references = [
        ("Deep Learning", "Yann LeCun, Yoshua Bengio, Geoffrey Hinton",
         "Nature", 2015, 521, "10.1038/nature14539"),
        ("Attention Is All You Need",
         "Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin",
         "NeurIPS", 2017, 30, "10.48550/arXiv.1706.03762"),
        ("Generative Adversarial Networks",
         "Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, Yoshua Bengio",
         "Communications of the ACM", 2020, 63, "10.1145/3422622"),
        ("BERT: Pre-training of Deep Bidirectional Transformers",
         "Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova", "ACL", 2019, 1, "10.18653/v1/N19-1423"),
        ("ImageNet Classification with Deep Convolutional Neural Networks",
         "Alex Krizhevsky, Ilya Sutskever, G. E. Hinton", "NeurIPS", 2017, 60, "10.1145/3065386")
    ]
    misc_references = [
        ("Python Documentation", "Python Software Foundation",
         2023, "https://docs.python.org/3/", "Check this"),
        ("GitHub Actions Guide", None, 2023,
         "https://docs.github.com/en/actions", "Tips for workflow")
    ]
    inproceeding_references = [
        ("Loppudemo", "Aappo Alatalo, Iida Häkkinen, Dodo Lökström, Sandra Ole, Ilmari Ranin", 2024,
         "Idias solutions", "", "Kumpulan kampus", "December", "http://127.0.0.1:5001/", "Helsingin yliopisto")
    ]

    for title, author, year, publisher, isbn in book_references:
        db.session.execute(text(
            "INSERT INTO book_references "
            "(title, author, year, publisher, ISBN) "
            "VALUES (:title, :author, :year, :publisher, :isbn)"
        ), {"title": title, "author": author, "year": year, "publisher": publisher, "isbn": isbn})

    for title, author,  journal, year, volume, doi in article_references:
        db.session.execute(text(
            "INSERT INTO article_references "
            "(title, author, journal, year, volume, DOI) "
            "VALUES (:title, :author, :journal, :year, :volume, :doi)"
        ), {"title": title, "author": author, "journal": journal, "year": year, "volume": volume, "doi": doi})

    for title, author, year, url, note in misc_references:
        db.session.execute(text(
            "INSERT INTO misc_references "
            "(title, author, year, url, note) "
            "VALUES (:title, :author, :year, :url, :note)"
        ), {"title": title, "author": author, "year": year, "url": url, "note": note})

    for title, author, year, booktitle, doi, address, month, url, organization in inproceeding_references:
        db.session.execute(text(
            "INSERT INTO inproceeding_references "
            "(title, author, year, booktitle, DOI, address, month, url, organization) "
            "VALUES (:title, :author, :year, :booktitle, :doi, :address, :month, :url, :organization)"
        ), {"title": title, "author": author, "year": year, "booktitle": booktitle,
            "doi": doi, "address": address, "month": month, "url": url, "organization": organization})

    db.session.commit()
    print("Example entries created successfully.")


if __name__ == "__main__":
    with app.app_context():
        setup_tables()
        create_examples()
