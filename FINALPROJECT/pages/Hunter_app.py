import streamlit as st
from PIL import Image

# Cargar las imágenes
imagen1 = 'images/NBA_GRAPH.jpg.png' 
st.image(imagen1,width=600)
imagen2 = 'images/NCAA_LOGO.png' 
st.image(imagen2,width=600) 
col1, col2 = st.columns(2) 

# Colocar las imágenes en las columnas
col1.image(imagen1)
col2.image(imagen2)
