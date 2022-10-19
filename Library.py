from model.book import Book

class Library:
    __main = None

    def main(__main):
        if __main == None:
            __main = Library()
        return __main

    def __init__(self):
        self.__book_list =[]

    @property
    def count (self):
        return len(self.__book_list)

    def add(self, book:Book):
        assert isinstance (book, Book), "Объект должен быть Book"
        self.__book_list.extend(book)
