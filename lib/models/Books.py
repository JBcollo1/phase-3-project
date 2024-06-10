from models.__init__ import CURSOR, CONN
from models.table import create_table
create_table()
class books:
    def __init__(self,id, title, author_id, borrowers_id) -> None:
        self._id = id
        self._title = title
        self._author_id = author_id
        self._borrowers_id = borrowers_id
    def save(self):
        CURSOR.execute("SELECT id FROM  books WHERE id = ?", (self._id,))
        if CURSOR.fetchone():
            raise ValueError(f"Book with id {self._id} already exists")
        sql = """
             INSERT INTO books (
             id, title, author_id, borrower_id)  
             VALUES (?, ?, ?,?)  
            """
        CURSOR.execute(sql, (self._id, self._title, self._author_id, self._borrowers_id))
        CONN.commit()    
    @classmethod
    def book_list (cls):
        CURSOR.execute ( """
             SELECT * FROM books 
        """)
    
        return CURSOR.fetchall() 

    def find_by_name ( self,title):
        sql = """
                SELECT books.title, authors.name
                FROM books
                LEFT JOIN authors
                ON books.authors_id = authors.id
                WHERE books.title = ?
        """
        CURSOR.execute(sql, (self._title,))
        return CURSOR.fetchone() 
    def delete_book( self,id):
        CURSOR.execute("DELETE FROM books WHERE id = ?", int(self._id,))
        CONN.commit()

    
        
        