class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def description(self):
        return f"Libro: {self.title} by {self.author}"

    # Opcional
    def __str__(self):
        return f"Libro: {self.title} Autor: {self.author} STR"


class DigitalBook(Book):
    def __init__(self, title, author, format):
        super().__init__(title, author)
        self.format = format

    def description(self):
        return f"Libro: {self.title} Autor: {self.author}"

    def __str__(self):
        return f"Libro: {self.title} Autor: {self.author} {self.format} STR"
