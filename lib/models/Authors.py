from models.__init__ import CURSOR, CONN
from models.table import create_table
create_table()

class Author:
    def __init__(self, id, name, category=None):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        self._id = id
        self._name = name
        self._category = category

    def add_author(self):
        CURSOR.execute("SELECT id FROM  authors WHERE id = ?", (self._id,))
        if CURSOR.fetchone():
            raise ValueError(f"Author with id {self._id} already exists")
        sql = """
        INSERT INTO authors (id, name, category)  
        VALUES (?, ?, ?)  
        """
        CURSOR.execute(sql, (self._id, self._name, self._category))
        CONN.commit()
    @classmethod
    def author_list(cls):
        CURSOR.execute("""
            SELECT authors.id, authors.name,authors.category, books.title
            FROM authors
            LEFT JOIN books
            ON authors.id = books.author_id
        """)
        return CURSOR.fetchall()
    
    @classmethod
    def update_author_name(cls, author_id, new_name):
        sql = """
        UPDATE authors
        SET name = ?
        WHERE id = ?
        """
        CURSOR.execute(sql, (new_name, author_id))
        CONN.commit()
    @classmethod
    def update_author_category(cls, author_id, new_category):
        sql = """
        UPDATE authors
        SET category = ?
        WHERE id = ?
        """
        CURSOR.execute(sql, (new_category, author_id))
        CONN.commit()
    @classmethod
    def find_by_id ( cls, id):
        sql = """
                SELECT authors.name
                FROM authors
               
                WHERE authors.id = ?
        """
        CURSOR.execute(sql, (id,))
        return CURSOR.fetchone() 
    @classmethod
    def delete_author( cls,id):
        sql = """
             DELETE 
             FROM authors
             WHERE id = ?
        """
        CURSOR.execute(sql,(id,))
        CONN.commit()
