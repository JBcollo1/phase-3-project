# Library Management System
## By Jorbat Kamau



## Introduction

Welcome to the Library Management System project! This application provides a command-line interface (CLI) for managing books, authors, and borrowers in a library. The system allows you to add, list, find, update, and delete records for books, authors, and borrowers. Below is a detailed description of the project files and their functionalities.



## CLI Script
### cli.py
The cli.py file is the main entry point of the application. It provides a user-friendly interface for interacting with the library management system. The script includes a menu with various options to manage books, authors, and borrowers.

Key functionalities:

Add a new book: Prompts the user for book details and adds the book to the database.
List all books: Displays all books in the library along with their authors and borrowers.
Find a book by ID: Searches for a book by its ID and displays its details.
Delete a book by ID: Deletes a book from the library using its ID.
Add an author: Prompts the user for author details and adds the author to the database.
List all authors and their books: Displays all authors along with their books.
Author management: Allows updating or deleting author details.
Borrower management: Allows adding, listing, and deleting borrowers.



## Book Model
### books.py


The books.py file defines the Book class, which represents a book in the library. The class includes methods to save a book, list all books, find a book by ID, and delete a book.

Constructor: Initializes a book with an ID, title, author ID, and optional borrower ID.
save(): Saves a new book to the database.
book_list(): Returns a list of all books with their details.
find_by_id(id): Finds a book by its ID and returns its details.
delete_book(id): Deletes a book by its ID.



## Author Model
### author.py

The author.py file defines the Author class, which represents an author in the library. The class includes methods to add an author, list all authors, update author details, find an author by ID, and delete an author.

Constructor: Initializes an author with an ID, name, and optional category.
add_author(): Adds a new author to the database.
author_list(): Returns a list of all authors along with their books.
update_author_name(author_id, new_name): Updates the name of an author.
update_author_category(author_id, new_category): Updates the category of an author.
find_by_id(id): Finds an author by their ID and returns their name.
delete_author(id): Deletes an author by their ID

## Borrower Model
### borrowers.py

The borrowers.py file defines the Borrower class, which represents a borrower in the library. The class includes methods to add a borrower, list all borrowers, find a borrower by ID, and delete a borrower.

Constructor: Initializes a borrower with an ID and name.
add_borrower(): Adds a new borrower to the database.
borrower_list(): Returns a list of all borrowers along with the books they have borrowed.
find_by_id(id): Finds a borrower by their ID and returns their name.
delete_borrower(id): Deletes a borrower by their ID.

# installation
1. Clone the repository using
```bash
 git@github.com:JBcollo1/phase-3-project.git
```
2. The repository, if downloaded as a .zip file will need to be extracted to your preferred location.

3. Navigate to the project folder on your bash terminal.

4. Run the application 
4. Install dependancies using

    ```bash
      pipenv install
    ```

5. Run the application using

    ```bash
      python3 cli.py
    ```
## Technologies Used
python

## License
Copyright &copy; 2024 Jorbat Kamau 
@@ -44,4 +61,4 @@ Permission is hereby granted, free of charge, to any person obtaining a copy of

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY O
