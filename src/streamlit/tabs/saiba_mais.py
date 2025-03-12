import streamlit as st
from utils import *

def tab_saiba_mais():
    st.markdown(
        """
        ### Saiba mais  
        A _pysentimiento_ é uma biblioteca que suporta algumas tarefas de PLN em quatro línguas: Espanhol, Inglês, Italiano e Português. A biblioteca tem como referência o artigo [pysentimiento: A Python Toolkit for Sentiment Analysis in Spanish, English, Italian and Portuguese](https://doi.org/10.48550/arXiv.2106.09462).     
        """
    )

    with st.expander("**Cite o artigo (BibTeX)**", expanded=False):
        st.code(language='latex', body="""
        @article{DBLP:journals/corr/abs-2106-09462,
            author       = {Juan Manuel P{\'{e}}rez and
                            Juan Carlos Giudici and
                            Franco M. Luque},
            title        = {pysentimiento: {A} Python Toolkit for Sentiment Analysis and SocialNLP
                            tasks},
            journal      = {CoRR},
            volume       = {abs/2106.09462},
            year         = {2021},
            url          = {https://arxiv.org/abs/2106.09462},
            eprinttype    = {arXiv},
            eprint       = {2106.09462},
            timestamp    = {Tue, 29 Jun 2021 16:55:04 +0200},
            biburl       = {https://dblp.org/rec/journals/corr/abs-2106-09462.bib},
            bibsource    = {dblp computer science bibliography, https://dblp.org}
            }
        """)

    st.markdown(
        """
        A biblioteca suporta as seguintes tarefas e línguas:
        | Tarefa                        | Línguas                               |  
        |:---------------------         |:--------------------------------------|  
        | Análise de Sentimentos        | es, en, it, pt                        |  
        | Detecção de Discurso de Ódio  | es, en, it, pt                        |  
        | Detecção de Ironia            | es, en, it, pt                        |  
        | Análise de Emoções            | es, en, it, pt                        |  
        | NER & POS tagging             | es, en                                |  
        """
    )

    st.caption("Tarefas e línguas suportadas. Tabela traduzida de [Supported tasks | pysentimiento](https://github.com/pysentimiento/pysentimiento/blob/master/docs/TASKS.md#supported-tasks)")
    
    st.markdown(
        """
        Para cada tarefa e língua, os autores utilizaram diferentes datasets, o que acarreta em diferenças nos modelos.  
        Os resultados para Português estão apresentados na tabela abaixo. Os resultados são expressos como a porcentagem da média do Macro F1 +/- o desvio padrão.
        | Modelo       | Sentimento      | Emoção     | Discurso de Ódio  |  
        |:-------------|:------------    |:-----------|:--------------    |  
        | BERT-pt      | 70.0 +- 0.3     | 44.4 +- 0.6| 64.1 +- 1.1       |  
        | BERTabaporu  | 73.8 +- 0.4     | 43.9 +- 0.5| **70.3 +- 3.3**   |  
        | BERTweet-BR  | **75.3 +- 0.5** | 43.2 +- 1.1| 55.6 +- 5.5       |  
        | RoBERTuito   | 71.7 +- 0.4     | 45.2 +- 0.6| 70.0 +- 2.4       |  
        """
    )

    st.caption("Resultados para o Português. Tabela traduzida de [Results | pysentimiento](https://github.com/pysentimiento/pysentimiento/blob/master/docs/TASKS.md#results)")

    logo_lamid()