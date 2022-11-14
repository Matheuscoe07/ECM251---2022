import streamlit as st
from models.usuario import Usuario
from controllers.usuario_controller import UsuarioController

st.set_page_config(
    page_title="Login - Loja T4",
    page_icon="💿",
    #layout="wide",
    initial_sidebar_state="collapsed"
)

if st.session_state.usuario != None:
    st.warning("Você ja esta logado!")
else:
    st.header("Login")
    email = st.text_input('Email', placeholder="Insira seu email")
    senha = st.text_input('Senha', type="password", placeholder="Insira sua senha")
    st.markdown('<a href="">Esqueci minha senha</a>', unsafe_allow_html=True)
    st.checkbox("Lembre de mim")
    logar = st.button('Login')
    if logar:
        if st.session_state.usuario_controller.verifica_usuario(email, senha):
            st.session_state.usuario = st.session_state.usuario_controller.pegar_usuario(email)
            st.success("Bem vindo! Login realizado com sucesso!")
        else:
            st.error("Algo deu errado...")

    st.subheader("Não possui uma conta?")
    cadastrar = st.button("Cadastre-se")


