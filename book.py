
from dataclasses import dataclass, field

@dataclass
class Book:
    """A data class to represent a book in a library system."""
    title: str
    author: str
    isbn: str
    publication_year: int
    copies_available: int
    genre: str  # My own devised attribute

    def is_available(self) -> bool:
        """Checks if the book is available."""
        return self.copies_available > 0

    def borrow_book(self):
        """Borrows a book."""
        if self.is_available():
            self.copies_available -= 1
        else:
            raise ValueError("No copies available to borrow.")

    def return_book(self):
        """Returns a book."""
        self.copies_available += 1

