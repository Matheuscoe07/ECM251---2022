class User():
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def __str__(self) -> str:
        return f'User(name:{self.name}, email:{self.email}, password:{self.password})'
    
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def check_password(self, password):
        return self.password == password