import streamlit as st

if 'challenge1' not in st.session_state:
    st.session_state['challenge1'] = False
    st.session_state['challenge1_Vp'] = 0.00
    st.session_state['challenge1_Vs'] = 0.00
    st.session_state['challenge1_potencia'] = 0.00

st.title(':blue[𝐒𝐞𝐜̧𝐚̃𝐨 𝟏]')

st.title('Dimensionamento de um transformador monofásico')
st.markdown('O dimensionamento de um transformador monofásico serve para garantir que o equipamento seja capaz de atender às necessidades específicas de um sistema elétrico, operando com segurança e eficiência. Esse processo envolve calcular as capacidades elétricas adequadas.')
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader('𝐃𝐚𝐝𝐨𝐬 𝐝𝐞 𝐞𝐧𝐭𝐫𝐚𝐝𝐚')
    st.markdown('• Tensão Primária Vp em Volts')
    st.markdown('• Tensão Secundária Vs em Volts')
    st.markdown('• Potência da carga em VA ou W')
with col2:
    st.subheader('𝐃𝐚𝐝𝐨𝐬 𝐝𝐞 𝐬𝐚𝐢́𝐝𝐚')
    st.markdown('• Número de Espiras do Enrolamento Primário e Secundário')
    st.markdown('• Bitola do cabo primário e do cabo secundário')
    st.markdown('• Tipo de lâmina e quantidade')
    st.markdown('• Dimensões do transformador: Núcleo e dimensões finais, peso.')

st.divider()

st.title('Dados de entrada')

with st.form('challenge1_form'):

    st.subheader('Tensão Primária')
    Vp = st.number_input("Informe a Tensão Primária **(Vp)** em Volts", value = st.session_state['challenge1_Vp'])

    st.subheader('Tensão Secundária')
    Vs = st.number_input("Informe a Tensão Secundária **(Vs)** em Volts", value = st.session_state['challenge1_Vs'])

    st.subheader('Potência da Carga')
    potencia = st.number_input("Informe a Potência da carga em Watts", value = st.session_state['challenge1_potencia'])

    if (st.form_submit_button('Gerar Resultado') or st.session_state['challenge1']):
        st.session_state['challenge1'] = True
        st.session_state['challenge1_Vp'], st.session_state['challenge1_Vs'], st.session_state['challenge1_potencia'] = Vp, Vs, potencia

        st.divider()
        st.subheader('Número de Espiras no Primário e Secundário')

        st.write('Primeiramente, vamos encontrar a quantidade de espiras no primário e secundário do transformador. Para isso, temos as seguintes informações:')
        st.latex(f'Vp = {Vp} V')
        st.latex(f'Vs = {Vs} V')
        st.latex(f'Potência = {potencia} W')
        
        st.write('Agora vamos calcular o valor da corrente no primário e secundário:')
        Ip, Is = (potencia / Vp), (potencia / Vs)
        st.latex(fr'Ip = \frac{{{potencia}}}{{{Vp}}} = {{{Ip}}}')
        st.latex(fr'Is = \frac{{{potencia}}}{{{Vs}}} = {{{Is}}}')

        st.latex(fr'{{{Vp}}} \cdot Ns - {{{Vs}}} \cdot Np = 0')
        st.latex(fr'{{{Is}}} \cdot Ns - {{{Ip}}} \cdot Np = 0')

        st.latex(fr'Ns = \frac{{{Vs}}}{{{Vp}}} \cdot Np')
        st.latex(fr'{{{Is}}} \cdot \frac{{{Vs}}}{{{Vp}}} \cdot Np - {{{Ip}}} \cdot Np = 0')
