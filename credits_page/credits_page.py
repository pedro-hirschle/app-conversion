import streamlit as st

st.title('Créditos')

st.markdown('Esse projeto foi desenvolvido por uma equipe de estudantes de Engenharia de Computação da Universidade de Pernambuco (UPE) com propósito educacional sobre transformadores e eletromagnetismo.')

st.divider()
st.subheader('Time de Desenvolvimento')

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image('credits_page/models/carlos.jpg')
    st.markdown('**Carlos Eduardo**')
    st.page_link('https://www.linkedin.com/in/carlos-eduh/', label='Linkedin', icon='✅')

with col2:
    st.image('credits_page/models/george.jpg')
    st.markdown('**George Vieira**')
    st.page_link('https://www.linkedin.com/in/george-vieira-nrb/', label='Linkedin', icon='✅')

with col3:
    st.image('credits_page/models/pedro.jpg')
    st.markdown('**Pedro Hirschle**')
    st.page_link('https://www.linkedin.com/in/pedro-hirschle/', label='Linkedin', icon='✅')

with col4:
    st.image('credits_page/models/riquelme.jpg')
    st.markdown('**Riquelme Lopes**')
    st.page_link('https://www.linkedin.com/in/riquelme-lopes-575435132/', label='Linkedin', icon='✅')

st.divider()
st.subheader('Professor Responsável')

st.image('credits_page/models/professor.jpg')
st.markdown('**Raimundo Lima**')
st.page_link('https://www.linkedin.com/in/raimundo-lima-697b6335/', label='Linkedin', icon='✅')

st.divider()
st.subheader('Instituição de Ensino')

col1, col2, col3 = st.columns(3)

with col1:
    st.image('credits_page/models/upe.png')

with col2:
    st.image('credits_page/models/poli.png')

with col3:
    st.image('credits_page/models/ecomp.png')