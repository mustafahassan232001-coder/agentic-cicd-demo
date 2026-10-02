from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models import Expense
from sqlalchemy import func

expense_bp = Blueprint('expense_bp', __name__)

@expense_bp.route('/')
def index():
    category = request.args.get('category')
    query = Expense.query
    if category:
        query = query.filter_by(category=category)
    
    expenses = query.order_by(Expense.date.desc()).all()
    total = db.session.query(func.sum(Expense.amount)).scalar() or 0
    return render_template('index.html', expenses=expenses, total=total, active_category=category)

@expense_bp.route('/add', methods=['POST'])
def add_expense():
    try:
        amount = float(request.form['amount'])
        category = request.form['category']
        description = request.form['description']
        new_expense = Expense(amount=amount, category=category, description=description)
        db.session.add(new_expense)
        db.session.commit()
    except:
        flash('Invalid input')
    return redirect(url_for('expense_bp.index'))

@expense_bp.route('/delete/<int:id>')
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for('expense_bp.index'))