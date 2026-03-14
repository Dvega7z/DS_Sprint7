import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import plotly.express as px  
import streamlit as st


# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Titulo
st.title("Venta de Autos Online")

# Descripcion
st.write("En esta pagina podras encontar el vehiculo que mejor se adapte a tus necesidades")

# Boton para crear histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Histograma para ver qué años de vehículos son más comunes')
    
    # Crear histograma con model_year
    fig = px.histogram(car_data, x="model_year")
    fig.update_layout(title_text='Distribución de Años de Vehículos')
    
    st.plotly_chart(fig, use_container_width=True)


# Boton para el grafico de dispersion 
disp_button = st.button('Construir gráfico de dispersión')

if disp_button:
    st.write('Creación de un gráfico de dispersión para la relación entre año del modelo y precio')
    
    # Crear el gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="model_year", y="price", 
                            title="Relación entre Año del Modelo y Precio")
    

    st.plotly_chart(fig_scatter, use_container_width=True)
    
