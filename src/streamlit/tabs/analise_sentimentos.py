from pysentimiento import create_analyzer
import streamlit as st

@st.cache_resource
def load_pysentimiento_analyzer():
    return create_analyzer(task="sentiment", lang="pt")

def analisador(texto):
    analyzer = load_pysentimiento_analyzer()
    return analyzer.predict(texto)

def tab_analise_sentimentos():
    st.markdown("### Análise de Sentimentos")
    st.markdown("Insira o texto na caixa abaixo e clique no botão 'Analisar' para obter a análise de sentimentos.")
    texto = st.text_area("Texto", placeholder="Insira o texto aqui...", height=70)
    if st.button("Analisar"):
        resultado = analisador(texto)
        with st.container(border=True):
            st.markdown("### Resultado")
            st.table(
                {
                    "**Polaridade**": [resultado.output],
                    "**Positiva**": [resultado.probas['POS']],
                    "**Neutra**": [resultado.probas['NEU']],
                    "**Negativa**": [resultado.probas['NEG']]
                }
            )
