# lib/cli.py

from helpers import (
    exit_program,
    
)
from models.Books import books
from models.Authors import Author
from models.Borrowers import Borrowers 
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
            category = input("Enter Author Subject Matter: ")  
            author = Author(id, name, category)
            author.add_author()
            print("Author added successfully.")

        elif choice == "6":
            author_list = Author.author_list()  
            for author in author_list:
                print(f"Author ID: {author[0]}, Author Name: {author[1]}, Author Subject Matter: {author[2]}, Authors Book: {author[3]}") 
        elif choice == "7":
            print("Please select an option:")
            print("1. Update Name ")
            print("2. update Subject Matter ")
            print("3. Delete Author details")
            print("4. Exit ")
            update = input ("Make Updates: ")
            if update == "1":
                author_id = input("Enter Author ID: ")
                new_name = input("Enter Author new name: ")
                Author.update_author_name(author_id, new_name ) 
            elif update == "2":
                author_id = input("Enter Author ID: ")
                new_subject = input("Enter Author New Subject Matter: ")
                Author.update_author_category(author_id, new_subject )
            elif update == "3":
                id = input("Author ID: ")
                author = Author.find_by_id(id)
                if author:
                    Author.delete_author(id)
                    print("Author deleted successfully.")
                else:
                    print("Author not found.")

            elif update == "4":
                exit_program()

        elif choice == "8":
            print("Please select an option")
            print("1. Add patron information ")
            print("2. List Patrons ")
            print("3. Delete Patron Details")
            print("4. Exit ")
            update = input ("Patron Details: ")
            if update == "1":
                id = input("Patron ID ID: ")
                name = input("Patron name: ")
                
                borrower = Borrowers(id, name)
                borrower.add_borrower()
                print("Patron added successfully.")
            elif update == "2":
                borrower_list = Borrowers.patron_list()
                for borrower in borrower_list:
                    print(f"Patron ID: {borrower[0]}, Patron Name: {borrower[1]}, Book taken: {borrower[2]}")
            elif update == "3":
                id = input("Patron ID: ")
                patron = Borrowers.find_by_id(id)
                if patron:
                    Borrowers.delete_patron(id)
                    print("Patron deleted successfully.")
                else:
                    print("Patron not found.")

            elif update == "4":
                exit_program()


                

                
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
    print("7. Author update section ")
    print("8. Patrons section ")



if __name__ == "__main__":
    main()
