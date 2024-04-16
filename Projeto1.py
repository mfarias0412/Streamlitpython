import streamlit as st
import pandas as pd

st.set_page_config(page_title="Primeiro Site  do Márcinho")

with st.container():
     st.subheader("Meu Primeiro site com Márcinho")
     st.title("Dashboard de Contratos")
     st.write("Informações Sobre os contratatos fechados no mês de Maio")
     st.write("Quer ver as noticias do Mengão? [Clique aqui](https://ge.globo.com/futebol/times/flamengo/)")

@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("resultados.csv")
    return tabela

with st.container():
     st.write("---")
     qtde_dias = st.selectbox("Selecione o Período", ["7Dias", "15Dias", "21Dias", "30 Dias"])
     num_dias = int(qtde_dias.replace("Dias", ""))
     dados = carregar_dados()
     dados = dados[-num_dias:]
     st.area_chart(dados, x="Data", y="Contratos")

