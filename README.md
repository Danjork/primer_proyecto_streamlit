# primer proyecto streamlit
#📝 ToDo App - Danjork
Una pequeña aplicación para gestionar tareas diarias en el trabajo contruida en [StreamLit](https://streamlit.io/) y [Pandas](https://pandas.pydata.org/). Permite crear, visualizar y actualizar tareas como "pendiente", "pausado" o "completado".

![img.png](img.png)

## ✨ Funcionalidades

- Agregar nuevas tareas
- Visualizar todas las tareas en una tabla
- Cambiar el estado de una tarea a "Pendiente", "Pausado" o "Completado"
- Almacenamiento archivo CSV

## 🏃 Cómo correr la app

1. **Clona el repositorio**

```bash
git clone https://github.com/tu-usuario/todo-streamlit-app.git
cd todo-streamlit-app

python -m venv .venv
# En Windows:
.venv\Scripts\activate
# En macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt

streamlit run app.py

#
✅ Requisitos
Python 3.8+

Streamlit

Pandas
