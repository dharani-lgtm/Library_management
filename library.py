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
def display_books():
    if len(books) == 0:
        print("No books available!")
    else:
        print("\n=============================")
        print("        Available Books       ")
        print("=============================")
        for i, book in enumerate(books, start=1):
            print(f"{i}. {book['title']} - {book['author']}")
        print("=============================")
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

def add_book(title, author):
    book = {"title": title, "author": author}
    books.append(book)
    print(f"Book added: {title} by {author}")

# Test
add_book("Python Programming", "Guido van Rossum")
add_book("Clean Code", "Robert Martin")
display_books()
display_books()

def search_book(title):
    for book in books:
        if book["title"].lower() == title.lower():
            print(f"Book found: {book['title']} by {book['author']}")
            return
    print(f"Book not found: {title}")

# Test
add_book("Python Programming", "Guido van Rossum")
search_book("Python Programming")
search_book("Java Programming")
