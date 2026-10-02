from .database import get_db

class TaskModel:
    @staticmethod
    def create(title, description, completed=False):
        conn = get_db()
        cursor = conn.execute(
            'INSERT INTO tasks (title, description, completed) VALUES (?, ?, ?)',
            (title, description, int(completed))
        )
        task_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return task_id

    @staticmethod
    def get_all():
        conn = get_db()
        tasks = conn.execute('SELECT * FROM tasks').fetchall()
        conn.close()
        return [dict(t) for t in tasks]

    @staticmethod
    def get_by_id(task_id):
        conn = get_db()
        task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
        conn.close()
        return dict(task) if task else None

    @staticmethod
    def update(task_id, title, description, completed):
        conn = get_db()
        conn.execute(
            'UPDATE tasks SET title = ?, description = ?, completed = ? WHERE id = ?',
            (title, description, int(completed), task_id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete(task_id):
        conn = get_db()
        conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        conn.close()
