from models.produto import Produto
from controllers.produto_controller import ProdutoController
from models.usuario import Usuario
from controllers.usuario_controller import UsuarioController

import streamlit as st

if 'usuario_controller' not in st.session_state:
    st.session_state.usuario_controller = UsuarioController()
if 'item_controller' not in st.session_state:
    st.session_state.produto_controller = ProdutoController()
if 'usuario' not in st.session_state:
    st.session_state.usuario = None

st.set_page_config(
    page_title="Home - Loja T4",
    page_icon="💿",
    layout="wide",
    #initial_sidebar_state="collapsed"
)

st.header("Bem vindo à T4")
st.subheader("A melhor loja que você nunca viu!")

if st.session_state.usuario != None: #NÃO ESQUECER DE DESTROCAR PARA OS TESTES!!!!!!!!!!!!!!!!!!!
    with st.container():
        cola, colb, colc, coli = st.columns(4)
        with cola:
            st.button("Carrinho")
        
        with colb:
            st.button("Perfil")
        
        with colc:
            st.button("Home", disabled = True)
        
        with coli:
            st.button("Cadastrar produto")


    st.subheader("Produtos")

    with st.container():
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.image("src/assets/Super_Mario_World.jpg")
            st.write('Super Mario World - SNES')
            st.write("~R$ 105,00~")
            st.write("**R$ 100,00** (a vista)")
            visitar = st.button("Saber mais", key="produto1")
            carrinho1 = st.button("Adicionar ao carrinho", key="add1")
            if carrinho1:
                st.success("Produto adicionado ao carrinho!")
            
        with col2:
            st.image("src/assets/Sonic_The_Hedgehog.jpg")
            st.write('Sonic the Hedgehog - Mega Drive')
            st.write("~R$ 105,00~")
            st.write("**R$ 100,00** (a vista)")
            visitar = st.button("Saber mais", key="produto2")
            carrinho2 = st.button("Adicionar ao carrinho", key="add2")
            if carrinho2:
                st.success("Produto adicionado ao carrinho!")

            
        with col3:
            st.image("src/assets/Donkey_Kong_Country_3.jpg")
            st.write('Donkey Kong Country 3 - SNES')
            st.write("~R$ 105,00~")
            st.write("**R$ 100,00** (a vista)")
            visitar = st.button("Saber mais", key="produto3")
            carrinho3 = st.button("Adicionar ao carrinho", key="add3")
            if carrinho3:
                st.success("Produto adicionado ao carrinho!")

        with col4:
            st.image("src/assets/Pokemon_Silver.jpg")
            st.write('Pokemon Silver - GB Color')
            st.write("~R$ 105,00~")
            st.write("**R$ 100,00** (a vista)")
            visitar = st.button("Saber mais", key="produto4")
            carrinho4 = st.button("Adicionar ao carrinho", key="add4")
            if carrinho4:
                st.success("Produto adicionado ao carrinho!")

    with st.container():
        col5, col6, col7, col8 = st.columns(4)
        with col5:
            st.image("src/assets/Ocarina_Of_Time.jpg")
            st.write('Legend of Zelda: Ocarina of time - N64')
            st.write("~R$ 105,00~")
            st.write("**R$ 100,00** (a vista)")
            visitar = st.button("Saber mais", key="produto5")
            carrinho5 = st.button("Adicionar ao carrinho", key="add5")
            if carrinho5:
                st.success("Produto adicionado ao carrinho!")

        with col6:
            st.image("src/assets/Pokemon_Platinum.jpg")
            st.write('Pokemon Platinum - NDS')
            st.write("~R$ 105,00~")
            st.write("**R$ 100,00** (a vista)")
            visitar = st.button("Saber mais", key="produto6")
            carrinho6 = st.button("Adicionar ao carrinho", key="add6")
            if carrinho6:
                st.success("Produto adicionado ao carrinho!")
            
        with col7:
            st.image("src/assets/Crash_Bandicoot.jpg")
            st.write('Crash Bandicoot - PS1')
            st.write("~R$ 105,00~")
            st.write("**R$ 100,00** (a vista)")
            visitar = st.button("Saber mais", key="produto7")
            carrinho7 = st.button("Adicionar ao carrinho", key="add7")
            if carrinho7:
                st.success("Produto adicionado ao carrinho!")
            
        with col8:
            st.image("src/assets/Donkey_Kong_Country.jpg")
            st.write('Donkey Kong Country - SNES')
            st.write("~R$ 105,00~")
            st.write("**R$ 100,00** (a vista)")
            visitar = st.button("Saber mais", key="produto8")
            carrinho8 = st.button("Adicionar ao carrinho", key="add8")
            if carrinho8:
                st.success("Produto adicionado ao carrinho!")
            

else:
    st.warning("Você não está logado, faça o login e retorne aqui :)")
