import streamlit as st 
import pandas as pd 
import plotly.express as px

st.header("Dashboard de Análise de Carros")

car_data = pd.read_csv('vehicles.csv')

# Botão para histograma
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para histograma (alternativa)
build_histogram = st.checkbox('Criar um histograma')

if build_histogram:
    st.write('Criando um histograma para a coluna odometer')
    fig1 = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão para odometer vs preço')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
