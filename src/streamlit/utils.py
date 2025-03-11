import streamlit as st

def logo_lamid():
    st.divider()
    colunas = st.columns([3, 0.5])
    colunas[0].image('src/streamlit/imgs/lamid-logo-full.png', width=150)
    colunas[1].caption("Desenvolvido por:<br>Túlio Gois & Nayla Chagas", unsafe_allow_html=True)
    