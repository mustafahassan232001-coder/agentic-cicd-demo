from flask import render_template, request, redirect, url_for
from . import db
from .models import Expense

def register_routes(app):
    @app.route('/')
    def index():
        category = request.args.get('category')
        if category:
            expenses = Expense.query.filter_by(category=category).all()
        else:
            expenses = Expense.query.all()
        total = sum(e.amount for e in expenses)
        return render_template('index.html', expenses=expenses, total=total)

    @app.route('/add', methods=['POST'])
    def add():
        try:
            title = request.form.get('title')
            amount = float(request.form.get('amount'))
            category = request.form.get('category')
            if not title or not category: raise ValueError
            new_expense = Expense(title=title, amount=amount, category=category)
            db.session.add(new_expense)
            db.session.commit()
        except:
            pass
        return redirect(url_for('index'))

    @app.route('/delete/<int:id>')
    def delete(id):
        expense = Expense.query.get_or_404(id)
        db.session.delete(expense)
        db.session.commit()
        return redirect(url_for('index'))