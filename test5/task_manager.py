import uuid

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = {
            "id": str(uuid.uuid4()),
            "description": description,
            "completed": False
        }
        self.tasks.append(task)
        return task

    def get_tasks(self):
        return self.tasks

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t['id'] != task_id]

    def update_task(self, task_id, description, completed):
        for task in self.tasks:
            if task['id'] == task_id:
                task['description'] = description
                task['completed'] = completed == 'on'
                return True
        return False

# Singleton instance for the app to share
task_manager = TaskManager()