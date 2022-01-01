import os
import tempfile

import pytest
from flask import current_app
from flask.cli import with_appcontext
from flask import g

from app.manage import app
from app.shared.models import db 


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    print(db_path, flush=True)
    app.config.update({'TESTING': True, 'DATABASE': db_path})

    with app.test_client() as client:
        with app.app_context():
            with current_app.open_resource("schema.sql") as f:
                db.executescript(f.read().decode("utf8"))
        yield client

    os.close(db_fd)
    os.unlink(db_path)

def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert b'No entries here so far' in rv.data