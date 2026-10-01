from flask import current_app as app, render_template, request, redirect, url_for, flash
from app import db
from app.models import Expense
from datetime import datetime

@app.route('/')
def index():
    category = request.args.get('category')
    query = Expense.query
    if category:
        query = query.filter_by(category=category)
    expenses = query.all()
    total = sum(e.amount for e in expenses)
    return render_template('index.html', expenses=expenses, total=total, selected_category=category)

@app.route('/add', methods=['POST'])
def add_expense():
    try:
        amount = float(request.form.get('amount'))
        category = request.form.get('category')
        description = request.form.get('description')
        date_str = request.form.get('date')
        date = datetime.strptime(date_str, '%Y-%m-%d') if date_str else datetime.utcnow()

        if not category or not description:
            raise ValueError("Missing fields")

        new_expense = Expense(amount=amount, category=category, description=description, date=date)
        db.session.add(new_expense)
        db.session.commit()
    except Exception:
        flash("Invalid input")
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['POST'])
def edit_expense(id):
    expense = Expense.query.get_or_404(id)
    try:
        expense.amount = float(request.form.get('amount'))
        expense.category = request.form.get('category')
        expense.description = request.form.get('description')
        db.session.commit()
    except Exception:
        flash("Invalid update")
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for('index'))