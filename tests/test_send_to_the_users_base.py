import pytest
from unittest.mock import Mock

from ..app.core import Sender
from ..app.core import SpamSender
from ..app.models import User


def test_spam_send(session):
    spam_sender = SpamSender(session, Sender)
    spam_sender.send_emails(
        'sender',
        'subject',
        'user',
        'content',
    )
    
    
@pytest.mark.parametrize(
    'users',
    [
        [
            User(name='Foo', email='foo@bar.com'),
            User(name='Dot', email='dot@env.com')
        ],
        [
            User(name='Foo', email='foo@bar.com'),
        ],
    ]
)
def test_amount_spam_send(session, users):
    for user in users:
        session.save(user)
    sender = Mock()
    spam_sender = SpamSender(session, sender)
    spam_sender.send_emails(
        'test@test.com',
        'user',
        'subject',
        'content'
    )
    assert len(users) == sender.send.call_count
    

def test_spam_param(session):
    user = User(name='Foo', email='foo@bar.com')
    session.save(user)
    sender = Mock()
    spam_sender = SpamSender(session, sender)
    spam_sender.send_emails(
        'test@test.com',
        'foo@bar.com',
        'subject',
        'content',
    )
    sender.send.assert_called_once_with(
        'test@test.com',
        'foo@bar.com',
        'subject',
        'content',
    )
