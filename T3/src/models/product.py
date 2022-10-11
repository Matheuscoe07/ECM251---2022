import streamlit as st
class Product():
    def __init__(self, name, price, url):
        self._name = name
        self._price = price
        self._url = url
    
    def get_name(self):
        return self._name
    def get_name(self):
        return self._price
    def get_name(self):
        return self._url

    def __str__(self):
        return f'{self._name} + {self._price} + {self._url}'
    
    def __eq__(self, __o: object):
        if isinstance(__o, Product):
            return self._name == __o.get_name()
        else:
            return False
