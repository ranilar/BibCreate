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
    pass
    

class Misc(Reference):
    pass

class Improceedings(Reference):
    pass


    def __str__(self):
        is_done = "done" if self.done else "not done"
        return f"{self.content}, {is_done}"