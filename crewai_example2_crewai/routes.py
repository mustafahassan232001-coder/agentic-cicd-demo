from flask import Blueprint, request, jsonify
from models import Task

task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(Task.get_all()), 200

@task_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.get_by_id(task_id)
    if not task: return jsonify({'error': 'Task not found'}), 404
    return jsonify(task), 200

@task_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Missing title'}), 400
    task_id = Task.create(data['title'], data.get('description', ''), data.get('completed', False))
    return jsonify({'id': task_id}), 201

@task_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if not Task.get_by_id(task_id): return jsonify({'error': 'Task not found'}), 404
    data = request.get_json()
    Task.update(task_id, data.get('title'), data.get('description'), data.get('completed'))
    return jsonify({'message': 'Task updated'}), 200

@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if not Task.get_by_id(task_id): return jsonify({'error': 'Task not found'}), 404
    Task.delete(task_id)
    return '', 204