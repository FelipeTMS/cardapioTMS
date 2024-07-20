import streamlit as st
import pandas as pd
from pathlib import Path

# Configurar a página para o modo amplo
st.set_page_config(layout="wide", page_title="teste")

# Carregar os dados do arquivo Excel
def carregar_dados(caminho):
    dados = pd.read_excel(caminho)
    return dados

# Função para filtrar os dados
def filtrar_dados(dados, marca, nome_comercial, tela_intervalo, _5g,Ano_intervalo,RAM_intervalo, Bateria_intervalo, HD_intervalo, situacao):
    if marca:
        dados = dados[dados['Marca'].isin(marca)]
    if nome_comercial:
        dados = dados[dados['Nome comercial'].isin(nome_comercial)]
    if tela_intervalo:
        dados = dados[dados['Tela'].between(tela_intervalo[0], tela_intervalo[1])]
    if _5g:
        dados = dados[dados['5G'] == "S"]
    if Ano_intervalo:
        dados = dados[dados['Lançamento'].between(Ano_intervalo[0], Ano_intervalo[1])]
    if RAM_intervalo:
        dados = dados[dados['RAM (GB)'].between(RAM_intervalo[0], RAM_intervalo[1])]
    if Bateria_intervalo:
        dados = dados[dados['Bateria (mAh)'].between(Bateria_intervalo[0], Bateria_intervalo[1])]
    if HD_intervalo:
        dados = dados[dados['Armazenamento Interno'].between(HD_intervalo[0], HD_intervalo[1])]
    if situacao:
        dados = dados[dados['Situação'].isin(situacao)]
    return dados


# Carregar o dataset
pasta_arquivo = pasta_datasets = Path(__file__).parent.parent
caminho_arquivo_tab = pasta_arquivo / 'cardapio_tms_tablet.xlsx'
df_tab = carregar_dados(caminho_arquivo_tab)

# Sidebar - Filtros
st.sidebar.header('Filtros')
marca_filtro = st.sidebar.multiselect('Marca', df_tab['Marca'].unique())
nome_comercial_filtro = st.sidebar.multiselect('Nome comercial', df_tab['Nome comercial'].unique())
_5g_filtro = st.sidebar.checkbox('5G')
tela_filtro = st.sidebar.select_slider('Tela', options=sorted(df_tab['Tela'].unique()), value=(min(df_tab['Tela']), max(df_tab['Tela'])))
ano_Filtro = st.sidebar.select_slider('Lançamento', options=sorted(df_tab['Lançamento'].unique()), value=(min(df_tab['Lançamento']), max(df_tab['Lançamento'])))
RAM_filtro = st.sidebar.select_slider('RAM (GB)', options=sorted(df_tab['RAM (GB)'].unique()), value=(min(df_tab['RAM (GB)']), max(df_tab['RAM (GB)'])))
bateria_filtro = st.sidebar.select_slider('Bateria (mAh)', options=sorted(df_tab['Bateria (mAh)'].unique()), value=(min(df_tab['Bateria (mAh)']), max(df_tab['Bateria (mAh)'])))
HD_Filtro = st.sidebar.select_slider('Armazenamento Interno', options=sorted(df_tab['Armazenamento Interno'].unique()), value=(min(df_tab['Armazenamento Interno']), max(df_tab['Armazenamento Interno'])))
situacao_filtro = st.sidebar.multiselect('Situação', df_tab['Situação'].unique())

# Filtrar os dados com base nas seleções
df_filtrado_tab = filtrar_dados(df_tab, marca_filtro, nome_comercial_filtro, tela_filtro, _5g_filtro, ano_Filtro, RAM_filtro, bateria_filtro, HD_Filtro  ,situacao_filtro)

# Mostrar os dados no app
st.write(df_filtrado_tab)