from app.user import User
from app.database import Connection
    
    
def test_user_save():
    conn = Connection()
    session = conn.get_engine()
    user = User(name='Foo')
    session.save(user)
    assert isinstance(user.id, int)
    session.roll_back()
    session.close()
    conn.close()
    
    
def test_list_users():
    conn = Connection()
    session = conn.get_engine()
    users = [User(name='Foo'), User(name='Dot')]
    for user in users:
        session.save(user)
    assert users == session.get_list_objects()
    session.roll_back()
    session.close()
    conn.close()
    