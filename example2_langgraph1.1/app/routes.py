from flask import Blueprint, request, jsonify
from .models import TaskModel

task_bp = Blueprint('tasks', __name__)

@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(TaskModel.get_all()), 200

@task_bp.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = TaskModel.get_by_id(id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task), 200

@task_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    task_id = TaskModel.create(data['title'], data.get('description', ''), data.get('completed', False))
    return jsonify({'id': task_id, 'message': 'Task created'}), 201

@task_bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    if not TaskModel.get_by_id(id):
        return jsonify({'error': 'Task not found'}), 404
    
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
        
    TaskModel.update(id, data['title'], data.get('description', ''), data.get('completed', False))
    return jsonify({'message': 'Task updated'}), 200

@task_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    if not TaskModel.get_by_id(id):
        return jsonify({'error': 'Task not found'}), 404
    
    TaskModel.delete(id)
    return '', 204
