import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos desde un archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear encabezado
st.header('Análisis de datos de vehículos')

# Crear un botón para construir un histograma
hist_button = st.button('Construir histograma')

if hist_button: 
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón para construir un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button: 
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price", title='Odometer vs Price')
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Opcional: Utilizar casillas de verificación
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_histogram: 
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter: 
    st.write('Construir un gráfico de dispersión para odómetro y precio')
    fig = px.scatter(car_data, x="odometer", y="price", title='Odometer vs Price')
    st.plotly_chart(fig, use_container_width=True)
