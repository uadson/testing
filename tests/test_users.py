from app.models import User

    
def test_user_save(session):
    user = User(name='Foo')
    session.save(user)
    assert isinstance(user.id, int)
    
    
def test_list_users(session):
    users = [User(name='Foo'), User(name='Dot')]
    for user in users:
        session.save(user)
    assert users == session.get_list_objects()
    