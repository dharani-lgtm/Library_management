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

def add_book(title, author):
    book = {"title": title, "author": author}
    books.append(book)
    print(f"Book added: {title} by {author}")

# Test
add_book("Python Programming", "Guido van Rossum")
add_book("Clean Code", "Robert Martin")
display_books()