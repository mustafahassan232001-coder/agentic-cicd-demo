from flask import Flask, render_template, request, redirect, url_for
from task_manager import task_manager

app = Flask(__name__)

@app.route('/')
def index():
    tasks = task_manager.get_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    description = request.form.get('description')
    if description:
        task_manager.add_task(description)
    return redirect(url_for('index'))

@app.route('/delete/<task_id>')
def delete(task_id):
    task_manager.delete_task(task_id)
    return redirect(url_for('index'))

@app.route('/update/<task_id>', methods=['POST'])
def update(task_id):
    description = request.form.get('description')
    completed = request.form.get('completed')
    task_manager.update_task(task_id, description, completed)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)