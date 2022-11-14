import streamlit as st

st.set_page_config(
    page_title="Home - Loja T4",
    page_icon="💿",
    #layout="wide",
    # initial_sidebar_state="collapsed"
)

st.header("Seu perfil")

with st.container():
    cola, colb, colc, coli = st.columns(4)
    with cola:
        st.button("Carrinho")

    with colb:
        st.button("Perfil", disabled = True)

    with colc:
        st.button("Home")
    
    with coli:
        st.button("Cadastrar produto")
    
st.subheader("Informações principais")
st.write("Nome:")
#st.write()
st.write("Email:")
#st.write()

st.subheader("Alterar dados")

with st.expander("Alteração de dados:"):
    email = st.text_input("Novo email")
    senha = st.text_input("Nova senha", type="password")
    enviar = st.button("Alterar dados")
    

