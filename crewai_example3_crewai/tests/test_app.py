import pytest
from app import create_app
from database import db
from models import Expense

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client

def test_add_expense(client):
    rv = client.post('/add', data={'amount': 50, 'category': 'Food', 'description': 'Lunch'})
    assert rv.status_code == 302
    with client.application.app_context():
        assert Expense.query.count() == 1
        assert Expense.query.first().amount == 50