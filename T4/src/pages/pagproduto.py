import streamlit as st

st.set_page_config(
    page_title="Produto - Loja T4",
    page_icon="💿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

with st.container():
    cola, colb, colc, coli = st.columns(4)
    with cola:
        st.button("Carrinho")

    with colb:
        st.button("Perfil")

    with colc:
        st.button("Home")
    
    with coli:
        st.button("Cadastrar produto")

#if saiba mais = produto1:
with st.expander("Super Mario World - SNES"):
    col1, col2 = st.columns(2)
    with col1:
        st.header("Super Mario World - SNES")
        st.write("~R$ 105,00~")
        st.write("**R$ 100,00**")
        st.write("À vista no PIX ou boleto bancário (5% de desconto)")
        st.write("ou 6x de R$ 17,5 sem juros")
        
        st.caption("As compras devem ser realizadas na página principal, essa é apenas uma página informativa")
        
        st.subheader("Descrição do produto")
        st.write("Após trazer paz ao Mushroom World em Super Mario Bros. 3, os irmãos Mario e Luigi decidem tirar férias com a Princesa Toadstool em um lugar chamado Dinosaur Land, um mundo com tema pré-histórico, cheio de dinossauros e outros inimigos. Enquanto descansa na praia, a Princesa Toadstool é capturada por Bowser. Quando Mario e Luigi acordam, eles tentam encontrá-la e, após horas de busca, encontram um ovo gigante na floresta. De repente, esse ovo eclode e dele sai um jovem dinossauro chamado Yoshi, que lhes diz que seus amigos dinossauros também foram aprisionados em ovos por Koopalings mal-intencionados. Mario e Luigi logo percebem que isso deve ser obra do malvado Rei Bowser e de seus Koopalings. Mario, Luigi e Yoshi decidem salvar Toadstool e os amigos dinossauros de Yoshi, atravessando a Dinosaur Land em busca de Bowser e seus Koopalings. Para ajudá-lo, Yoshi dá uma capa a Mario quando eles começam sua jornada. Mario e Luigi continuam a seguir Bowser, derrotando os Koopalings no processo e salvando os amigos de Yoshi. Eles finalmente chegam ao castelo de Bowser, onde enfrentam-no em uma batalha final. Eles enviam Bowser aos céus e salvam a Princesa Toadstool, restaurando a paz na Dinosaur Land.")

        
    with col2:
        st.image("src/assets/Super_Mario_World.jpg")

# -------------------------------------------------------------------------------------------

with st.expander("Sonic The Hedgehog - Mega Drive"):
    col1, col2 = st.columns(2)
    with col1:
        st.header("Sonic The Hedgehog - Mega Drive")
        st.write("~R$ 105,00~")
        st.write("**R$ 100,00**")
        st.write("À vista no PIX ou boleto bancário (5% de desconto)")
        st.write("ou 6x de R$ 17,5 sem juros")

        st.caption("As compras devem ser realizadas na página principal, essa é apenas uma página informativa")

        st.subheader("Descrição do produto")
        st.write("Numa tentativa de roubar as seis Esmeraldas do Caos e aproveitar o seu poder para controlar o mundo, o Dr. Ivo Robotnik (conhecido como Dr. Eggman na versão japonesa) aprisionou os animais da Ilha do Sul dentro de robots agressivos e de cápsulas metálicas estacionárias. O jogador controla Sonic, cujo objectivo é parar os planos de Robotnik, salvando os animais e colecionar as Esmeraldas para ele próprio.[1] Se o jogador consegue recolher todas as Esmeraldas e completar o jogo, é mostrado no fim uma sequência final como recompensa. Se as Esmeraldas não forem todas recolhidas, o Robotnik goza com o jogador.")

    with col2:
        st.image("src/assets/Sonic_The_Hedgehog.jpg")
        
#-------------------------------------------------------------------------------------------

with st.expander("Donkey Kong Country 3 - SNES"):
    col1, col2 = st.columns(2)
    with col1:
        st.header("Donkey Kong Country 3 - SNES")
        st.write("~R$ 105,00~")
        st.write("**R$ 100,00**")
        st.write("À vista no PIX ou boleto bancário (5% de desconto)")
        st.write("ou 6x de R$ 17,5 sem juros")

        st.caption("As compras devem ser realizadas na página principal, essa é apenas uma página informativa")
        
        st.subheader("Descrição do produto")
        st.write("Meses após que a Ilha dos Crocodilos é engolida pelo mar, Donkey Kong & Diddy Kong foram explorar as Ilhas DK, mas demoram muito a voltar por dois dias e Dixie Kong começa a procura deles entrando numa massa continental começando na caverna de Wrinkly Kong.")


    with col2:
        st.image("src/assets/Donkey_Kong_Country_3.jpg")

    
# -------------------------------------------------------------------------------------------

with st.expander('Pokemon Silver - GB Color'):
    col1, col2 = st.columns(2)
    with col1:
        st.header('Pokemon Silver - GB Color')
        st.write("~R$ 105,00~")
        st.write("**R$ 100,00**")
        st.write("À vista no PIX ou boleto bancário (5% de desconto)")
        st.write("ou 6x de R$ 17,5 sem juros")

        st.caption("As compras devem ser realizadas na página principal, essa é apenas uma página informativa")

        st.subheader("Descrição do produto")
        st.write("Como nos jogos anteriores, o personagem do jogador recebe seu primeiro Pokémon, uma escolha entre Chikorita, Cyndaquil e Totodile, do cientista Pokémon local da região, Professor Elm, e então começa sua jornada para ganhar os oito Insígnias de Ginásio da região de Johto e em seguida, desafie o Elite dos Quatro e o Campeão para se tornarem o novo Mestre Pokémon da região. Opondo-se a ele está seu rival misterioso, um garoto que roubou um dos outros Pokémon do Professor Elm e regularmente desafia o jogador a testar seus pontos fortes.[10] O jogador também encontra a vilã Equipe Rocket, tendo se reunido para buscar seu líder anterior, Giovanni, para devolver o grupo à sua antiga glória.[9] Eventualmente, o jogador frustra a Equipe Rocket de uma vez por todas e derrota a Elite dos Quatro e o Campeão da Liga Pokémon no Indigo Plateau. O jogador pode então viajar para a região de Kanto dos jogos anteriores e desafiar os Líderes de Ginásio de lá, descobrindo o quanto mudou nos três anos após os eventos de Red e Blue. Depois de derrotar os Líderes de Ginásio da região de Kanto, o jogador pode entrar no traiçoeiro Monte. Área prateada, lar de Pokémon muito poderosos. Nas profundezas do Monte. As cavernas de Silver são Red, o protagonista de Red e Blue, a quem o jogador pode desafiar para a batalha mais difícil do jogo.")

    with col2:
        st.image("src/assets/Pokemon_Silver.jpg")


# -------------------------------------------------------------------------------------------

with st.expander('Legend of Zelda: Ocarina of time - N64'):
    col1, col2 = st.columns(2)
    with col1:
        st.header('Legend of Zelda: Ocarina of time - N64')
        st.write("~R$ 105,00~")
        st.write("**R$ 100,00**")
        st.write("À vista no PIX ou boleto bancário (5% de desconto)")
        st.write("ou 6x de R$ 17,5 sem juros")

        st.caption("As compras devem ser realizadas na página principal, essa é apenas uma página informativa")

        st.subheader("Descrição do produto")
        st.write("Link é um jovem da floresta que vê seu lar em perigo e parte em uma jornada para deter um rei maligno e salvar o reino de Hyrule! Para completar sua missão, ele terá que encontrar a princesa Zelda e ajudar outros povos para reunir a Triforce e restabelecer o equilíbrio do mundo!")


    with col2:
        st.image("src/assets/Ocarina_Of_Time.jpg")


# -------------------------------------------------------------------------------------------

with st.expander('Pokemon Platinum - NDS'):
    col1, col2 = st.columns(2)
    with col1:
        st.header('Pokemon Platinum - NDS')
        st.write("~R$ 105,00~")
        st.write("**R$ 100,00**")
        st.write("À vista no PIX ou boleto bancário (5% de desconto)")
        st.write("ou 6x de R$ 17,5 sem juros")

        st.caption("As compras devem ser realizadas na página principal, essa é apenas uma página informativa")

        st.subheader("Descrição do produto")
        st.write("Igual Diamond e Pearl só que agora é diferente")


    with col2:
        st.image("src/assets/Pokemon_Platinum.jpg")


# -------------------------------------------------------------------------------------------

with st.expander('Crash Bandicoot - PS1'):
    col1, col2 = st.columns(2)
    with col1:
        st.header('Crash Bandicoot - PS1')
        st.write("~R$ 105,00~")
        st.write("**R$ 100,00**")
        st.write("À vista no PIX ou boleto bancário (5% de desconto)")
        st.write("ou 6x de R$ 17,5 sem juros")

        st.caption("As compras devem ser realizadas na página principal, essa é apenas uma página informativa")

        st.subheader("Descrição do produto")
        st.write("Nas ilhas distantes próximas à costa sudeste da Austrália, os malignos cientistas Dr. Neo Cortex e seu assistente Dr. Nitrus Brio desenvolvem um acelerador genético chamado Evolvo-Ray para transformar os habitantes das ilhas em feras com força sobre-humana, e eles escolhem um bandicoot chamado Crash para ser o general de seu exército de animais-soldados. No entanto, Cortex decide fazer um teste inicial em um ainda não totalmente funcional Vórtice Cortex, a máquina que detém o Evolvo-Ray, apesar de seu assistente alertar que o Vórtice não está pronto. Cortex testa Crash na máquina, mas o experimento falha e o Vórtice o rejeita; Crash aproveita o momento para escapar pela janela e acaba caindo em mar aberto. Cortex mantém Tawna, outra bandicoot, como sua próxima cobaia. Tendo se apegado a Tawna durante o cativeiro, Crash faz uma longa jornada para resgatá-la e derrotar Cortex. ")

    with col2:
        st.image("src/assets/Crash_Bandicoot.jpg")

# -------------------------------------------------------------------------------------------

with st.expander('Donkey Kong Country - SNES'):
    col1, col2 = st.columns(2)
    with col1:
        st.header('Donkey Kong Country - SNES')
        st.write("~R$ 105,00~")
        st.write("**R$ 100,00**")
        st.write("À vista no PIX ou boleto bancário (5% de desconto)")
        st.write("ou 6x de R$ 17,5 sem juros")

        st.caption("As compras devem ser realizadas na página principal, essa é apenas uma página informativa")

        st.subheader("Descrição do produto")
        st.write("Nas ilhas distantes próximas à costa sudeste da Austrália, os malignos cientistas Dr. Neo Cortex e seu assistente Dr. Nitrus Brio desenvolvem um acelerador genético chamado Evolvo-Ray para transformar os habitantes das ilhas em feras com força sobre-humana, e eles escolhem um bandicoot chamado Crash para ser o general de seu exército de animais-soldados. No entanto, Cortex decide fazer um teste inicial em um ainda não totalmente funcional Vórtice Cortex, a máquina que detém o Evolvo-Ray, apesar de seu assistente alertar que o Vórtice não está pronto. Cortex testa Crash na máquina, mas o experimento falha e o Vórtice o rejeita; Crash aproveita o momento para escapar pela janela e acaba caindo em mar aberto. Cortex mantém Tawna, outra bandicoot, como sua próxima cobaia. Tendo se apegado a Tawna durante o cativeiro, Crash faz uma longa jornada para resgatá-la e derrotar Cortex.")

    with col2:
        st.image("src/assets/Donkey_Kong_Country.jpg")
