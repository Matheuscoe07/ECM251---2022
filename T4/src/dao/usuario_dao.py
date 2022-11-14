import sqlite3
from src.models.usuario import Usuario

class UsuarioDAO:

    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = UsuarioDAO()
        return cls._instance

    def _connect(self):  # cria uma conexao com o banco
        self.conn = sqlite3.connect('databases\sqlite.db')

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
                            SELECT * FROM Usuarios;
                            """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(
                Usuario(id=resultado[0], nome=resultado[1], email=resultado[2], senha=resultado[3]))
        self.cursor.close()
        return resultados

    def inserir_usuario(self, usuario):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
                            INSERT INTO Usuarios (id, nome, email, senha)
                            VALUES(?,?,?,?);
                            """, (usuario.get_id(), usuario.get_nome(), usuario.get_email(), usuario.get_senha()))
        self.conn.commit()
        self.cursor.close()
    
    def atualizar_usuario(self, usuario):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
                            UPDATE Usuarios SET email = ?, senha = ? WHERE nome = ?
                            """, (usuario.get_email(), usuario.get_senha(), usuario.get_nome_usuario()))
        self.conn.commit()
        self.cursor.close()
    
    def get_usuario(self, nome_usuario):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Usuarios WHERE nome = ?;
        """, (nome_usuario))
        resultado = self.cursor.fetchone()
        self.cursor.close()
        return Usuario(nome_usuario=resultado[1], email=resultado[2], senha=resultado[3])
