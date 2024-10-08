import streamlit as st

st.title('Créditos')

st.markdown('Esse projeto foi desenvolvido por uma equipe de estudantes de Engenharia de Computação da Universidade de Pernambuco (UPE) com propósito educacional sobre transformadores e eletromagnetismo.')

st.divider()
st.subheader('Time de Desenvolvimento')

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image('credits/models/carlos.jpg', caption='Carlos Eduardo')
    st.page_link('https://www.linkedin.com/in/carlos-eduh/', label='___𝐋𝐢𝐧𝐤𝐞𝐝𝐢𝐧', icon='🔗')

with col2:
    st.image('credits/models/george.jpg', caption='George Vieira')
    st.page_link('https://www.linkedin.com/in/george-vieira-nrb/', label='___𝐋𝐢𝐧𝐤𝐞𝐝𝐢𝐧', icon='🔗')

with col3:
    st.image('credits/models/pedro.jpg', caption='Pedro Hirschle')
    st.page_link('https://www.linkedin.com/in/pedro-hirschle/', label='___𝐋𝐢𝐧𝐤𝐞𝐝𝐢𝐧', icon='🔗')

with col4:
    st.image('credits/models/riquelme.jpg', caption='Riquelme Lopes')
    st.page_link('https://www.linkedin.com/in/riquelme-lopes-575435132/', label='___𝐋𝐢𝐧𝐤𝐞𝐝𝐢𝐧', icon='🔗')

st.divider()
st.subheader('Professor Responsável')

st.image('credits/models/professor.jpg', caption='Raimundo Lima')
st.page_link('https://www.linkedin.com/in/raimundo-lima-697b6335/', label='___𝐋𝐢𝐧𝐤𝐞𝐝𝐢𝐧', icon='🔗')

st.divider()
st.subheader('Instituição de Ensino')

col1, col2, col3 = st.columns(3)

with col1:
    st.image('credits/models/upe.png')

with col2:
    st.image('credits/models/poli.png')

with col3:
    st.image('credits/models/ecomp.png')