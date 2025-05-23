import pandas as pd


class library:

    def __init__(self, books):
        self.books = books

    def check_book(self, book):
        if book in self.books:
            return
        else:
            return False

    def author_check(self, author):
        if author in self.books:
            return True
        else:
            return False


def test_library(library):
    book_title = "Steve Jobs"
    print()
