from models.__init__ import CURSOR, CONN
from models.table import create_table
create_table()
class Borrowers:
    def __init__(self, id, name):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        self._id = id
        self._name = name
       

    def add_borrower(self):
        CURSOR.execute("SELECT id FROM  borrowers WHERE id = ?", (self._id,))
        if CURSOR.fetchone():
            raise ValueError(f"Patron with id {self._id} already exists")
        sql = """
        INSERT INTO borrowers (id, name)  
        VALUES (?, ?)  
        """
        CURSOR.execute(sql, (self._id, self._name))
        CONN.commit()
    @classmethod
    def patron_list(cls):
        CURSOR.execute("""
            SELECT borrowers.id, borrowers.name, books.title
            FROM borrowers
            LEFT JOIN books
            ON borrowers.id = books.author_id
        """)
        return CURSOR.fetchall()
      
    @classmethod
    def find_by_id ( cls, id):
        sql = """
                SELECT *
                FROM borrowers
               
                WHERE books.id = ?
        """
        CURSOR.execute(sql, (id,))
        return CURSOR.fetchone() 
    @classmethod
    def delete_patron( cls,id):
        sql = """
             DELETE *
             FROM borrowers
             WHERE id = ?
        """
        CURSOR.execute(sql,(id,))
        CONN.commit()
