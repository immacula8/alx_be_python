class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out


    def check_out(self):
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True
    
class Library:
    def __init__(self):
        self._books = []  # private list of Book objects

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f"'{title}' has been checked out."
        return f"'{title}' is not available."

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f"'{title}' has been returned."
        return f"'{title}' was not checked out."

    def list_available_books(self):
        available = [book.title for book in self._books if book.is_available()]
        return available
