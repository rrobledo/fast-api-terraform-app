import alembic.config
import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session
from sqlalchemy_utils import database_exists  # type: ignore

from app.settings import globals as g


@pytest.yield_fixture(name="test_db", scope="session")
def setup_test_db():
    # Configs only used in test
    PG_DATABASE_URL: str = g.config(
        "PG_DATABASE_URL",
        cast=str,
        default="postgresql://postgres:postgres@localhost:5432",
    )
    TEST_DATABASE: str = g.config("TEST_DATABASE", cast=str, default="db_test")

    # Override global DATABASE_URL to point at test database
    g.DATABASE_CONN_URL = PG_DATABASE_URL
    g.DATABASE_NAME = TEST_DATABASE
    g.DATABASE_URL = f"{PG_DATABASE_URL}/{TEST_DATABASE}"

    pg_engine = create_engine(PG_DATABASE_URL)

    conn = pg_engine.connect()
    conn.execute("COMMIT")
    if database_exists(g.DATABASE_URL):
        conn.execute(f"DROP DATABASE {TEST_DATABASE}")
    conn.execute("COMMIT")
    conn.execute(f"CREATE DATABASE {TEST_DATABASE}")
    engine2 = create_engine(f"{PG_DATABASE_URL}/{TEST_DATABASE}", echo=True)
    conn2 = engine2.connect()
    conn2.execute("COMMIT")
    conn2.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
    conn2.close()
    engine2.dispose()

    alembic.config.main(argv=["--raiseerr", "upgrade", "head"])

    try:
        engine = create_engine(f"{PG_DATABASE_URL}/{TEST_DATABASE}", echo=True)
        yield engine

        engine.dispose()
    finally:
        conn.execute("COMMIT")
        conn.execute(f"DROP DATABASE {TEST_DATABASE}")
        conn.close()


@pytest.yield_fixture(name="db", scope="function")
def db_session(test_db):
    connection = test_db.connect()
    transaction = connection.begin()
    session = Session(autocommit=False, autoflush=False, bind=connection)
    try:
        session.begin_nested()
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()
