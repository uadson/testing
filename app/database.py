from time import sleep


class Connection:
    
    def __init__(self):
        sleep(1)
    
    def gen_session(self):
        return Session()
        
    def close(self):
        ...
        
        
class Session:
    
    count = 0
    objects = []
    
    def roll_back(self):
        self.objects.clear()
        
    def close(self):
        ...
        
    def get_list_objects(self):
        return self.objects
        
    def save(self, obj):
        Session.count += 1
        obj.id = Session.count
        self.objects.append(obj)