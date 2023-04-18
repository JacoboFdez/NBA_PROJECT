import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
st.set_page_config(
        page_title="NBA HUNTERS",
        page_icon="🤯",
        layout="wide"
    )

st.sidebar.success("Select a page above.")
st.title("")
# Cargar las imágenes
st.image( 'images/vs.jpg' ) 


st.write("""Bienvenido a mi proyecto de compilación de datos de jugadores universitarios y de la NBA desde 2002 hasta 2023!
Este proyecto tiene como objetivo recopilar datos de jugadores universitarios y de la NBA en un período de 21 años, desde 2002 hasta 2023. Los datos recopilados incluyen información sobre los jugadores universitarios que pasan a jugar en la NBA y los que no.
Como segundo objetivo he realizado una modelo predictivo en base a estos datos el cual nos puede ayudar a predecir si un jugador llegará o no a la nba en base a sus estadísticas universitarias.
A su vez,sacaremos patrones como por ejemplo el porcentaje de jugadores universitarios que optan a ir a la NBA, el equipo que más jugadores ha brindado a la misma y muchos otros datos interesantes.""")



df = pd.read_csv("notebooks/PREDICCIÓN.csv")
nba_count = df[df['NBA'] == 'Sí'].shape[0]
no_nba_count = df[df['NBA'] == 'No'].shape[0]
df2 = pd.read_csv('data/PREDICCIÓN.csv')
# HISTORGRAMA 1
plt.figure(figsize=(4,4))
sns.histplot(df2.PPG, facecolor='darkorange', edgecolor='black', bins=30, color='black', kde=True)
plt.title('Distribución de PPG', fontsize=10)
st.pyplot()


st.write('''cómo podemos observar las posibilidades de acceder a la NBA son bastante
         limitadas, podemos observar que , en los últimos 21 años,de más de 30 000 jugadores, 
         sólo alrededor de 1000 han conseguido llegar a la meta de jugar en la NBA, veámoslo más
         cómodamente con porcentaje''')


'''# PIE CHART
figsize=(3, 3))
labels = ['Sí', 'No']
sizes = [nba_count, no_nba_count]
colors = ['#FFC154', '#3D3D3D']
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax1.set_title('Jugadores que llegan a la NBA', fontsize=9)
st.pyplot(fig1) ''' 







