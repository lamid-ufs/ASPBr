from pysentimiento import create_analyzer
from utils import *
import streamlit as st
import pandas as pd
from io import StringIO

@st.cache_resource
def load_pysentimiento_analyzer():
    return create_analyzer(task="sentiment", lang="pt")

@st.dialog("Planilha inválida!")
def erro(tipo):
    if tipo == "VAZIA":
        mensagem = "certifique-se de que a planilha inserida possui dados"
    if tipo == "NULOS":
        mensagem = "Não é possível analisar a planilha: existem células nulas/vazias no arquivo"
    st.error(mensagem,
             icon=":material/quick_reference:")
    
    if st.button("Ok"):
        st.cache_data.clear()
        del st.session_state.arquivo_lido
        st.rerun()

@st.dialog("### Resultado", width = large)
def analisador_coluna(resultados):

    with st.container(border=True):
        st.markdown("#### Resultado")
        st.markdown("A `Polaridade` indica qual é o sentimento predominante no texto e as colunas `'Positiva'`, `'Neutra'`, e `'Negativa'` indicam qual a probabilidade do texto possuir a respectiva polaridade.")
        
        for resultado in resultados:
            st.table(
                {
                    #"**Polaridade**": [resultado.output],
                    "**Positiva**": [resultado.probas['POS']],
                    "**Neutra**": [resultado.probas['NEU']],
                    "**Negativa**": [resultado.probas['NEG']]
                }
            )

def carregamento():
    estado = False
    while not estado:
        analisador()
        st.spinner("Analisando...")
    


@st.dialog("Análise de colunas", width = "large")
def seletor(colunas, dataframe):
    coluna = st.selectbox(
            "Que coluna você deseja analisar?",
            colunas,
            index=None,
            placeholder="Selecione a coluna desejada...",
        )
    
    if st.button("Analisar",
                 key = 'analise_coluna',
                 help = "Clique para analisar as emoções da coluna selecionada",
                 on_click = carregamento()):
        valores = dataframe[coluna].tolist()

        
    
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

def extrator_colunas(arquivo):
    """
    Transforma um arquivo em dataframe e retorna um seletor de
    suas colunas.
    """
    if arquivo is not None:
        dataframe = read_planilha(arquivo)
        
        if dataframe.isnull().values.any():
            erro("NULOS")

        colunas = dataframe.columns

        if not colunas.empty:
            seletor(colunas, dataframe)
        else:
            erro("VAZIA")
            

def analisador(texto):
    """
    Realiza a análise de sentimentos a partir da pysentimiento.
    """
    analyzer = load_pysentimiento_analyzer()
    return True, analyzer.predict(texto)

def upload_arquivo():
    """
    Gerencia os arquivos inseridos e exibe um dataframe.
    """
    
    arquivo = st.file_uploader(label ="upload_planilhas",
                                key = f"arquivo_lido",
                                type = ["csv", "xls", "xlsx", "ods"],
                                label_visibility = "collapsed")
    extrator_colunas(arquivo)

def tab_analise_sentimentos():
    """
    Aba de análise de sentimentos.
    """
    st.markdown("### Análise de Sentimentos")
    st.markdown("Insira o texto na caixa abaixo e clique no botão **Analisar** para obter a análise de sentimentos.")
    texto = st.text_area("Texto", placeholder="Insira o texto a ser analisado...", height=70)
    if st.button("Analisar"):
        _, resultado = analisador(texto)
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
    