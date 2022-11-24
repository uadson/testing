import pytest

from ..app.core import Sender, InvalidEmail


def test_create_email_sender():
    sender = Sender()
    assert sender is not None


# parameterization of elements
@pytest.mark.parametrize(
    'senders',
    ['foo@bar.com', 'doo@bar.com']
)
def test_sender(senders):
    sender = Sender()
    with pytest.raises(InvalidEmail):
        sender.send(
            senders,
            'receivers',
            'subject',
            'content'
        )
    

@pytest.mark.parametrize(
    'senders',
    ['', 'foo']
)
def test_validate_email_sender(senders):
    sender = Sender()
    with pytest.raises(InvalidEmail):
        sender.send(
            senders,
            'receivers',
            'subject',
            'content'
        )


@pytest.mark.parametrize(
    'receivers',
    ['', 'dot']
)
def test_validate_email_receiver(receivers):
    sender = Sender()
    with pytest.raises(InvalidEmail):
        sender.send(
            'senders',
            receivers,
            'subject', 
            'content'
        )


@pytest.mark.parametrize(
    'receivers',
    ['mud@bar.com', 'dot@bar.com']
)
def test_receiver(receivers):
    sender = Sender()
    with pytest.raises(InvalidEmail):
        sender.send(
            'senders',
            receivers,
            'subject',
            'content'
        )
