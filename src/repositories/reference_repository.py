from sqlalchemy import text
from config import db
from entities.reference import Book, Article, Misc, Inproceeding


def get_references_by_type(ref_type):
    sql = text(f"SELECT * FROM {ref_type}_references")
    result = db.session.execute(sql)
    references = result.fetchall()

    if ref_type == "book":
        return [Book(*reference) for reference in references]
    if ref_type == "article":
        return [Article(*reference) for reference in references]
    if ref_type == "misc":
        return [Misc(*reference) for reference in references]
    if ref_type == "inproceeding":
        return [Inproceeding(*reference) for reference in references]
    return []


def search_references_by_type_and_tag(ref_type, query):
    table_map = {
        "book": "book_references",
        "article": "article_references",
        "misc": "misc_references",
        "inproceeding": "inproceeding_references"
    }

    table_name = table_map.get(ref_type)
    if not table_name:
        raise ValueError(f"Invalid reference type: {ref_type}")

    sql = text(f"""
        SELECT B.*
        FROM {table_name} B
        LEFT JOIN tags_references TR ON TR.reference_id = B.id AND TR.reference_type = '{ref_type}'
        LEFT JOIN tags T ON T.id = TR.tag_id
        WHERE B.title ILIKE :query OR B.author ILIKE :query OR CAST(B.year AS TEXT) ILIKE :query OR T.name ILIKE :query
    """)
    result = db.session.execute(
        sql,
        {
            "query": "%"+query+"%"
        },
    )
    references = result.fetchall()
    print(references)

    if ref_type == "book":
        return [Book(*reference) for reference in references]
    if ref_type == "article":
        return [Article(*reference) for reference in references]
    if ref_type == "misc":
        return [Misc(*reference) for reference in references]
    if ref_type == "inproceeding":
        return [Inproceeding(*reference) for reference in references]

    return []


def get_all_references():
    books = get_references_by_type("book")
    articles = get_references_by_type("article")
    miscs = get_references_by_type("misc")
    inproceedingit = get_references_by_type("inproceeding")

    all_references = []
    for book in books:
        all_references.append({
            'type': 'book',
            'reference': book
        })

    for article in articles:
        all_references.append({
            'type': 'article',
            'reference': article
        })

    for misc in miscs:
        all_references.append({
            'type': 'misc',
            'reference': misc
        })

    for inproceeding in inproceedingit:
        all_references.append({
            'type': 'inproceeding',
            'reference': inproceeding
        })

    return all_references


def search_all_references(query):
    books = search_references_by_type_and_tag("book", query)
    articles = search_references_by_type_and_tag("article", query)
    miscs = search_references_by_type_and_tag("misc", query)
    inproceedingit = search_references_by_type_and_tag("inproceeding", query)

    all_references = []
    for book in books:
        all_references.append({
            'type': 'book',
            'reference': book
        })

    for article in articles:
        all_references.append({
            'type': 'article',
            'reference': article
        })

    for misc in miscs:
        all_references.append({
            'type': 'misc',
            'reference': misc
        })

    for inproceeding in inproceedingit:
        all_references.append({
            'type': 'inproceeding',
            'reference': inproceeding
        })

    return all_references


