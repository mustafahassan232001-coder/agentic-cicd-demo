from database import Database

class TaskManager:
    def __init__(self, db_name='tasks.db'):
        self.db = Database(db_name)

    def create_task(self, title, description):
        if not title or not isinstance(title, str): return {'error': 'Invalid title'}
        with self.db.get_connection() as conn:
            cursor = conn.execute('INSERT INTO tasks (title, description) VALUES (?, ?)', (title, description))
            conn.commit()
            return {'id': cursor.lastrowid, 'title': title, 'description': description, 'completed': 0}

    def get_all_tasks(self):
        with self.db.get_connection() as conn:
            return [dict(row) for row in conn.execute('SELECT * FROM tasks').fetchall()]

    def update_task(self, task_id, title, description, completed):
        with self.db.get_connection() as conn:
            task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
            if not task: return {'error': 'Task not found'}
            conn.execute('UPDATE tasks SET title=?, description=?, completed=? WHERE id=?', 
                         (title, description, 1 if completed else 0, task_id))
            conn.commit()
            return {'success': True}

    def delete_task(self, task_id):
        with self.db.get_connection() as conn:
            conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
            conn.commit()
            return {'success': True}