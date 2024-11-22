class Reference:
    def __init__(self, id, ref_type, title, author, year, publisher, ISBN):
        self.id = id
        self.ref_type = ref_type
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.ISBN = ISBN


    def __str__(self):
        is_done = "done" if self.done else "not done"
        return f"{self.content}, {is_done}"