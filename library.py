# Library Management System
books = []

def display_books():
    if len(books) == 0:
        print("No books available!")
    else:
        print("\nAvailable Books:")
        for i, book in enumerate(books, start=1):
            print(f"{i}. {book}")

# Test
display_books()
def remove_book(title):
    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            print(f"Book removed: {title}")
            return
    print(f"Book not found: {title}")

# Test
add_book("Python Programming", "Guido van Rossum")
remove_book("Python Programming")
display_books()