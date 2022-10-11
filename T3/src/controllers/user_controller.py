import streamlit as st
from models.user import User

class UserController():
    def __init__(self):
        if 'usuario' not in st.session_state:
            st.session_state.usuario = None
        if 'all_users' not in st.session_state:
            u1 = User(name = "Mario", email = "mario@mshrm.com", password = "Peach")
            u2 = User(name = "Sonic", email = "sonic@hills.com", password = "Amy")
            u3 = User(name = "Link", email = "link@hyrule.com", password = "Zelda")
            u4 = User(name = "Tom Nook", email = "Tom@NookInc.com", password = "Money")
            st.session_state.all_users = [u1, u2, u3, u4]
    
    def checkLogin(self, email, password):
        right_user = None
        for u in st.session_state.all_users:
            if email == u.get_email() and u.check_password(password):
                right_user = u
                break
        if right_user == None:
            st.error('Usuário ou senha inválidos')
            st.session_state.usuario = None
        else:
            st.success('Login realizado com sucesso')
            st.session_state.usuario = right_user