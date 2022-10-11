import streamlit as st


with open('src/style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

if st.session_state.usuario != None:
    with col1:
        st.image('https://i.imgur.com/vxvpZEj.png', width = 300)

    with col2:
        st.markdown("# **Zelda's Rupees**")
        st.markdown("Rupees, também conhecido como Rupias, é a moeda do mundo de 'The legend of Zelda'. Atualmente (10/2022) ela se encontra em circulação nas terrass de Hyrule, the Dark World, Koholint Island, Termina, Labrynna, Holodrum, the Great Sea, the World of the Ocean King, New Hyrule, Skyloft, Lorule and Hytopia.")
        st.markdown("### 1 Rupee = R$ 0,5")
        valor = st.number_input('Insira aqui o valor que deseja trocar')
        st.write('O valor a ser trocado é de ', valor, 'Reais')
        trocar = st.button("Trocar Rupees")
        if trocar:
            st.success('Favor se encaminhar até a página de carrinho/pagamento')
        

else:
    st.error('Não identificamos seu login, por isso você não poderá acessar a R$ :(')
