from job_stats import create_app
import os


def test_config():
    print(os.getenv("POSTGRES_DB_URI"))
    assert not create_app().testing
    assert create_app(
        {"TESTING": True, "SQLALCHEMY_DATABASE_URI": os.getenv("POSTGRES_DB_URI")}
    ).testing