def create_book(title, author, year, publisher, ISBN):
    sql = text(
        """
        INSERT INTO book_references (title, author, year, publisher, ISBN)
        VALUES (:title, :author, :year, :publisher, :ISBN)
        RETURNING id
    """
    )
    result = db.session.execute(
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
    return result.fetchone()[0]


def create_article(title, author, journal, year, volume, DOI):
    sql = text(
        """
        INSERT INTO article_references (title, author, journal, year, volume, DOI)
        VALUES (:title, :author, :journal, :year, :volume, :DOI)
        RETURNING id
        """
    )
    result = db.session.execute(
        sql,
        {
            "title": title,
            "author": author,
            "journal": journal,
            "year": year,
            "volume": int(volume) if volume and volume.isdigit() else None,
            "DOI": DOI,
        },
    )
    db.session.commit()
    return result.fetchone()[0]


def create_misc(title, author, year, url, note):
    sql = text(
        """
        INSERT INTO misc_references (title, author, year, url, note)
        VALUES (:title, :author, :year, :url, :note)
        RETURNING id
        """
    )
    result = db.session.execute(
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
    return result.fetchone()[0]


def create_inproceeding(title, author, year, booktitle, DOI, address, month, url, organization):
    sql = text(
        """
        INSERT INTO inproceeding_references (title, author, year, booktitle, DOI, address, month, url, organization)
        VALUES (:title, :author, :year, :booktitle, :DOI, :address, :month, :url, :organization)
        RETURNING id
        """
    )
    result = db.session.execute(
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
    return result.fetchone()[0]


def get_reference(ref_type, ref_id):
    if ref_type == "book":
        sql = text("SELECT * FROM book_references WHERE id = :id")
        result = db.session.execute(sql, {"id": ref_id})
        reference = result.fetchall()
        return Book(*reference[0])

    if ref_type == "article":
        sql = text("SELECT * FROM article_references WHERE id = :id")
        result = db.session.execute(sql, {"id": ref_id})
        reference = result.fetchall()
        return Article(*reference[0])

    if ref_type == "misc":
        sql = text("SELECT * FROM misc_references WHERE id = :id")
        result = db.session.execute(sql, {"id": ref_id})
        reference = result.fetchall()
        return Misc(*reference[0])

    if ref_type == "inproceeding":
        sql = text("SELECT * FROM inproceeding_references WHERE id = :id")
        result = db.session.execute(sql, {"id": ref_id})
        reference = result.fetchall()
        return Inproceeding(*reference[0])

    return None


def delete_reference_by_type(ref_type, ref_id):
    sql = text("""
        DELETE FROM tags_references
        WHERE reference_id = :reference_id AND reference_type = :reference_type
    """)
    db.session.execute(sql, {"reference_id": ref_id,
                       "reference_type": ref_type})

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

    elif ref_type == "inproceeding":
        sql = text("DELETE FROM inproceeding_references WHERE id = :id")
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
                "volume": int(reference.volume) if reference.volume and reference.volume.isdigit() else None,
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

    elif ref_type == "inproceeding":
        sql = text("""
            UPDATE inproceeding_references
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


def create_or_get_tag(tag_name):
    sql = text("""
        INSERT INTO tags (name) VALUES (:name)
        ON CONFLICT (name) DO NOTHING
        RETURNING id
    """)
    result = db.session.execute(sql, {"name": tag_name})
    tag_id = result.fetchone()

    if tag_id:
        return tag_id[0]

    # Jos tagia ei luotu, haetaan sen ID
    sql = text("SELECT id FROM tags WHERE name = :name")
    result = db.session.execute(sql, {"name": tag_name})
    tag_id = result.fetchone()[0]
    db.session.commit()
    return tag_id


def link_tag_to_reference(tag_id, ref_id, ref_type):
    sql = text("""
        INSERT INTO tags_references (tag_id, reference_id, reference_type)
        VALUES (:tag_id, :reference_id, :reference_type)
        ON CONFLICT DO NOTHING
    """)
    db.session.execute(sql, {
        "tag_id": tag_id,
        "reference_id": ref_id,
        "reference_type": ref_type
    })
    db.session.commit()


def get_tags_for_reference(ref_id, ref_type):
    tags_sql = text("""
        SELECT t.id, t.name 
        FROM tags t
        JOIN tags_references tr 
        ON t.id = tr.tag_id
        WHERE tr.reference_id = :ref_id AND tr.reference_type = :ref_type
    """)
    tags_result = db.session.execute(
        tags_sql, {"ref_id": ref_id, "ref_type": ref_type}).mappings()
    return [{"id": row.id, "name": row.name} for row in tags_result]


def delete_orphan_tags(tag_id):
    orphan_check_sql = text("""
        SELECT COUNT(*) FROM tags_references WHERE tag_id = :tag_id
    """)
    orphan_count = db.session.execute(
        orphan_check_sql, {"tag_id": tag_id}).scalar()

    if orphan_count == 0:
        db.session.execute(text("DELETE FROM tags WHERE id = :tag_id"), {
                           "tag_id": tag_id})
        db.session.commit()
