from flask import render_template, request, redirect, url_for
from . import db
from .models import Expense

def register_routes(app):
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
    def add():
        title = request.form.get('title')
        amount = request.form.get('amount')
        category = request.form.get('category')
        if title and amount and category:
            db.session.add(Expense(title=title, amount=float(amount), category=category))
            db.session.commit()
        return redirect(url_for('index'))

    @app.route('/delete/<int:id>')
    def delete(id):
        expense = Expense.query.get_or_404(id)
        db.session.delete(expense)
        db.session.commit()
        return redirect(url_for('index'))