import streamlit as st
from models.produto import Produto

st.set_page_config(
    page_title="Novo Produto - Loja T4",
    page_icon="💿",
    #layout="wide",
    # initial_sidebar_state="collapsed"
)

if st.session_state.usuario != None:
    st.header("Cadastrar novo produto")

    idproduto = st.text_input("ID do produto")
    nomeproduto = st.text_input("Nome do produto")
    valorproduto = st.number_input("Valor do produto", min_value=0.00)
    st.text_input("URL da imagem do produto")
    enviarproduto = st.button("Cadastrar novo produto")

    if enviarproduto:
        produto = Produto(idproduto, nomeproduto, valorproduto)
        st.session_state.produto_controller.add_produto(produto)
        st.success("O produto fora cadastrado com sucesso em nossa database! No entanto, ele será postado em nosso site em um futuro breve")
        st.button("Voltar à página principal")

else:
    st.warning("Você não está logado, faça o login e retorne aqui :)")
