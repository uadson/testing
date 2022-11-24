from ..app.models import User

    
def test_user_save(session):
    user = User(name='Foo', email='foo@bar.com')
    session.save(user)
    assert isinstance(user.id, int)
    
    
def test_list_users(session):
    users = [User(name='Foo', email='foo@bar.com'), User(name='Dot', email='dot@env.com')]
    for user in users:
        session.save(user)
    assert users == session.get_list_objects()
    