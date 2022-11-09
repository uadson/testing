import pytest
from app.database import Connection
    

@pytest.fixture(scope='session')
def conn():
    # setup
    conn_obj = Connection()
    yield conn_obj
    # tear down
    conn_obj.close()


@pytest.fixture
def session(conn):
    # setup
    session_obj = conn.gen_session()
    yield session_obj
    # tear down
    session_obj.roll_back()
    session_obj.close()
