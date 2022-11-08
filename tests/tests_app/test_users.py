import pytest
from app.user import User
from app.database import Connection
    

@pytest.fixture
def conn():
    # setup
    conn_obj = Connection()
    yield conn_obj
    # tear down
    conn_obj.close()


@pytest.fixture
def session(conn):
    # setup
    session_obj = conn.get_engine()
    yield session_obj
    # tear down
    session_obj.roll_back()
    session_obj.close()
    

def test_user_save(session):
    user = User(name='Foo')
    session.save(user)
    assert isinstance(user.id, int)
    
    
def test_list_users(session):
    users = [User(name='Foo'), User(name='Dot')]
    for user in users:
        session.save(user)
    assert users == session.get_list_objects()
    