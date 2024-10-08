import streamlit as st

st.title(':blue[𝐒𝐞𝐜̧𝐚̃𝐨 𝟏]')

st.title('Dimensionamento de um transformador monofásico')
st.markdown('Escrever alguma coisa aqui pra ficar bonitin')
st.divider()

st.subheader('Tensão Primária')
Vp = st.number_input("Informe a Tensão Primária **(Vp)** em Volts", format='%0.2f')

st.subheader('Tensão Secundária')
Vs = st.number_input("Informe a Tensão Secundária **(Vs)** em Volts", format='%0.2f')

st.subheader('Potência da Carga')
potencia = st.number_input("Informe a Potência da carga em Watts", format='%0.2f')

st.divider()
st.subheader('Dados de Entrada')
st.write('• 𝐀 𝐓𝐞𝐧𝐬𝐚̃𝐨 𝐏𝐫𝐢𝐦𝐚́𝐫𝐢𝐚 𝐞́ ', Vp, '𝐕𝐨𝐥𝐭𝐬')
st.write('• 𝐀 𝐓𝐞𝐧𝐬𝐚̃𝐨 𝐒𝐞𝐜𝐮𝐧𝐝𝐚́𝐫𝐢𝐚 𝐞́ ', Vs, '𝐕𝐨𝐥𝐭𝐬')
st.write('• 𝐀 𝐏𝐨𝐭𝐞̂𝐧𝐜𝐢𝐚 𝐝𝐚 𝐂𝐚𝐫𝐠𝐚 𝐞́ ', potencia, '𝐖𝐚𝐭𝐭𝐬')
st.write('')

if (st.button('Gerar Resultado')):
    st.subheader('Número de Espiras no Primário (Np) e no Secundário (Ns)')

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
