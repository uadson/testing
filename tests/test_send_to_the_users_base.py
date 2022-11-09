from app.core import Sender
from app.core import SpamSender


def test_spam_send(session):
    spam_sender = SpamSender(session, Sender)
    spam_sender.send_emails(
        'senders',
        'subject',
        'content',
    )