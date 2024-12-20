import streamlit as st
import pandas as pd
from pathlib import Path
from PIL import Image

# Configurar a página para o modo amplo
img = Image.open("TMS logo.png")
st.set_page_config(layout="wide", page_title="Cardápio TMS",page_icon=img)

# Carregar os dados do arquivo Excel
def carregar_dados(caminho):
    dados = pd.read_excel(caminho)
    return dados

# Função para filtrar os dados
def filtrar_dados(dados, modelo, Processador, tela_intervalo, Digital,Ethernet, Peso_intervalo,RAM_intervalo, Bateria_intervalo, HD_intervalo,Foco, SO):
    if modelo:
        dados = dados[dados['Modelo'].isin(modelo)]
    if Processador:
        dados = dados[dados['Processador'].isin(Processador)]
    if tela_intervalo:
        dados = dados[dados['Tela'].between(tela_intervalo[0], tela_intervalo[1])]
    if Digital:
        dados = dados[dados['Digital'] == "Sim"]
    if Ethernet:
        dados = dados[dados['Ethernet'] == "Sim"]
    if Peso_intervalo:
        dados = dados[dados['Peso(Kg)'].between(Peso_intervalo[0], Peso_intervalo[1])]
    if RAM_intervalo:
        dados = dados[dados['RAM (GB)'].between(RAM_intervalo[0], RAM_intervalo[1])]
    if Bateria_intervalo:
        dados = dados[dados['Bateria (Wh)'].between(Bateria_intervalo[0], Bateria_intervalo[1])]
    if HD_intervalo:
        dados = dados[dados['Armazenamento Interno (GB)'].between(HD_intervalo[0], HD_intervalo[1])]
    if Foco:
        dados = dados[dados['Foco'] == "B2B"]
    if SO:
        dados = dados[dados['Sistema Operacional'].isin(SO)]
    return dados


# Carregar o dataset
pasta_arquivo = pasta_datasets = Path(__file__).parent.parent
caminho_arquivo_tab = pasta_arquivo / 'cardapio_tms_notebook.xlsx'
df_tab = carregar_dados(caminho_arquivo_tab)

# Sidebar - Filtros
st.sidebar.header('Filtros')
modelo_filtro = st.sidebar.multiselect('Modelo', df_tab['Modelo'].unique())
SO_filtro = st.sidebar.multiselect('Sistema Operacional', df_tab['Sistema Operacional'].unique())
Processador_filtro = st.sidebar.multiselect('Processador', df_tab['Processador'].unique())
Digital_filtro = st.sidebar.checkbox('Digital')
Ethernet_filtro = st.sidebar.checkbox('Ethernet')
#B2B_filtro = st.sidebar.checkbox('Foco')
tela_filtro = st.sidebar.select_slider('Tela', options=sorted(df_tab['Tela'].unique()), value=(min(df_tab['Tela']), max(df_tab['Tela'])))
#ano_Filtro = st.sidebar.select_slider('Lançamento', options=sorted(df_tab['Lançamento'].unique()), value=(min(df_tab['Lançamento']), max(df_tab['Lançamento'])))
HD_Filtro = st.sidebar.select_slider('Armazenamento Interno (GB)', options=sorted(df_tab['Armazenamento Interno (GB)'].unique()), value=(min(df_tab['Armazenamento Interno (GB)']), max(df_tab['Armazenamento Interno (GB)'])))
RAM_filtro = st.sidebar.select_slider('RAM (GB)', options=sorted(df_tab['RAM (GB)'].unique()), value=(min(df_tab['RAM (GB)']), max(df_tab['RAM (GB)'])))
bateria_filtro = st.sidebar.select_slider('Bateria (Wh)', options=sorted(df_tab['Bateria (Wh)'].unique()), value=(min(df_tab['Bateria (Wh)']), max(df_tab['Bateria (Wh)'])))
#situacao_filtro = st.sidebar.multiselect('Situação', df_tab['Situação'].unique())
peso_filtro = st.sidebar.select_slider('Peso(Kg)', options=sorted(df_tab['Peso(Kg)'].unique()), value=(min(df_tab['Peso(Kg)']), max(df_tab['Peso(Kg)'])))

# Filtrar os dados com base nas seleções
df_filtrado_tab = filtrar_dados(df_tab, 
                                modelo_filtro, 
                                Processador=Processador_filtro, 
                                tela_intervalo=tela_filtro, 
                                Digital=Digital_filtro, 
                                Ethernet=Ethernet_filtro, 
                                Peso_intervalo=peso_filtro, 
                                RAM_intervalo=RAM_filtro, 
                                Bateria_intervalo=bateria_filtro, 
                                HD_intervalo=HD_Filtro, 
                                Foco=None, 
                                SO=SO_filtro)

# Mostrar os dados no app

st.markdown("""
<div style="text-align: center;">
    <h1>Cardápio TMS - Notebook</h1>
</div>
""", unsafe_allow_html=True)

st.write(df_filtrado_tab)