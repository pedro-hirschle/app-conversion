import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

if 'transformer_challenge' not in st.session_state:
    st.session_state['transformer_challenge'] = False

st.title(':blue[𝐒𝐞𝐜̧𝐚̃𝐨 𝟒]')
st.title('Cálculo da regulação do transformador')
st.markdown('A regulação do transformador é uma medida que indica a variação percentual na tensão secundária de um transformador quando ele passa da condição de vazio (sem carga) para a condição de carga nominal.')

with st.form(key='input_form'):
    st.subheader('Insira os Parâmetros do Transformador e da Carga')
    
    s_transformador = st.number_input('Potência Nominal do Transformador (kVA)', min_value=1.0, value=200.0, step=1.0)
    v_primario = st.number_input('Tensão Nominal Primária (kV)', min_value=0.1, value=20.0, step=0.1)
    v_secundario = st.number_input('Tensão Nominal Secundária (kV)', min_value=0.1, value=2.4, step=0.1)
    z_eq_real = st.number_input('Resistência Equivalente (Ohms)', min_value=0.0, value=0.28, step=0.01)
    z_eq_imag = st.number_input('Reatância Equivalente (Ohms)', min_value=0.0, value=1.0, step=0.01)
    
    s_carga = st.number_input('Potência da Carga (kVA)', min_value=1.0, value=180.0, step=1.0)
    fp_carga = st.number_input('Fator de Potência da Carga (0 a 1)', min_value=0.0, max_value=1.0, value=1.0, step=0.01)
    
    submit_button = st.form_submit_button(label='Gerar Resultado')

if submit_button or st.session_state['transformer_challenge']:
    st.session_state['transformer_challenge'] = True
    st.session_state['s_transformador'], st.session_state['v_primario'], st.session_state['v_secundario'] = s_transformador, v_primario, v_secundario
    st.session_state['z_eq_real'], st.session_state['z_eq_imag'], st.session_state['s_carga'], st.session_state['fp_carga'] = z_eq_real, z_eq_imag, s_carga, fp_carga

    st.divider()
    st.subheader('Cálculos Detalhados')

    s_carga = st.session_state['s_carga'] * 1e3  # kVA -> VA
    v_secundario = st.session_state['v_secundario'] * 1e3  # kV -> V
    z_eq = complex(st.session_state['z_eq_real'], st.session_state['z_eq_imag'])  # impedância como num complexo

    # corrente da carga
    i_carga = s_carga / v_secundario
    i_carga = i_carga * (st.session_state['fp_carga'] + 1j * np.sqrt(1 - st.session_state['fp_carga']**2))

    queda_tensao = i_carga * z_eq

    # tensão em carga
    v_full_load = v_secundario - abs(queda_tensao)

    v_no_load = v_secundario
    regulacao = ((v_no_load - v_full_load) / v_full_load) * 100

    st.write('Agora vamos detalhar os cálculos usando os valores inseridos:')

    st.latex(f'I_{{\text{{carga}}}} = \\frac{{{s_carga:.2f}}}{{{v_secundario:.2f}}} = {i_carga:.2f} \\text{{ A}}')
    st.latex(f'\\Delta V = I_{{\text{{carga}}}} \\times Z_{{\text{{eq}}}} = ({i_carga:.2f}) \\times ({z_eq.real} + j{z_eq.imag}) = {queda_tensao:.2f} \\text{{ V}}')
    st.latex(f'V_{{\text{{FL}}}} = V_{{\text{{secundário}}}} - |\\Delta V| = {v_secundario:.2f} - {abs(queda_tensao):.2f} = {v_full_load:.2f} \\text{{ V}}')
    st.latex(f'\\text{{Regulação}} = \\frac{{{v_no_load:.2f} - {v_full_load:.2f}}}{{{v_full_load:.2f}}} \\times 100\\% = {regulacao:.2f}\\%')

    st.subheader('Resultado da Regulação do Transformador')
    st.write(f'**Regulação do Transformador:** {regulacao:.2f}%')
    if regulacao < 1:
        st.success("**Avaliação:** Excelente. O transformador mantém a tensão praticamente constante sob carga.")
    elif 1 <= regulacao < 3:
        st.success("**Avaliação:** Muito Bom. A variação de tensão é quase imperceptível para a maioria das aplicações.")
    elif 3 <= regulacao < 5:
        st.warning("**Avaliação:** Bom. A variação de tensão é aceitável para a maioria das aplicações comerciais e industriais.")
    elif 5 <= regulacao < 10:
        st.warning("**Avaliação:** Razoável. A variação de tensão é mais perceptível, mas ainda tolerável em situações não críticas.")
    elif 10 <= regulacao < 15:
        st.error("**Avaliação:** Ruim. A variação de tensão é alta e pode afetar equipamentos sensíveis.")
    else:
        st.error("**Avaliação:** Inaceitável. A regulação é muito alta, indicando que o transformador não é adequado para a maioria das aplicações.")

    ## ------------------ diagrama fasorial ------------------ ##
    fig, ax = plt.subplots()
    ax.quiver(0, 0, np.real(i_carga), np.imag(i_carga), angles='xy', scale_units='xy', scale=1, color='r', label='Corrente')
    ax.quiver(0, 0, np.real(queda_tensao), np.imag(queda_tensao), angles='xy', scale_units='xy', scale=1, color='b', label='Queda de Tensão')
    ax.quiver(0, 0, v_secundario, 0, angles='xy', scale_units='xy', scale=1, color='g', label='Tensão Secundária')

    plt.xlim(-v_secundario * 0.5, v_secundario * 1.5)
    plt.ylim(-v_secundario * 0.5, v_secundario * 0.5)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.title('Diagrama Fasorial do Transformador')
    plt.xlabel('Parte Real (V)')
    plt.ylabel('Parte Imaginária (V)')
    plt.legend()
    st.pyplot(fig)
