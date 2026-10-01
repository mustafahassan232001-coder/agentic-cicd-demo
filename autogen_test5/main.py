from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory storage
tasks = {}

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    task_id = str(uuid.uuid4())
    task = {'id': task_id, 'title': data['title'], 'completed': False}
    tasks[task_id] = task
    return jsonify(task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(list(tasks.values())), 200

@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    if task_id not in tasks:
        return jsonify({'error': 'Task not found'}), 404
    
    data = request.get_json()
    tasks[task_id].update({
        'title': data.get('title', tasks[task_id]['title']),
        'completed': data.get('completed', tasks[task_id]['completed'])
    })
    return jsonify(tasks[task_id]), 200

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        return '', 204
    return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)