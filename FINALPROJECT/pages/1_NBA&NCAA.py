
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
st.title("NBA/NCAA STATS & CONCLUSIONS")
def crear_pagina():
    st.write("¡Esta es mi página de Streamlit!")

st.image("images/SUBPLOT1.png")
st.write("Cómo podemos observar la cantidad de jugadores que han pasado a la nba en los últimos 20 años a través de su carrera universitaria, es una minoría,hay factores influyentes como la necesidad de los equipos según el año,la calidad de los jugadores del draft, y la calidad de agentes externos de ligas como podrían ser las europeas")
st.write('''cómo podemos observar las posibilidades de acceder a la NBA son bastante
         limitadas, podemos observar que , en los últimos 21 años,de más de 30 000 jugadores, 
         sólo alrededor de 1000 han conseguido llegar a la meta de jugar en la NBA
        ''')
st.image("images/SUBPLOT_PTS.png")

st.write('''Aquí podemos comprobar como la media de puntos de un jugador universitario en comparación  aun jugador de la nba tiene diferencia
a priori no parece una diferencia muy significativa, pero tenemos que teneer en cuenta dos factores, esto es una MEDIA , y lso jugadores de la NCAA juegan
alrededor de 30 partidos por temporada, mientras que los jugadores de la NBA juegan un minimo de 82 partidos por temporada, por lo que es mucho más dificil mantener una buena media.''')
st.image("images/subplot_importancia.png")

st.write("En éste gráfico podemos observar perfectamente la relación entre las diferentes características que hacen que un jugador destaque o no,como para así poder llegar a la NBA, hablemos un poco de ellas")