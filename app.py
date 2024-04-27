import pandas as pd
import datetime
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

st.title('Demonstrativo das vendas no mês de Dezembro de 2019')

df = pd.read_excel('Vendas.xlsx')
min_date = datetime.date(2019, 12, 1)
max_date = datetime.date(2019, 12, 25)

st.divider()

st.sidebar.title('Filtrar por Data')
d = st.sidebar.date_input(
    'Período de Dezembro', (min_date, max_date))

d_inicio = pd.to_datetime(d[0])
d_fim = pd.to_datetime(d[1])

d_filtro = df[(df["Data"] >= d_inicio) & (df["Data"] <= d_fim)]
st.sidebar.write('Seu filtro é: ', d_filtro)


fig = px.bar(d_filtro, x='ID Loja', y='Quantidade', color='Produto',
             title='Gráfico da quantidade de produtos vendidos por loja')
fig

st.divider()

fig2 = px.bar(d_filtro, x='Data', y='Valor Final',
              title='Gráfico de receita por dia')
fig2

st.divider()
