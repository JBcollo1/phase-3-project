# lib/cli.py

from helpers import (
    exit_program,
    
)
from models.Books import books
from models.Authors import Author
from models.table import create_table
create_table()

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            id = input("Book ID: ")
            title = input("Title name: ")
            author_id = input("Author ID: ")
            borrower_id = input("Borrower ID: ")
            book = books(id, title, author_id, borrower_id)
            book.save()
            print("Book added successfully.")
            
        elif choice == "2":
            book_list = books.book_list()
            for book in book_list:
                print(f"BOOK ID: {book[0]}, Book Name: {book[1]}, Author ID: {book[2]}, Borrower ID: {book[3]}")
        elif choice == "3":
            id = input("Title ID: ")
            book = books.find_by_id(id)
            if book:
                print(f"Book found: Title: {book[0]}, Author Name: {book[1]}")
            else:
                print("Book not found.")
                
        elif choice == "4":
            id = input("Book ID: ")
            book = books.find_by_id(id)
            if book:
                books.delete_book(id)
                print("Book deleted successfully.")
            else:
                print("Book not found.")

        elif choice == "5":
            id = input("Enter Author ID: ")
            name = input("Enter Author Name: ")
            author = Author(id, name)
            author.save()
            print("Author added successfully.")

        elif choice == "6":
            author_list = Author.author_list()  
            for author in author_list:
                print(f"Author ID: {author[0]}, Author Name: {author[1]}")      
                
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add a new book")
    print("2. List all books")
    print("3. Find a book by ID")
    print("4. Delete a book by ID")
    print("5. Add author")
    print("6. List all authors and their id")



if __name__ == "__main__":
    main()
