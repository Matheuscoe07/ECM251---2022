import streamlit as st

st.set_page_config(
    page_title="Confirmação - Loja T4",
    page_icon="💿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.header("Obrigado pela sua compra!")
home = st.button("Voltar à página inicial")