from flask import Flask, render_template, request, redirect, url_for
from task_manager import TaskManager

app = Flask(__name__)
manager = TaskManager()

@app.route('/')
def index():
    tasks = manager.get_all_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    content = request.form.get('content')
    if content:
        manager.add_task(content)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    manager.delete_task(task_id)
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    new_content = request.form.get('content')
    manager.update_task(task_id, new_content)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)