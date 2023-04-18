
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

def crear_pagina():
    st.write("¡Esta es mi página de Streamlit!")


df2 = pd.read_csv('data/PREDICCIÓN.csv')

# Calcular la cantidad de jugadores que llegaron a la NBA y los que no
nba_count = df2[df2['NBA'] == 'Sí'].shape[0]
no_nba_count = df2[df2['NBA'] == 'No'].shape[0]

# PIE CHART
fig1, ax1 = plt.subplots(figsize=(6, 6))
labels = ['Sí', 'No']
sizes = [nba_count, no_nba_count]
colors = ['#FFA07A', '#87CEEB']
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax1.set_title('Proporción de jugadores que llegan a la NBA', fontsize=14)
st.pyplot(fig1)  
# HISTORGRAMA 1
fig2, ax2 = plt.subplots()
sns.histplot(df2.PPG, facecolor='dodgerblue', edgecolor='black', bins=20, color='black', kde=True)
ax2.set_title('Distribución de PPG', fontsize=14)
st.pyplot(fig2)  