# from models.__init__ import CURSOR, CONN
# from models.table import create_table
# create_table()

# class Borrowers:
#     def __init__(self):
#         self._id = None
#         self._name = None

#     def set_id(self, id):
#         if not isinstance(id, int):
#             raise ValueError("ID must be an integer")
#         self._id = id

#     def set_name(self, name):
#         if not name or not isinstance(name, str):
#             raise ValueError("Name must be a non-empty string")
#         self._name = name

#     def save(self):
#         if self._id is None or self._name is None:
#             raise ValueError("ID and Name must be set before saving")
        
#         CURSOR.execute("SELECT id FROM borrowers WHERE id = ?", (self._id,))
#         if CURSOR.fetchone():
#             raise ValueError(f"Borrower with id {self._id} already exists")
        
#         sql = """
#         INSERT INTO borrowers (id, name)  
#         VALUES (?, ?)  
#         """
#         CURSOR.execute(sql, (self._id, self._name))
#         CONN.commit()

#     def articles(self):
#         sql = """
#             SELECT books.title
#             FROM articles
#             LEFT JOIN authors
#             ON books.author_id = authors.id
#             WHERE authors.id = ?
#         """
#         CURSOR.execute(sql, (self._id,))
#         articles = CURSOR.fetchall()
#         return [article[0] for article in articles] if articles else None
