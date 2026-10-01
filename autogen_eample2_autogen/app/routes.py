from flask import render_template, request, redirect, url_for
from . import db
from .models import Task

def register_routes(app):
    @app.route('/')
    def index():
        tasks = Task.query.all()
        return render_template('index.html', tasks=tasks)

    @app.route('/add', methods=['POST'])
    def add_task():
        title = request.form.get('title')
        if not title:
            return "Title is required", 400
        new_task = Task(title=title, description=request.form.get('description', ''))
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))

    @app.route('/update/<int:id>', methods=['POST'])
    def update_task(id):
        task = Task.query.get_or_404(id)
        task.completed = not task.completed
        db.session.commit()
        return redirect(url_for('index'))

    @app.route('/delete/<int:id>', methods=['POST'])
    def delete_task(id):
        task = Task.query.get_or_404(id)
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('index'))