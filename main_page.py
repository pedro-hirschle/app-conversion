import streamlit as st

st.image('introduction_page/models/logo.jpg')
st.title('Plataforma de Suporte para Projetos de Transformadores')
st.divider()

pg = st.navigation([
     st.Page('introduction_page/introduction_page.py', title='Introdução', icon='ℹ️'),
     st.Page('challenge1_page/challenge1_page.py', title='Desafio 1', icon='1️⃣'),
     st.Page('challenge2_page/challenge2.py', title='Desafio 2', icon='2️⃣'),
     st.Page('challenge3_page/challenge3_page.py', title='Desafio 3', icon='3️⃣'),
     st.Page('credits_page/credits_page.py', title='Créditos', icon='©️')
])

pg.run()