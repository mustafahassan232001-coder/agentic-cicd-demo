import pytest
import os
import tempfile
from app import create_app
from app.database import init_db

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app()
    app.config['DATABASE'] = db_path
    app.config['TESTING'] = True

    # Re-initialize with the temp DB path to ensure clean state per test
    init_db(db_path)

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(db_path)
