from src.models.produto import Produto
from src.controllers.produto_controller import ProdutoController

controller = ProdutoController()
produtos = controller.pegar_todos_produtos()

for produto in produtos:
    print(produto)

novo_item = Produto("AAA", "aaa", 10)
controller.inserir_produto()