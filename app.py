import streamlit as st
import pandas as pd
import os

#Cargar tareas o crear archivo vacio
FILE = "tareas.csv"

def cargar_datos():
    if not os.path.exists(FILE):
        df = pd.DataFrame(columns=["Tarea", "Estado"])
        df.to_csv(FILE, index=False)
    return pd.read_csv(FILE)

def guardar_datos(df):
    df.to_csv(FILE, index=False)
df = cargar_datos()

st.title("📋 ToDo App Danjork")
st.markdown("Organiza tus tareas como un profesional 🧠")


#Agregar nueva tarea
nueva_tarea = st.text_input("Escribe una tarea:")

if st.button("Agregar"):
    if nueva_tarea:
        nueva_fila = pd.DataFrame([[nueva_tarea, "Pendiente"]], columns=["Tarea","Estado"])
        df = pd.concat([df, nueva_fila],ignore_index=True)
        guardar_datos(df)
        st.success("Tarea agregada correctamente")
        st.rerun()
    else:
        st.warning("Escribe una tarea antes")

st.write("### Filtrar tareas por estado")
opcion_estado = st.selectbox("Selecciona un estado: ", ["Todas","Pendiente","Completada","Pausado"])

if opcion_estado != "Todas":
    df = df[df["Estado"] == opcion_estado]

#Aqui muestra la tabla con las tareas ingresadas
st.write("### Tareas Actuales")
st.dataframe(df)

#modifica el estado
st.write("### Modificar estado de tareas")

for i, row in df.iterrows():
    col1, col2, col3 , col4= st.columns([4,2,2,2])
    with col1:
        st.write(f"{i+1}. {row['Tarea']}")
    with col2:
        if st.button("✅ Completar", key=f"comp_{i}"):
            df.at[i, "Estado"] = "Completada"
            df.to_csv(FILE, index=False)
            st.rerun()
    with col3:
        if st.button("⏸ Pausar", key=f"pausa_{i}"):
            df.at[i, "Estado"] = "Pausada"
            df.to_csv(FILE, index=False)
            st.rerun()
    with col4:
        if st.button("🗑 Eliminar", key=f"elim_{i}"):
            df.drop(i, inplace=True)
            df.to_csv(FILE, index=False)
            st.rerun()

