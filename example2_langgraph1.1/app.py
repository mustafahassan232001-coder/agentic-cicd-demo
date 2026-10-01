from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import db

app = Flask(__name__)

@app.route('/')
def index():
    tasks = db.get_all_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    if not title:
        return "Title is required", 400
    db.add_task(title, description)
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    task = db.get_task(task_id)
    if not task:
        return "Task not found", 404
    
    # Toggle status
    _, title, desc, completed = task
    db.update_task(task_id, title, desc, not completed)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if not db.delete_task(task_id):
        return "Task not found", 404
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)