from tabs.analise_sentimentos import tab_analise_sentimentos
#from tabs.saiba_mais import tab_saiba_mais
import streamlit as st

st.title("ASPBr")
st.markdown("> Análise de Sentimentos e Polaridades para o Português Brasileiro")
st.markdown("O ASPBr é uma aplicação web que permite realizar a tarefa de análise de sentimentos de textos em português utilizando a biblioteca [_pysentimiento_](https://github.com/pysentimiento/pysentimiento) (Informações sobre a biblioteca estão na aba **'Saiba mais'**).")

tab1, tab2 = st.tabs(["Análise de Sentimentos", "Saiba mais"])

with tab1:
    tab_analise_sentimentos()

    