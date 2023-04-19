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

st.write("Antes de nada,vamos a explicar brevemente en qué consisten y qué son estas ligas")

st.image("images/NCAA_logotipo.jpg",use_column_width=True)
st.image("images/MAPA_NCAA.jpg",use_column_width=True)
st.write("La NCAA Men's Basketball es una competición de baloncesto universitario en los Estados Unidos, organizada por la Asociación Nacional de Atletismo Universitario (NCAA). Es un campeonato anual que incluye equipos de universidades y colegios de todo el país. La NCAA Men's Basketball es conocida por su popularidad, emocionantes partidos y el desarrollo de futuros jugadores de baloncesto profesionales. Es una liga universitaria altamente competitiva y seguida por fanáticos del baloncesto en todo el país.")

st.image("images/logotipo.png",use_column_width=True)
st.image("images/MAPA_NBA.jpg",use_column_width=True)
st.write("La NBA (National Basketball Association) es la principal liga de baloncesto profesional de Estados Unidos y una de las más importantes a nivel mundial. Es una liga compuesta por equipos profesionales ubicados en ciudades de Estados Unidos y Canadá. La NBA es conocida por su alta competitividad, con jugadores de élite a nivel mundial, emocionantes partidos y una gran base de seguidores en todo el mundo. Es considerada la liga más prestigiosa y popular del baloncesto profesional, y cuenta con una rica historia y tradición en la cultura del deporte.")












