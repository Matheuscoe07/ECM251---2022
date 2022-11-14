import streamlit as st
import datetime as datetime
from models.usuario import Usuario

st.set_page_config(
    page_title="Cadastro - Loja T4",
    page_icon="💿",
    #layout="wide",
    initial_sidebar_state="collapsed"
)

st.header("Cadastre-se")
nome = st.text_input("Nome completo")
st.radio("Gênero", ["Masculino", "Feminino", "Não-binárie", "Outro"])
st.date_input("Data de nascimento", 
            min_value = datetime.date(1900, 1, 1),
            max_value = datetime.date(2023, 1, 1),
            )
st.text_input("CPF")
st.text_input("Telefone")
email = st.text_input("Email")
senha = st.text_input("Senha", type="password")
st.checkbox("Eu aceito a política de privacidade")
cadastrar = st.button("Cadastrar")
if cadastrar:
    usuario = Usuario(nome, email, senha)
    st.session_state.usuario_controller.add_usuario(usuario)
    st.success("Seja bem vindo! Você foi cadastrado com sucesso :)")
else:
    st.error("Algo deu errado...")


