import os
import pandas as pd
import numpy as np
from unidecode import unidecode
from utiles import *
import streamlit as st
from io import StringIO
from utiles import *
from sections import *

st.set_page_config(
    page_title="RIPS Xpert"
)

st.title("Home Page :rainbow[RIPS Xpert]")
st.sidebar.success("Playgroud")

st.info('Visita la **documentación** para asegurarte de que el archivo cumple con los *requisitos básicos*', icon="ℹ️")
uploaded_file = st.file_uploader("Carga el Archivo .xlsx correpondiente al mes a analizar.")

if uploaded_file is None:
    # Muestra un mensaje informativo si no se ha cargado ningún archivo
    st.info("Por favor, cargue un archivo usando el botón de arriba.",icon="ℹ️")

else:

    pacientes = pd.read_excel(uploaded_file, sheet_name='Pacientes')
    tratamientos = pd.read_excel(uploaded_file, sheet_name='Tratamientos')
    referencia = pd.read_excel(uploaded_file, sheet_name='Referencia')

    #Preparación Tratamientos Dataset
    tratamientos['Fecha Tratamiento'] = tratamientos['Fecha Tratamiento'] #.apply(lambda x: validar_fecha_excel_o_normal(x))
    tratamientos = pd.merge(tratamientos,referencia,left_on=['Procedimiento'],right_on=['Procedimiento'], how='inner')
    tratamientos = tratamientos[['Fecha Tratamiento','Cedula Paciente','CUPS','CIE-10','DX2','Precio']]

    #Preparación Pacientes Dataset
    pacientes = pacientes[(pacientes['¿Corresponde?'] == 'Confirmo')&(pacientes['Tipo Documento'] == 'CC')]
    pacientes['Fecha Nacimiento'] = pacientes['Fecha Nacimiento'] #.apply(validar_fecha_excel_o_normal)
    pacientes['Nombre'] = pacientes['Nombre'].apply(lambda x: unidecode(x).strip().upper())
    pacientes['Apellido'] = pacientes['Apellido'].apply(lambda x: unidecode(x).strip().upper())
    pacientes['Genero'] = pacientes['Genero'].apply(lambda x: 'M' if x == 'Masculino' else 'F')
    pacientes = pacientes[['Cedula','Nombre','Apellido','Tipo Documento','Fecha Nacimiento','Genero']]

    dataset = pd.merge(tratamientos,pacientes,left_on=['Cedula Paciente'],right_on=['Cedula'], how='left')
    dataset = dataset[['Fecha Tratamiento','Tipo Documento','Cedula','Nombre','Apellido','Fecha Nacimiento','Genero','CUPS','CIE-10','DX2','Precio']]
    dataset.columns = ['FECHA','TDOC','CEDULA','NOMBRE','APELLIDO','NACIMIENTO','GENERO','CUPS','CIE10','DX2','PRECIO']
    dataset.dropna(inplace=True)
    dataset['EDAD'] = dataset['NACIMIENTO'].apply(extract_age)

    #fill tabla us
    us_data = dataset.copy()
    us_data['Tipo de Identificación del Usuario'] = us_data['TDOC']
    us_data['Número de Identifiación del Usuario en el Sistema'] = us_data['CEDULA'].apply(lambda x:int(x))
    us_data['Primer Apellido del usuario'] = us_data['APELLIDO']
    us_data['Primer nombre del usuario'] = us_data['NOMBRE']
    us_data['Edad'] = us_data['EDAD']
    us_data['Sexo'] = us_data['GENERO']
    us_data = constant_params_us(us_data)
    us_data = us_data.drop_duplicates(subset=['Número de Identifiación del Usuario en el Sistema'])

    st.warning('**Verifica!**, Usa la tabla de consultas (**AC.txt**) del *mes pasado* antes de colocar el número de factura.', icon="⚠️")
    text_input = st.text_input(label= "Ultimo Codigo de Factura **Unicamente el Número Ej. 1354**",label_visibility="visible",disabled=False,placeholder="Ingresa la ultima factura",key="bill_code")

    if text_input:
        #fill tabla ac
        try:
            bill_code = int(text_input)
            st.info(f"Si la ultima factura Ingresada fue: **{text_input}**, Iniciarás apartir de: **OF{bill_code + 1}APSBS188**",icon="ℹ️")
        except ValueError:
            st.write("Ingresa un número válido.")

        ac_data = dataset.copy()
        ac_data['Tipo de Identificación del Usuario'] = ac_data['TDOC']
        ac_data['Número de identificación del usuario en el sistema'] = ac_data['CEDULA'].apply(lambda x:int(x))
        ac_data['Código del Diagnóstico principal'] = ac_data['CIE10']
        ac_data['Código del diagnóstico relacionado N° 1'] = ac_data['DX2']
        ac_data['Fecha de la consulta'] = ac_data['FECHA']
        ac_data = constant_params_ac(ac_data,bill_code)
        
        #fill tabla ap
        ap_data = dataset.copy()
        ap_data['Tipo de Identificación del Usuario'] = ap_data['TDOC']
        ap_data['Número de identificación del usuario en el sistema'] = ap_data['CEDULA'].apply(lambda x:int(x))
        ap_data['Diagnóstico principal'] = ap_data['CIE10']
        ap_data['Código del diagnóstico relacionado'] = ap_data['DX2']
        ap_data['Fecha del procedimiento'] = ap_data['FECHA']
        ap_data['Código del procedimiento'] = ap_data['CUPS']
        ap_data['Forma de realización del acto quirúrgico'] = ap_data['CUPS'].apply(lambda x: '1' if str(x)[0]=='2' else '')
        ap_data['Valor del Procedimiento'] = ap_data['PRECIO']
        ap_data = constant_params_ap(ap_data,bill_code)
        
        to_reprice_bills = list(ap_data[ap_data['Diagnóstico principal'] == 'Z012']['Número de la factura'].values)

        #fill tabla af
        af_data = dataset.copy()
        #parametros constantes af
        af_data['Código del Prestador'] = '110013660801'
        af_data['Razón Social o Apellidos y nombres del prestador'] = 'ANGIE SOSA'
        af_data['Tipo de Identificación'] = 'CC'
        af_data['Número de Identificación'] = '1020830226'
        af_data['Código entidad Administradora'] = 'SDS001'
        af_data['Nombre entidad administradora'] = 'SECRETARIA DISTRITAL DE SALUD'
        af_data['Número del Contrato'] = ''
        af_data['Plan de Beneficios'] = ''
        af_data['Número de la póliza'] = ''
        af_data['Valor total del pago compartido COPAGO'] = '0'
        af_data['Valor de la comisión'] = '0'
        af_data['Valor total de Descuentos'] = '0'
        af_data['Número de la factura'] = add_bill_identifier(af_data,bill_code)
        af_data['Valor Neto a Pagar por la entidad Contratante'] = af_data.apply(lambda data: '0' if data['Número de la factura'] in to_reprice_bills else data['PRECIO'], axis=1)
        af_data['Fecha de expedición de la factura'] = af_data['FECHA']
        af_data['Fecha de Inicio'] = af_data['Fecha de expedición de la factura'].apply(lambda x: start_end_month(x)[0])
        af_data['Fecha final'] = af_data['Fecha de expedición de la factura'].apply(lambda x: start_end_month(x)[1])
        af_data = af_data[af_columns]

        
        #Eliminar Facturas de Procedimientos con Codigo Z012
        ap_data = ap_data[ap_data['Diagnóstico principal'] != 'Z012']

        bill = list(ac_data['Número de la factura'].values)[-1:]
        bill = str(bill[-1:][0])
        archivo = 'example/bill.txt'

        with open(archivo, 'w') as file:
            file.write(bill)

        st.write(us_data)
        #download us
        @st.cache_data 
        def convert_df(df):
            csv_without_header = df.to_csv(index=False, header=False).encode('utf-8')
            return csv_without_header
        
        csv_us = convert_df(us_data)
        st.download_button(
            label="Usuarios RIPS",
            data=csv_us,
            file_name='us.txt',
            mime='text/csv',
        )

        st.write(ac_data)
        #download us
        csv_ac = convert_df(ac_data)
        st.download_button(
            label="Consultas RIPS",
            data=csv_ac,
            file_name='ac.txt',
            mime='text/csv',
        )

        st.write(ap_data)
        #download ap
        csv_ap = convert_df(ap_data)
        st.download_button(
            label="Procedimientos RIPS",
            data=csv_ap,
            file_name='ap.txt',
            mime='text/csv',
        )


        st.write(af_data)
        #download af
        csv_af = convert_df(af_data)
        st.download_button(
            label="Facturas RIPS",
            data=csv_af,
            file_name='af.txt',
            mime='text/csv',
        )
        