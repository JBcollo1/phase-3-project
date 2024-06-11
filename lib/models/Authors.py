from models.__init__ import CURSOR, CONN
from models.table import create_table
create_table()

class Author:
    def __init__(self):
        self._id = None
        self._name = None

    def set_id(self, id):
        if not isinstance(id, int):
            raise ValueError("ID must be an integer")
        self._id = id

    def set_name(self, name):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        self._name = name

    def add_author(self, id, name):
        if self._id is None or self._name is None:
            raise ValueError("ID and Name must be set before saving")
        
        CURSOR.execute("SELECT id FROM authors WHERE id = ?", (id,))
        if CURSOR.fetchone():
            raise ValueError(f"Author with id {id} already exists")
        
        sql = """
        INSERT INTO authors (id, name)  
        VALUES (?, ?)  
        """
        CURSOR.execute(sql, (id, name))
        CONN.commit()

    @classmethod
    def author_list (cls):
        CURSOR.execute ( """
             SELECT * FROM authors 
        """)
        
