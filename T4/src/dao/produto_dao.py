import sqlite3
from src.models.produto import Produto

class ProdutoDAO:
    
    _instance = None
    
    def __init__(self) -> None:
        self._connect()
    
    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = ProdutoDAO()
        return cls._instance
    
    def _connect(self): #cria uma conexao com o banco
        self.conn = sqlite3.connect('databases\sqlite.db')
    
    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
                            SELECT * FROM Produtos;
                            """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Produto(id=resultado[0], nome=resultado[1], preco=resultado[2]))
        self.cursor.close()
        return resultados
    
    def inserir_produto(self, produto):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
                            INSERT INTO Produtos (id, nome, preco)
                            VALUES(?,?,?);
                            """, (produto.get_id(), produto.get_nome(), produto.get_preco()))
        self.conn.commit()
        self.cursor.close()