
from book import Book

# Create a new book
book = Book("The Lord of the Rings", "J.R.R. Tolkien", "978-0-618-64015-7", 1954, 5, "Fantasy")

# Print book details
print(book)

# Check if the book is available
print(f"Is book available? {book.is_available()}")

# Borrow the book
book.borrow_book()
print(f"Copies available after borrowing: {book.copies_available}")

# Return the book
book.return_book()
print(f"Copies available after returning: {book.copies_available}")

# Borrow all copies
for _ in range(5):
    book.borrow_book()

print(f"Copies available after borrowing all: {book.copies_available}")

# Try to borrow one more
try:
    book.borrow_book()
except ValueError as e:
    print(f"Error: {e}")

