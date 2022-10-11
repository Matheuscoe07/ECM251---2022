import streamlit as st

with open('src/style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

if st.session_state.usuario != None:
    with col1:
        st.header('Como deseja pagar?')
        pagamento = st.radio('Métodos de pagamento:', ('PIX','Cartão de crédito', 'Cartão de débito', 'Boleto bancário', 'Pagar em agência'))
        if pagamento == 'PIX':
            st.markdown('---')
            st.write('QR Code:')
            st.image('https://br.qr-code-generator.com/wp-content/themes/qr/new_structure/markets/core_market/generator/dist/generator/assets/images/websiteQRCode_noFrame.png')
            st.write('PIX Copia e cola: 54748745435768740003547687413201324657864000000058478708978709877857/978725123368693696585274121473520000000013578767441212135489')
            apertou = st.button('Pagar!')
            if apertou:
                st.success('Obrigado pela escolha! Você será redirecionado em breve! (spoiler: não vai ter redirecionamento pq o streamlit não faz essa função então vai pra página de confirmação por favor)')
        
        elif pagamento == 'Cartão de crédito':
            st.markdown('---')
            num_cartao = st.text_input('Número do cartão', placeholder='Digite aqui o número do cartão')
            nome_cartao = st.text_input('Nome do titular', placeholder='Digite aqui o nnome do titular')
            codigo = st.text_input('CVV', placeholder='Digite aqui o CVV do cartão')
            data_venc = st.date_input('Data de vencimento')
            apertou = st.button('Pagar!')
            
            if num_cartao and nome_cartao and codigo != None:
                if apertou:
                    st.success('Obrigado pela escolha! Você será redirecionado em breve! (spoiler: não vai ter redirecionamento pq o streamlit não faz essa função então vai pra página de confirmação por favor)')
            else:
                if apertou:
                    st.error('Erro! Falta de informações...')
        
        elif pagamento == 'Cartão de débito':
            st.markdown('---')
            num_cartao = st.text_input('Número do cartão', placeholder='Digite aqui o número do cartão')
            nome_cartao = st.text_input('Nome do titular', placeholder='Digite aqui o nnome do titular')
            codigo = st.text_input('CVV', placeholder='Digite aqui o CVV do cartão')
            data_venc = st.date_input('Data de vencimento')
            apertou = st.button('Pagar!')
            
            if num_cartao and nome_cartao and codigo != None:
                if apertou:
                    st.success('Obrigado pela escolha! Você será redirecionado em breve! (spoiler: não vai ter redirecionamento pq o streamlit não faz essa função então vai pra página de confirmação por favor)')
            else:
                if apertou:
                    st.error('Erro! Falta de informações...')
        
        elif pagamento == 'Boleto bancário':
            st.markdown('---')
            baixou = st.download_button('Baixe aqui o seu boleto bancário', data='')
            if baixou:
                st.success('Obrigado pela escolha! Você será redirecionado em breve! (spoiler: não vai ter redirecionamento pq o streamlit não faz essa função então vai pra página de confirmação por favor)')
        
        else:
            st.markdown('---')
            st.markdown('**Endereço:** Okugaharacho, Nara, 630-1232, Japan')
            st.markdown('**Agência:** 1234')
            apertou = st.button('Gerar recibo!')
            if apertou:
                st.success('Obrigado pela escolha! Você será redirecionado em breve! (spoiler: não vai ter redirecionamento pq o streamlit não faz essa função então vai pra página de confirmação por favor)')
    with col2:
        st.image('https://i.imgur.com/vxvpZEj.png', width = 175)
        st.markdown("### Zelda's Rupees")
        st.markdown("1 Rupee = R$ 0,5")

else:
    st.error('Não identificamos seu login, por isso você não poderá acessar a R$ :(')
