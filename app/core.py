class Sender:
    
    def __init__(self):
        self.amount_emails_sent = 0
    
    def send(
        self,
        senders: str,
        receivers: str,
        subject: str,
        content: str
    ):
        if '@' not in senders:
            raise InvalidEmail(f"Invalid Email to {senders}")
        else:
            pass
        
        if '@' not in receivers:
            raise InvalidEmail(f"Invalid Email to {receivers}")
        else:
            pass
        
        self.amount_emails_sent += 1
            
        return (senders, receivers,)

    
class InvalidEmail(Exception):
    pass


class SpamSender:
    
    def __init__(self, session, sender):
        self.session = session
        self.sender = sender
        
    def send_emails(
        self, 
        sender: str,
        user: str, 
        subject: str, 
        content:str
        ):
        for user in self.session.get_list_objects():
            self.sender.send(
                sender,
                user.email,
                subject,
                content
            )