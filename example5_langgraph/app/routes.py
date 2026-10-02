from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import db
from .models import Task

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', tasks=tasks)

@main.route('/add', methods=['POST'])
@login_required
def add_task():
    content = request.form.get('content')
    if content:
        new_task = Task(content=content, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/delete/<int:id>')
@login_required
def delete_task(id):
    task = Task.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))