class Library:
    # Class attributes
    total_books = 0  # Stores total number of books in the library
    all_books = []   # List of all books available in the library

    def __init__(self, name):
        """Initialize a library member with a name and an empty list of borrowed books."""
        self.name = name
        self.borrowed_books = []  # List to store books borrowed by the member

    def borrow_book(self, book):
        """Allows a member to borrow a book if available."""
        if book in Library.all_books:
            self.borrowed_books.append(book)  # Add book to member's borrowed list
            Library.all_books.remove(book)    # Remove book from library's available list
            Library.total_books -= 1          # Decrease total book count
            print(f"{self.name} borrowed '{book}'")
        else:
            print("Book not available.")  # Book is not available in the library

    def return_book(self, book):
        """Allows a member to return a borrowed book to the library."""
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)  # Remove book from member's borrowed list
            Library.all_books.append(book)    # Add book back to library's list
            Library.total_books += 1          # Increase total book count
            print(f"{self.name} returned '{book}'")
        else:
            print(f"{self.name} does not have '{book}' to return.")

    @classmethod
    def view_library_books(cls):
        """Displays the total number of books and lists all available books in the library."""
        print(f"Total books in library: {cls.total_books}")
        print("Available books:", cls.all_books)


# Example Usage
# Adding books to the library
Library.all_books = ["Harry Potter", "The Hobbit", "1984", "To Kill a Mockingbird"]
Library.total_books = len(Library.all_books)

# Viewing available books before borrowing
Library.view_library_books()

# Creating members
member1 = Library("Alice")
member2 = Library("Bob")

# Borrowing books
member1.borrow_book("Harry Potter")
member2.borrow_book("The Hobbit")

# Viewing available books after borrowing
Library.view_library_books()

# Returning books
member1.return_book("Harry Potter")
member2.return_book("The Hobbit")

# Viewing available books after returning
Library.view_library_books()

'''
Output:
Total books in library: 4
Available books: ['Harry Potter', 'The Hobbit', '1984', 'To Kill a Mockingbird']

Alice borrowed 'Harry Potter'
Bob borrowed 'The Hobbit'

Total books in library: 2
Available books: ['1984', 'To Kill a Mockingbird']

Alice returned 'Harry Potter'
Bob returned 'The Hobbit'

Total books in library: 4
Available books: ['1984', 'To Kill a Mockingbird', 'Harry Potter', 'The Hobbit']
'''
