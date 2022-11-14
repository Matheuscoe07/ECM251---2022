from src.dao.produto_dao import ProdutoDAO

produtos = ProdutoDAO.get_instance().get_all()

for produto in produtos:
    print(produto)
