from models.__init__ import CONN, CURSOR

def create_table():
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS borrowers (
            id INTEGER PRIMARY KEY ,
            name TEXT NOT NULL
        )
    ''')
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY ,
            name TEXT NOT NULL
            cartegory TEXT
                   
        )
    ''')
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY ,
            title TEXT NOT NULL,
            author_id INTEGER,
            borrower_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors(id),
            FOREIGN KEY (borrower_id) REFERENCES borrowers(id)
        )
    ''')

    CONN.commit()


