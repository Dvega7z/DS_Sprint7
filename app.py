import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import plotly.express as px  
import streamlit as st


# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Titulo
st.title("Venta de Autos Online")

# Descripcion
st.write("En esta pagina podas encontar el vehiculo que mejor se adapte a tus necesidades")

# Boton para crear histograma
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)


# Boton para el grafico de dispersion 
disp_button = st.button('Construir gráfico de dispersión')

if disp_button:
    st.write('Creación de un gráfico de dispersión para la relación entre año del modelo y precio')
    
    # Crear el gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="model_year", y="price", 
                            title="Relación entre Año del Modelo y Precio")
    
    # Mostrar el gráfico
    st.plotly_chart(fig_scatter, use_container_width=True)