# Importando as bibliotecas necessárias
import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo os dados do arquivo CSV
car_data = pd.read_csv('vehicles.csv')  # Substitua pelo caminho correto do seu arquivo CSV

# Criando o título do aplicativo
st.header("Análise de Vendas de Veículos")

# Exibindo uma amostra dos dados
st.write("Visualizando os primeiros dados do conjunto:")
st.write(car_data.head())

# Criando um botão para gerar o histograma
hist_button = st.button('Criar histograma')

# Se o botão for clicado, cria um histograma
if hist_button:
    st.write('Criando um histograma para a coluna odometer')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Criando um botão para gerar o gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

# Se o botão for clicado, cria o gráfico de dispersão
if scatter_button:
    st.write('Criando um gráfico de dispersão entre preço e ano do veículo')
    fig_scatter = px.scatter(car_data, x="model_year", y="price", color="condition")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Desafio opcional: Substituindo botões por caixas de seleção
st.write("Desafio: Use as caixas de seleção abaixo para gerar gráficos")
build_histogram = st.checkbox('Criar um histograma')
build_scatter = st.checkbox('Criar gráfico de dispersão')

# Verifica se a caixa de seleção do histograma foi marcada
if build_histogram:
    st.write('Criando um histograma para a coluna odometer')
    fig_hist_checkbox = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist_checkbox, use_container_width=True)

# Verifica se a caixa de seleção do gráfico de dispersão foi marcada
if build_scatter:
    st.write('Criando um gráfico de dispersão entre preço e ano do veículo')
    fig_scatter_checkbox = px.scatter(car_data, x="model_year", y="price", color="condition")
    st.plotly_chart(fig_scatter_checkbox, use_container_width=True)
