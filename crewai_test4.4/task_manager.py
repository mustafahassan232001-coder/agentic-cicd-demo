class TaskManager:
    def __init__(self):
        self.tasks = []
        self.counter = 1

    def add_task(self, content):
        task = {'id': self.counter, 'content': content}
        self.tasks.append(task)
        self.counter += 1

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t['id'] != task_id]

    def update_task(self, task_id, new_content):
        for task in self.tasks:
            if task['id'] == task_id:
                task['content'] = new_content
                break

    def get_all_tasks(self):
        return self.tasks