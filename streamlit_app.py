import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
st.header('st.write')
# Example 1
st.write('Hello, *World!* :sunglasses:')
# Example 2
st.write('Goles x temporada Messi')
# Example 3
df = pd.DataFrame({
    'temporada': [1, 2, 3, 4],
    'goles': [38, 39, 21, 16]
    })
st.write(df)
# Example 4: Texto combinado con DataFrame
df_messi_temp = pd.DataFrame({
    'Temporada': [f'{a}-{a+1}' for a in range(2010, 2015)],
    'Goles': [47, 53, 73, 60, 41]
})
st.write('A continuación un resumen de sus mejores temporadas:', df_messi_temp, 'Época dorada en el FC Barcelona.')

# Example 5: Gráfico interactivo con variables simuladas de partidos
df_messi_stats = pd.DataFrame(
    np.random.randn(200, 3) * [10, 1, 0.5] + [90, 0.8, 0.6],
    columns=['minutos_jugados', 'goles', 'asistencias']
)

chart = alt.Chart(df_messi_stats).mark_circle().encode(
    x='minutos_jugados',
    y='goles',
    size='asistencias',
    color='asistencias',
    tooltip=['minutos_jugados', 'goles', 'asistencias']
).interactive()

st.write("Gráfico de rendimiento partido a partido")
st.write(chart)