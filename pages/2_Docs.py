import streamlit as st
import pandas as pd


with st.sidebar:
    st.success("Docs Review")   

st.title("Documentación :rainbow[RIPS Xpert]")

st.markdown("# :blue[**Quick**] Review RIPS")
intro = """
¡Hola! Gracias por utilizar :rainbow[**RIPS Xpert**]. Es importante que tengas en cuenta el siguiente conjunto de recomendaciones antes de cargar tu archivo:

- Asegúrate de nombrar las páginas del archivo **.xlsx** de acuerdo con los nombres especificados a continuación, respetando las *mayúsculas* y el orden dado:

    - **Pacientes**
    - **Tratamientos**
    - **Referencia**
- Si necesitas realizar ajustes en la tabla de referencia, te sugerimos hacerlo directamente desde el archivo **.xlsx** antes de cargarlo en la aplicación.

En caso de que encuentres algún error mientras utilizas la **aplicación de validación de RIPS**, no dudes en ponerte en contacto con el *desarrollador* para obtener asistencia y resolver cualquier problema.
"""

st.markdown(intro, unsafe_allow_html=True)

with st.expander("Tabla Pacientes",expanded=False):
    patient_cols_example = {
        'Fecha Registro': ['DD/MM/YYYY'],
        'Cedula': [1234567890],
        'Nombre': ['Primer Nombre'],
        'Apellido': ['Primer Apellido'],
        'Tipo Documento': ['CC'],
        'Lugar Expedicion': ['Cuidad'],
        '¿Corresponde?': ['Confirmo'],
        'Fecha Nacimiento': ['DD/MM/YYYY'],
        'Genero': ['M/F']
    }
    patient_df_example = pd.DataFrame(patient_cols_example)
    st.write(patient_df_example)

with st.expander("Tabla Tratamientos",expanded=False):
    data_tratamiento = {
        'Fecha Tratamiento': ['DD/MM/YYYY'],
        'Cedula Paciente': [1234567890],
        'Procedimiento': ['Procedimiento'],
        'Precio': ['100000']
    }
    df_tratamiento = pd.DataFrame(data_tratamiento)
    st.write(df_tratamiento)


with st.expander("Tabla Referencia",expanded=False):
    data_procedimiento = {
        'Procedimiento': ['Procedimiento'],
        'Grupo': ['R'],
        'Rips': ['Procedimiento RIPS'],
        'CUPS': [234402],
        'CIE-10': ['K081'],
        'DX2': ['K062']
        }
    df_procedimiento = pd.DataFrame(data_procedimiento)
    st.write(df_procedimiento)