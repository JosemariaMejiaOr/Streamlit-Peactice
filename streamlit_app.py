import numpy as np
import altair as alt
import pandas as pd
import streamlit as st



st.header('Análisis Pedidos')

st.write('Información Pedidos')

df = pd.DataFrame({
'Producto': ['Balon', 'Bicicleta', 'Lavadora', 'Zapatos'],
'Precio': [1500, 3500, 10000, 400]
})
st.write(df)


st.write('Rutas:')
st.subheader('Gráfico: Precio')
chart = alt.Chart(df).mark_circle(size=100).encode(
    x='Precio',
    y='Producto',
    tooltip=['Producto', 'Precio']
)
st.write(chart)
