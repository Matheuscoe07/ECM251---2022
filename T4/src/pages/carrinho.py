import streamlit as st

st.set_page_config(
    page_title="Carrinho - Loja T4",
    page_icon="💿",
    #layout="wide",
    initial_sidebar_state="collapsed"
)

with st.container():
    cola, colb, colc, coli = st.columns(4)
    with cola:
        st.button("Carrinho", disabled = True)

    with colb:
        st.button("Perfil")

    with colc:
        st.button("Home")
    
    with coli:
        st.button("Cadastrar produto")


if st.session_state.usuario == None:
    st.header("Carrinho")
    st.write("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")

    produtos = st.session_state.produto_controller.pegar_todos_produtos()
    for produto in produtos:
        st.markdown(f"### {produto.get_nome()}")
        st.markdown(f"#### R${produto.get_preco()}")
    
    st.write("―――――――――――――――――――――――――――――――――――――――――――――――――――――――")

    with st.expander("Escolha seu método de pagamento:"):
        st.radio("Métodos de pagamento:", ["PIX", "Boleto bancário", "Cartão de crédito", "Cartão de débito"])

    with st.expander("Calcular frete"):
        CEP = st.text_input("CEP", placeholder="Insira aqui seu CEP")
        frete = st.button("Calcular frete")

    finalizar = st.button("Finalizar compra")

else:
    st.warning("Você não está logado, faça o login e retorne aqui :)")
