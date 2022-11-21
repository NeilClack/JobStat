from job_stats import create_app
import pytest
import os


@pytest.fixture
def app():
    app = create_app(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": os.getenv("POSTGRES_DB_URI"),
            "JSONIFY_PRETTYPRINT_REGULAR": True,
        }
    )

    yield app


@pytest.fixture
def client(app):
    return app.test_client()
