import streamlit as st

st.title("mi primera app")
st.write("hola danjork")

nombre = st.text_input("Cual es tu nombre")
if nombre:
    st.success(f"Bienvenido, {nombre} ")

