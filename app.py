# importando bibliotecas
import pandas as pd
import streamlit as st
import plotly.express as px

# importando base de dados
def load_data():
    df = pd.read_csv("Ecommerce_DBS.csv")
    return df

df = load_data()
st.write(df)