from flask import render_template, request, jsonify
from models import TaskManager

tm = TaskManager()

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/api/tasks', methods=['GET', 'POST'])
    def handle_tasks():
        if request.method == 'GET':
            return jsonify(tm.get_all_tasks())
        data = request.json
        result = tm.create_task(data.get('title'), data.get('description'))
        return jsonify(result), (201 if 'id' in result else 400)

    @app.route('/api/tasks/<int:task_id>', methods=['PUT', 'DELETE'])
    def handle_task(task_id):
        if request.method == 'DELETE':
            return jsonify(tm.delete_task(task_id)), 200
        data = request.json
        result = tm.update_task(task_id, data.get('title'), data.get('description'), data.get('completed'))
        return jsonify(result), (200 if 'success' in result else 400)