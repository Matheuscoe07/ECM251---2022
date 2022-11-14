class Produto:
    def __init__(self, id, nome, preco) -> None:
        self._id = id
        self._nome = nome
        self._preco = preco
    
    def str(self) -> str:
        return f'Produto: id:{self.id} - Nome:{self.nome} - Preco:{self.preco}'
    
    def get_id(self):
        return self._id
    def set_id(self, id):
        self._id = id
    
    def get_nome(self):
        return self._nome
    def set_nome(self, nome):
        self._nome = nome
    
    def get_preco(self):
        return self._preco
    def set_preco(self, preco):
        self._preco = preco
