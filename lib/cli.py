# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)
from models.Books import books
from models.table import create_table
create_table()

def main():
    # db = books()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            id = input("Book ID: ")
            title = input("Title name: ")
            author_id = input("Author ID: ")
            borrower_id = input("Borrower ID: ")
            
            Book = books(id, title, author_id, borrower_id)
            return Book.save()
            
        elif choice == "1":
            book_list = books.book_list()
            for book in book_list:
              print(f"BOOK ID: {book[0]}, Book Name: {book[1]}, Author ID: {book[2]}, Borrower ID: {book[3]}")
            
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add a new book")
    print("2. List all books")
    print("3. Find a book by title")
    print("4. Delete a book by ID")


if __name__ == "__main__":
    main()
