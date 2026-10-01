import pytest
from app import create_app, db
from app.models import Expense

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_add_expense(client):
    rv = client.post('/add', data={'amount': '50', 'category': 'Food', 'description': 'Lunch', 'date': '2023-01-01'})
    assert rv.status_code == 302
    with client.application.app_context():
        assert Expense.query.count() == 1
        assert Expense.query.first().amount == 50

def test_delete_expense(client):
    client.post('/add', data={'amount': '20', 'category': 'Transport', 'description': 'Bus', 'date': '2023-01-01'})
    client.get('/delete/1')
    with client.application.app_context():
        assert Expense.query.count() == 0