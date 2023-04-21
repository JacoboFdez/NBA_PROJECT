import streamlit as st
from PIL import Image




import streamlit as st
import pandas as pd
import pickle

import os
st.image( 'images/NBA_HUNTER.png' ) 

# Obtener la ruta absoluta del archivo Dtree.pkl
ruta_absoluta = os.path.abspath('src/Dtree.pkl')

with open(ruta_absoluta, 'rb') as archivo:
    modelo_cargado = pickle.load(archivo)


def hacer_prediccion(GP, MPG, PPG, FG, TP, FT, ORB, DRB, RPG, APG, SPG, BPG, TOV, PF):
    datos_entrada = pd.DataFrame({'GP': [GP], 'MPG': [MPG], 'PPG': [PPG], 'FG%': [FG], '3P': [TP],
                                  'FT%': [FT], 'ORB': [ORB], 'DRB': [DRB], 'RPG': [RPG], 'APG': [APG],
                                  'SPG': [SPG], 'BPG': [BPG], 'TOV': [TOV], 'PF': [PF]})
    prediccion = modelo_cargado.predict(datos_entrada)
    return prediccion[0]

# Crear la interfaz de usuario con los widgets de entrada
st.title('Aplicación de predicción para jugadores de la NBA')
st.write('Ingrese los siguientes datos para hacer una predicción:')

GP = st.number_input('GP')
MPG = st.number_input('MPG')
PPG = st.number_input('PPG')
FG = st.number_input('FG%')
TP = st.number_input('3P')
FT = st.number_input('FT%')
ORB = st.number_input('ORB')
DRB = st.number_input('DRB')
RPG = st.number_input('RPG')
APG = st.number_input('APG')
SPG = st.number_input('SPG')
BPG = st.number_input('BPG')
TOV = st.number_input('TOV')
PF = st.number_input('PF')

# Hacer la predicción al hacer clic en el botón
if st.button('Hacer predicción'):
    resultado = hacer_prediccion(GP, MPG, PPG, FG, TP, FT, ORB, DRB, RPG, APG, SPG, BPG, TOV, PF)
    if resultado == 1:
        imagen_gif = 'images/YES.gif'
        st.image(imagen_gif, use_column_width=False)
        st.write('Con un 97% de acierto,el jugador de características citadas entrará a la NBA.')
    else:
        imagen_gif = 'images/NO.gif'
        st.image(imagen_gif, use_column_width=False)
        st.write('Con un 97% de acierto,el jugador de características citadas NO entrará a la NBA.')
