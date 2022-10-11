import streamlit as st
from models.product import Product

class ProductController():
    def __init__(self):
        if 'cart' not in st.session_state:
            st.session_state.carrinho = []
        if 'stock' not in st.session_state:
            p1 = Product(name="Rupee", price=0.5, url=""),
            p2 = Product(name="Coin", price=0.7, url=""),
            p3 = Product(name="Ring", price=1, url=""),
            p4 = Product(name="Pokedollar", price=1.5, url="")
            st.session_state.estoque = [p1, p2, p3, p4]
