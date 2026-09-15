import streamlit as st

st.title("Clasificador de temperatura")

temperatura = st.number_input(
    "Introduce la temperatura en °C:",
    value=20
)
if temperatura < 10:
    print("Hace frio")
elif temperatura <=10 >=24:
    print("La temperatura es agradable.")
else:temperatura <=25:
    print("Hace calor.")
