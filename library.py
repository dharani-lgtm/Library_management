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

# Test
add_book("Python Programming", "Guido van Rossum")
add_book("Clean Code", "Robert Martin")
display_books()