class Reference:
    def __init__(self, id, title, ref_type):
        self.id = id
        self.title = title
        self.ref_type = ref_type


class Book(Reference):
    def __init__(self, id, title, author=None, year=None, publisher=None, ISBN=None):
        super().__init__(id, title, "book")
        self.author = author
        self.year = year
        self.publisher = publisher
        # self.editor = editor
        self.ISBN = ISBN
        # self.volume = volume
        # self.pages = pages
        # self.month = month
        # self.note = note

    def __str__(self):
        return f"Book: {self.id}, Title: {self.title}, Author: {self.author}"


class Article(Reference):
    def __init__(self, id, title, author=None, journal=None, year=None, volume=None, DOI=None):
        super().__init__(id, title, "article")
        self.author = author
        self.journal = journal
        self.year = year
        self.volume = volume
        self.DOI = DOI

    def __str__(self):
        return f"Article: {self.id}, Title: {self.title}, Author: {self.author}"


class Misc(Reference):
    def __init__(self, id, title, year=None, author=None, url=None, note=None):
        super().__init__(id, title, "misc")
        self.year = year
        self.author = author
        self.url = url
        self.note = note

    def __str__(self):
        return f"BMisc: {self.id}, Title: {self.title}, Author: {self.author}"


class Inproceedings(Reference):
    def __init__(self, id, title, author=None, year=None, booktitle=None, DOI=None, address=None, month=None, url=None, organization=None):
        super().__init__(id, title, "inproceedings")
        self.author = author
        self.year = year
        self.booktitle = booktitle
        self.DOI = DOI
        self.address = address
        self.month = month
        self.url = url
        self.organization = organization

    def __str__(self):
        return f"Inproceedings: {self.id}, Title: {self.title}, Author: {self.author}"
