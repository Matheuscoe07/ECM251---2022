import streamlit as st
from models.user import User
from controllers.user_controller import UserController
from models.product import Product
from controllers.product_controller import ProductController

user_controller = UserController()
product_controller = ProductController()

if st.session_state.usuario != None:
    with open('src/style.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.text_input('Pesquisa', placeholder='O que procura?')
    st.markdown('---')
    st.markdown('# A maior casa de câmbio do mundo real e virtual!')
    st.markdown('O processo é simples, basta selecionar a moeda desejada para transformar em reais, selecionar o valor desejado e pagar. O valor cai automaticamente na sua conta bancária!')

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image('https://i.imgur.com/vxvpZEj.png', width=100)
        st.markdown("**Zelda's Rupees**")
        st.caption("1 Rupee = R$ 0,5")
        st.button("Trocar Rupees")
        st.markdown('<a href="">Criar alerta</a>', unsafe_allow_html=True)
    with col2:
        st.image(
            'https://mario.wiki.gallery/images/thumb/1/17/CoinMK8.png/1200px-CoinMK8.png', width=120)
        st.markdown("**Moedas do Mario**")
        st.caption("1 Moeda = R$ 0,7")
        st.button("Trocar Moedas")
        st.markdown('<a href="">Criar alerta</a>', unsafe_allow_html=True)
    with col3:
        st.image('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/2273a93f-836e-4ba7-9245-615da889cc91/dar1kqz-0713830f-d35f-4a46-b261-1cdce1b3c209.png/v1/fill/w_1024,h_1024,strp/ring_render_by_nuryrush_dar1kqz-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTAyNCIsInBhdGgiOiJcL2ZcLzIyNzNhOTNmLTgzNmUtNGJhNy05MjQ1LTYxNWRhODg5Y2M5MVwvZGFyMWtxei0wNzEzODMwZi1kMzVmLTRhNDYtYjI2MS0xY2RjZTFiM2MyMDkucG5nIiwid2lkdGgiOiI8PTEwMjQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.THyV6KeeoAZZvHaradPPxhf8K_Xsxczasly_4wXFCLg', width=145)
        st.markdown("**Anéis do Sonic**")
        st.caption("1 Anel = R$ 1")
        st.button("Trocar Anéis")
        st.markdown('<a href="">Criar alerta</a>', unsafe_allow_html=True)
    with col4:
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Russian_rouble_sign_%28PT_Sans_2.003%29.svg/800px-Russian_rouble_sign_%28PT_Sans_2.003%29.svg.png', width=105)
        st.markdown("**Pokedollars**")
        st.caption("1 Pokedolar = R$ 1,5")
        st.button("Trocar Pokedollars")
        st.markdown('<a href="">Criar alerta</a>', unsafe_allow_html=True)

else:
    st.error('Não identificamos seu login, por isso você não poderá acessar a R$ :(')
