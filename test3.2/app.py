from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)

# In-memory storage
tasks = {}

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks.values())

@app.route('/add', methods=['POST'])
def add_task():
    content = request.form.get('content')
    if content:
        task_id = str(uuid.uuid4())
        tasks[task_id] = {'id': task_id, 'content': content, 'completed': False}
    return redirect(url_for('index'))

@app.route('/delete/<task_id>')
def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
    return redirect(url_for('index'))

@app.route('/toggle/<task_id>')
def toggle_task(task_id):
    if task_id in tasks:
        tasks[task_id]['completed'] = not tasks[task_id]['completed']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)