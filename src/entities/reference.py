class Reference:
    def __init__(self, id, title):
        self.id = id
        self.title = title


class Book(Reference):
    def __init__(self, id, title, author=None, year=None, publisher=None, ISBN=None):
        super().__init__(id, title)
        self.author = author
        self.year = year
        self.publisher = publisher
        #self.editor = editor
        self.ISBN = ISBN
        # self.volume = volume
        # self.pages = pages
        # self.month = month
        # self.note = note

    def __str__(self):
        return f"Book: {self.id}, Title: {self.title}, Author: {self.author}"

class Article(Reference):
    def __init__(self, id, title, author=None, journal=None, year=None, volume=None, DOI=None):
        super().__init__(id, title)
        self.author = author
        self.journal = journal
        self.year = year
        self.volume = volume
        self.DOI = DOI    

    def __str__(self):
        return f"Book: {self.id}, Title: {self.title}, Author: {self.author}"

class Misc(Reference):
    def __init__(self, id, title, year=None, author=None, url=None, note=None):
        super().__init__(id, title)
        self.year = year
        self.author = author
        self.url = url
        self.note = note
   
    def __str__(self):
        return f"Book: {self.id}, Title: {self.title}, Author: {self.author}"
 

class Improceedings(Reference):
    def __init__(self, id, title, author=None, year=None, booktitle=None, DOI=None, address=None, month=None, url=None, organization=None):
        super().__init__(id, title)
        self.author = author
        self.year= year
        self.booktitle = booktitle
        self.DOI = DOI
        self.address = address
        self.url = url
        self.organization = organization

    def __str__(self):
        return f"Book: {self.id}, Title: {self.title}, Author: {self.author}"
 
    # def __str__(self):
    #     is_done = "done" if self.done else "not done"
    #     return f"{self.content}, {is_done}"