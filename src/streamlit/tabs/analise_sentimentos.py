from pysentimiento import create_analyzer
from utils import *
import streamlit as st
import pandas as pd
from io import StringIO

@st.cache_resource
def load_pysentimiento_analyzer():
    return create_analyzer(task="sentiment", lang="pt")


def read_planilha(arquivo):
    """
    Centraliza a leitura do arquivo a partir da extensão
    de arquivo utilizada.
    """
    extensao = arquivo.name.split('.')
    if extensao[1] == "csv":
        return pd.read_csv(arquivo)
    else:
        return pd.read_excel(arquivo)


def analisador(texto):
    """
    Realiza a análise de sentimentos a partir da pysentimiento.
    """
    analyzer = load_pysentimiento_analyzer()
    return analyzer.predict(texto)

def upload_arquivo():
    """
    Gerencia os arquivos inseridos e exibe um dataframe.
    """
    arquivo = st.file_uploader(label ="upload_planilhas",
                                type = ["csv", "xls", "xlsx", "ods"],
                                label_visibility = "collapsed")
    if arquivo is not None:
        dataframe = read_planilha(arquivo)
        st.dataframe(dataframe)

def tab_analise_sentimentos():
    """
    Aba de análise de sentimentos.
    """
    st.markdown("### Análise de Sentimentos")
    st.markdown("Insira o texto na caixa abaixo e clique no botão **Analisar** para obter a análise de sentimentos.")
    texto = st.text_area("Texto", placeholder="Insira o texto a ser analisado...", height=70)
    if st.button("Analisar"):
        resultado = analisador(texto)
        with st.container(border=True):
            st.markdown("#### Resultado")
            st.markdown("A `Polaridade` indica qual é o sentimento predominante no texto e as colunas `'Positiva'`, `'Neutra'`, e `'Negativa'` indicam qual a probabilidade do texto possuir a respectiva polaridade.")
            st.table(
                {
                    "**Polaridade**": [resultado.output],
                    "**Positiva**": [resultado.probas['POS']],
                    "**Neutra**": [resultado.probas['NEU']],
                    "**Negativa**": [resultado.probas['NEG']]
                }
            )
    st.markdown("Ou insira uma planilha abaixo")
    upload_arquivo()
    logo_lamid()
    