from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required, current_user
from models import Task
from database import db

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        task = Task(title=request.form['title'], user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', tasks=tasks)

@tasks_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    task = Task.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('tasks.index'))