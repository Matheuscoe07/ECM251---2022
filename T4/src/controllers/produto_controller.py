from src.models.produto import Produto
from src.dao.produto_dao import ProdutoDAO

class ProdutoController:
    def __init__(self) -> None:
        pass

    def pegar_produto(self, id) -> Produto:
        produto = ProdutoDAO.get_instance().pegar_item(id)
        return produto

    def add_produto(self, produto) -> None:
        ProdutoDAO.get_instance().inserir_produto(produto)
    
    def pegar_todos_produtos(self) -> list[Produto]:
        produtos = ProdutoDAO.get_instance().get_all()
        return produtos
