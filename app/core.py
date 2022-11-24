class Sender:
    
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
            
        return (senders, receivers)

    
class InvalidEmail(Exception):
    pass


# class MockSender(Sender):
    
#     def __init__(self):
#         self.amount_emails_sent = 0
#         self.send_param = None
        
#     def send(
#         self,
#         senders: str,
#         receivers: str,
#         subject: str,
#         content: str
#     ):
#         self.send_param = (senders, receivers, subject, content)
#         self.amount_emails_sent += 1
    

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