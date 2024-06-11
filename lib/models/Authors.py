from models.__init__ import CURSOR, CONN
from models.table import create_table
create_table()

class Author:
    def __init__(self,id, name, ) -> None:
        self._id = id
        self._name = name
       
    def save(self):
        CURSOR.execute("SELECT id FROM  authors WHERE id = ?", (self._id,))
        if CURSOR.fetchone():
            raise ValueError(f"Author with id {self._id} already exists")
        sql = """
             INSERT INTO authors (
             id, name)  
             VALUES (?, ?)  
            """
        CURSOR.execute(sql, (self._id, self._name))
        CONN.commit()  
    @classmethod
    def author_list(cls):
        CURSOR.execute("""
            SELECT * FROM authors
        """)
        return CURSOR.fetchall()
