class Usuario:
    def __init__(self, id, nome_usuario, email, senha) -> None:
        self._id = id
        self._nome_usuario = nome_usuario
        self._email = email
        self._senha = senha
    
    def get_nome_usuario(self):
        return self._nome_usuario
    def set_nome_usuario(self, nome_usuario):
        self._nome_usuario = nome_usuario
    
    def get_email(self):
        return self._email
    def set_email(self, email):
        self._email = email
    
    def get_senha(self):
        return self._senha
    def set_senha(self, senha):
        self._senha = senha
    
    def __str__(self) -> str:
        return f'Usuario: Nome:{self._nome_usuario} - Email:{self._email}'
    
    def verifica_senha(self, senha):
        return self._senha == senha
