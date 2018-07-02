comments = []
users = []

class User():
    '''Holds user data ''' 
    def __init__(self, username, password, role,comments='',last_seen=''):
        '''initializes user class'''
        self.username = username
        self.password = password
        role = "normal_user"
        self.role = role
        self.comments = comments
        self.last_seen = last_seen

class Moderator(User):
    '''Holds moderator data'''
    def __init__(self, username, password,role,comments= '',last_seen=''):
        super.__init__(username, password,comments,last_seen)
        role="moderator "
        self.role = role 


class Admin(Moderator):
    '''Holds admin data'''
    def __init__(self, username, password,role,comments='',last_seen=''):
        super.__init__(username, password,comments,last_seen)
        role="admin"
        self.role = role 
        self.comments = comments
        self.last_seen = last_seen

class Comments():
    def __init__(self,id,author,message,timestamp):
        self.author = author 
        self.id = id
        self.message = message
        self.timestamp = timestamp

        
    
    
    
