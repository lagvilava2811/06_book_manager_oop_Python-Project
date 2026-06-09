from abc import ABC, abstractmethod
from datetime import date


class LibraryItem(ABC):

    @abstractmethod
    def display_info(self):
        pass

class Book(LibraryItem):

    MIN_YEAR = 1

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be text.")
        value = value.strip()
        if not value:
            raise ValueError("Title cannot be empty.")
        self.__title = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise ValueError("Author must be text.")
        value = value.strip()
        if not value:
            raise ValueError("Author cannot be empty.")
        self.__author = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = self.validate_year(value)

    @classmethod
    def validate_year(cls, value):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError("Publication year must be an integer.")

        current_year = date.today().year
        if value < cls.MIN_YEAR or value > current_year:
            raise ValueError(f"Publication year must be between {cls.MIN_YEAR} and {current_year}.")

        return value

    def to_dict(self):
        return {"title": self.title, "author": self.author, "year": self.year}

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], int(data["year"]))

    def display_info(self):
        return f"{self.title} - {self.author} ({self.year})"

    def __str__(self):
        return self.display_info()


class BookManager:

    def __init__(self, books=None):
        self.__books = []
        for book in books or []:
            self.add_book(book)

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book objects can be added.")
        self.__books.append(book)

    def get_all_books(self):
        return self.__books.copy()

    def search_by_title(self, title):
        if not isinstance(title, str):
            raise ValueError("Search title must be text.")

        title = title.strip().lower()
        if not title:
            raise ValueError("Search title cannot be empty.")

        return [book for book in self.__books if title in book.title.lower()]
