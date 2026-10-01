import sqlite3

class Database:
    def __init__(self, db_path="tasks.db"):
        self.db_path = db_path
        self.init_db()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def init_db(self):
        with self.get_connection() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
                )
            ''')
            conn.commit()

    def add_task(self, title, description):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tasks (title, description, completed) VALUES (?, ?, 0)", (title, description))
            conn.commit()

    def get_all_tasks(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks")
            return cursor.fetchall()

    def get_task(self, task_id):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
            return cursor.fetchone()

    def update_task(self, task_id, title, description, completed):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE tasks SET title = ?, description = ?, completed = ? WHERE id = ?",
                (title, description, 1 if completed else 0, task_id)
            )
            return cursor.rowcount > 0

    def delete_task(self, task_id):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            return cursor.rowcount > 0