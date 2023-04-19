
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
st.title("¿Qué lleva a un jugador universitario a poder dar el salto a la NBA?")
def crear_pagina():
    st.write("¡Esta es mi página de Streamlit!")

imagen_1 = 'images/ENTRADAS.png'
imagen_2 = 'images/porcentaje_entradas.png'


col1, col2 = st.columns(2)
with col1:
    st.image(imagen_1)
with col2:
    st.image(imagen_2)
st.write("Cómo podemos observar la cantidad de jugadores que han pasado a la nba en los últimos 20 años a través de su carrera universitaria, es una minoría,hay factores influyentes como la necesidad de los equipos según el año,la calidad de los jugadores del draft, y la calidad de agentes externos de ligas como podrían ser las europeas")
st.write('''cómo podemos observar las posibilidades de acceder a la NBA son bastante
         limitadas, podemos observar que , en los últimos 21 años,de más de 30 000 jugadores, 
         sólo alrededor de 1000 han conseguido llegar a la meta de jugar en la NBA
        ''')

st.image("images/boxplot_importancia.png")

st.write("En éste gráfico podemos observar perfectamente la relación entre las diferentes características que hacen que un jugador destaque o no,como para así poder llegar a la NBA, hablemos un poco de ellas")