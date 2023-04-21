import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt 
st.image('images/VS_RADAR.jpg')
df = pd.read_csv("data/NBA_LIMPIO.csv")
def set_custom_style():
    plt.style.use('dark_background')
    plt.rcParams['axes.facecolor'] = '#1f2630'
    plt.rcParams['xtick.color'] = 'orange'
    plt.rcParams['ytick.color'] = 'orange'
    plt.rcParams['ytick.color'] = 'orange'
    plt.rcParams['xtick.labelsize'] = 8
    plt.rcParams['ytick.labelsize'] = 8
    plt.rcParams['axes.labelsize'] = 10
    plt.rcParams['axes.titlesize'] = 12
    plt.rcParams['axes.titleweight'] = 'bold'
    plt.rcParams['axes.titlepad'] = 12
    plt.rcParams['axes.grid'] = False
    plt.rcParams['legend.fontsize'] = 8
    plt.rcParams['legend.frameon'] = True
    plt.rcParams['legend.loc'] = 'lower right'
    plt.rcParams['legend.labelspacing'] = 0.5



def comp(df, player1, player2):
    df_1 = df[(df["Player"] == player1)]
    df_2 = df[(df["Player"] == player2)]
    categorias = ['PPG', 'FG%', 'APG' ,'RPG']
    categorias = [*categorias, categorias[0]]
    PLAY1 = [df_1["PPG"].median(), df_1["FG%"].median(), df_1["APG"].median(), df_1["RPG"].median()]
    PLAY2 = [df_2["PPG"].median(), df_2["FG%"].median(), df_2["APG"].median(), df_2["RPG"].median()]
    PLAY1 = [*PLAY1, PLAY1[0]]
    PLAY2 = [*PLAY2, PLAY2[0]]
    angulos = np.linspace(start=0, stop=2 * np.pi, num=len(categorias))
    
    set_custom_style()

    fig = plt.figure(figsize=(10,10))
    plt.polar(angulos, PLAY1, 'o-', label = f"{player1}")
    plt.polar(angulos, PLAY2, 'o-', label = f"{player2}")
    lines, labels = plt.thetagrids(np.degrees(angulos), labels=categorias)
    plt.title('Comparativa jugadores', size=12, y=1.05)
    plt.legend()
    
    # Mostrar la figura en Streamlit
    st.pyplot(fig)

# Agregar filtros en Streamlit
player1 = st.selectbox('Selecciona el jugador 1:', df['Player'].unique())
player2 = st.selectbox('Selecciona el jugador 2:', df['Player'].unique())

if st.button('Comparar'):
    comp(df, player1, player2)



