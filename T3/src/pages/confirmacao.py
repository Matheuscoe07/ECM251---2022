import streamlit as st

col1, col2 = st.columns(2)

if st.session_state.usuario != None:
    with col1:
        st.title('Cambio efetuado!')
        st.subheader('Obrigado por escolher a R$ como sua casa de câmbio!')
    with col2:
        st.image('https://i.imgur.com/vxvpZEj.png', width = 160)

else:
    st.error('Não identificamos seu login, por isso você não poderá acessar a R$ :(')
