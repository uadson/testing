class Sender:
    
    def send(
        self,
        senders: str,
        receivers: str,
        subject: str,
        body_text: str
    ):
        if '@' not in senders:
            raise InvalidEmail(f"Invalid Email to {senders}")
        else:
            pass
        
        if '@' not in receivers:
            raise InvalidEmail(f"Invalid Email to {receivers}")
        else:
            pass
        
        return (senders, receivers,)
    
    
class InvalidEmail(Exception):
    pass
