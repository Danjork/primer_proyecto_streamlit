import streamlit as st
import pandas as pd
import os

#Cargar tareas o crear archivo vacio
FILE = "tareas.csv"

if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["Tarea","Estado"])
    df.to_csv(FILE, index=False)

#Leer archivo con datos
df = pd.read_csv(FILE)

st.title("📝 ToDo App - Danjork")
st.subheader("Crear y gestionar tareas")

#Agregar nueva tarea
nueva_tarea = st.text_input("Escribe una tarea:")

if st.button("Agregar"):
    if nueva_tarea:
        nueva_fila = pd.DataFrame([[nueva_tarea, "Pendiente"]], columns=["Tarea","Estado"])
        df = pd.concat([df,nueva_fila],ignore_index=True)
        df.to_csv(FILE, index=False)
        st.success("Tarea agregada correctamente")
        st.rerun()
    else:
        st.warning("Escribe una tarea antes")

st.write("### Tareas Actuales")
st.dataframe(df)
