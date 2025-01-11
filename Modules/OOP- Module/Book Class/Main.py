class Book:
    def __init__(self, title, author, available=True):
        """Initialize a book with title, author, and availability status."""
        self.title = title
        self.author = author
        self.available = available

    def check_out(self):
        """Mark the book as checked out if it's available."""
        if self.available:
            self.available = False
            print(f"'{self.title}' by {self.author} has been checked out.")
        else:
            print(f"Sorry, '{self.title}' is currently unavailable.")

    def return_book(self):
        """Mark the book as available."""
        if not self.available:
            self.available = True
            print(f"'{self.title}' by {self.author} has been returned and is now available.")
        else:
            print(f"'{self.title}' is already available.")

    def display_info(self):
        """Display book details."""
        status = "Available" if self.available else "Checked Out"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")


class Library:
    def __init__(self):
        """Initialize the library with an empty catalog."""
        self.catalog = []

    def add_book(self, title, author):
        """Add a new book to the catalog."""
        new_book = Book(title, author)
        self.catalog.append(new_book)
        print(f"'{title}' by {author} has been added to the catalog.")

    def view_catalog(self):
        """Display the catalog of books."""
        if not self.catalog:
            print("The catalog is empty.")
        else:
            print("Library Catalog:")
            for book in self.catalog:
                book.display_info()


# Simple Scenario Interaction
def main():
    library = Library()

    # Adding books to the library catalog
    library.add_book("1984", "George Orwell")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")

    print("\nInitial Catalog:")
    library.view_catalog()

    # Checking out a book
    print("\nChecking out '1984':")
    library.catalog[0].check_out()

    # Trying to check out the same book again
    print("\nTrying to check out '1984' again:")
    library.catalog[0].check_out()

    # Returning a book
    print("\nReturning '1984':")
    library.catalog[0].return_book()

    # Viewing the updated catalog
    print("\nUpdated Catalog:")
    library.view_catalog()


if __name__ == "__main__":
    main()
