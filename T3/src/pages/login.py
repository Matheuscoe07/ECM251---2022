import streamlit as st
from models.user import User
from controllers.user_controller import UserController


# --- PLANO DE FUNDO ---

#https://i.imgur.com/BQF1Hev.png
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background: #FFFFFF url("https://i.imgur.com/BQF1Hev.png") no-repeat scroll 100% 50%;

[data-testid="stHeader"] {
    background: transparent none repeat fixed 50% 50%;
}

[data-testid="stToolbar"] {
    right: 2rem;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

with open('src/style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- LOGIN ---

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.image("https://i.imgur.com/lWRD4zc.png")  # Logo
    st.markdown('## Bem vindo!')
    st.markdown('# Log In')

    if st.session_state.usuario == None:
        email = st.text_input('Email', placeholder="Insira seu email")
        password = st.text_input('Senha', type="password", placeholder="Insira sua senha")
        enter = st.button('Login')
        if enter:
            #user_controller = UserController()
            UserController().checkLogin(email, password)
    else:
        st.success(f'Seja bem vindo, **{st.session_state.usuario.get_user}**')
        
    st.markdown('<a href="">Esqueci minha senha</a>', unsafe_allow_html=True)
    st.checkbox('Lembre de mim')
    st.markdown('Não tem uma conta?''<a href="">Cadastre-se</a>', unsafe_allow_html=True)
