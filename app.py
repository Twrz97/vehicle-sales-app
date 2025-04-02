import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Control de Mando - Análisis de Datos de Coches')

# Mensaje intro
st.write("Marca las casillas para construir gráficos interactivos:")

# Casilla de verfificacion para histograma
hist_box = st.checkbox('Construir histograma')  # crear un botón

if hist_box:  # al seleccionar casilla
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig_hist = px.histogram(car_data, x="odometer",
                            title="Distribución de Odometro", nbins=20)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla de verfificacion para Grafico de Dispersión
disp_box = st.checkbox('Construir gráfico de dispersión')  # crear un botón
if disp_box:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersión
    fig_disp = px.scatter(car_data, x="model_year", y="price",
                          title="Relación entre Año y Precio")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_disp, use_container_width=True)
