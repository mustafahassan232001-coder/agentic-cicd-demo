import sqlite3

class Database:
    def __init__(self, db_name='tasks.db'):
        self.db_name = db_name
        self._create_table()

    def get_connection(self):
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        return conn

    def _create_table(self):
        with self.get_connection() as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS tasks 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             title TEXT NOT NULL, 
                             description TEXT, 
                             completed BOOLEAN DEFAULT 0)''')
            conn.commit()