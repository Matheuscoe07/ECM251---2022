from src.models.usuario import Usuario
from src.dao.usuario_dao import UsuarioDAO

class UsuarioController:
    def __init__(self) -> None:
        pass
    
    def pegar_usuario(self, email) -> Usuario:
        usuario = UsuarioDAO.get_instance().get_usuario(email)
        return usuario
    
    def add_usuario(self, usuario) -> Usuario:
        UsuarioDAO.get_instance().add_usuario(usuario)
    
    def pegar_todos_usuarios(self):
        usuarios = UsuarioDAO.get_instance().get_all()
        return usuarios
    
    def atualizar_usuario(self, usuario):
        UsuarioDAO.get_instance().atualizar_usuario(usuario)
    
    def verifica_usuario(self, email, senha):
        usuario = UsuarioDAO.get_instance().get_usuario(email)
        if usuario != None:
            return usuario.verifica_usuario(senha)
        else:
            return False
