import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_CONNECTION_STRING = "postgresql://myuser:mypassword@localhost:5432/mydatabase"

@pytest.fixture(scope="session")
def db():
    engine = create_engine(DB_CONNECTION_STRING)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
