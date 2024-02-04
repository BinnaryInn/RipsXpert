import pandas as pd
import numpy as np
from utiles import *
import streamlit as st
from utiles import *
from sections import *

st.set_page_config(
    page_title="RIPS Xpert"
)

st.title("Overview Page :rainbow[RIPS Xpert]")
st.sidebar.success("Overview")

st.markdown('*A continuación, te proporcionamos una visión general de cómo se ven los **archivos***')

#columns
ac_columns =  ['Número de la factura','Código del prestador de servicios de salud','Tipo de Identificación del Usuario','Número de identificación del usuario en el sistema','Fecha de la consulta','Número de Autorización','Código de consulta','Finalidad de la consulta','Causa externa','Código del Diagnóstico principal','Código del diagnóstico relacionado N° 1','Código del diagnóstico relacionado N° 2','Código del diagnóstico relacionado N° 3','Tipo de diagnóstico principal','Valor de la consulta','Valor de la cuota moderadora','Valor Neto a pagar']
us_columns = ['Tipo de Identificación del Usuario','Número de Identifiación del Usuario en el Sistema','Código Entidad Administradora','Tipo de Usuario','Primer Apellido del usuario','Segundo apellido del usuario','Primer nombre del usuario','Segundo nombre del usuario','Edad','Unidad de medida de la Edad','Sexo','Código del departamento de residencia habitual','Código de municipios de residencia habitual','Zona de residencia habitual']
ap_columns = ['Número de la factura','Código del prestador de servicios de salud','Tipo de Identificación del Usuario','Número de identificación del usuario en el sistema','Fecha del procedimiento','Número de Autorización','Código del procedimiento','Ambito de realización del procedimiento','Finalidad del procedimiento','Personal que atiende','Diagnóstico principal','Código del diagnóstico relacionado','Código del diagnóstico de la Complicación','Forma de realización del acto quirúrgico','Valor del Procedimiento']
af_columns = ['Código del Prestador','Razón Social o Apellidos y nombres del prestador','Tipo de Identificación','Número de Identificación','Número de la factura','Fecha de expedición de la factura','Fecha de Inicio','Fecha final','Código entidad Administradora','Nombre entidad administradora','Número del Contrato','Plan de Beneficios','Número de la póliza','Valor total del pago compartido COPAGO','Valor de la comisión','Valor total de Descuentos','Valor Neto a Pagar por la entidad Contratante']


# ac = pd.read_csv('./example/AC.txt', header=None).fillna('')
# af = pd.read_csv('./example/AF.txt', header=None).fillna('')
# ap = pd.read_csv('./example/AP.txt', header=None).fillna('')
# us = pd.read_csv('./example/US.txt', header=None).fillna('')

# us.columns = us_columns
# ac.columns = ac_columns
# ap.columns = ap_columns
# af.columns = af_columns

ac_list = [
    ["Factura", "110013660801", "CC", "10000000", "01/03/2023", "", "890303", "10", "13", "K023", "K021", "", "", "2", "0", "0", "0"],
    ["Factura", "110013660801", "CC", "10000000", "01/03/2023", "", "890303", "10", "13", "K023", "K021", "", "", "2", "0", "0", "0"],
    ["Factura", "110013660801", "CC", "10000000", "02/03/2023", "", "890303", "10", "13", "K023", "K021", "", "", "2", "0", "0", "0"],
    ["Factura", "110013660801", "CC", "10000000", "03/03/2023", "", "890303", "10", "13", "K023", "K023", "", "", "2", "0", "0", "0"]
]

ac = pd.DataFrame(ac_list, columns=ac_columns)


af_list = [
    ["110013660801", "PRESTADOR", "CC", "1000000000", "Factura", "01/03/2023", "01/03/2023", "31/03/2023", "SDS001", "SECRETARIA DISTRITAL DE SALUD", "", "", "", "0", "0", "0", "50000"],
    ["110013660801", "PRESTADOR", "CC", "1000000000", "Factura", "01/03/2023", "01/03/2023", "31/03/2023", "SDS001", "SECRETARIA DISTRITAL DE SALUD", "", "", "", "0", "0", "0", "70000"],
    ["110013660801", "PRESTADOR", "CC", "1000000000", "Factura", "02/03/2023", "01/03/2023", "31/03/2023", "SDS001", "SECRETARIA DISTRITAL DE SALUD", "", "", "", "0", "0", "0", "80000"],
    ["110013660801", "PRESTADOR", "CC", "1000000000", "Factura", "03/03/2023", "01/03/2023", "31/03/2023", "SDS001", "SECRETARIA DISTRITAL DE SALUD", "", "", "", "0", "0", "0", "190000"]
]

af = pd.DataFrame(af_list, columns=af_columns)


ap_list = [
    ["Factura", "110013660801", "CC", "100000000", "01/03/2023", "", "232102", "1", "2", "", "K023", "K021", "", "1", "50000"],
    ["Factura", "110013660801", "CC", "100000000", "01/03/2023", "", "232102", "1", "2", "", "K023", "K021", "", "1", "70000"],
    ["Factura", "110013660801", "CC", "100000000", "02/03/2023", "", "232102", "1", "2", "", "K023", "K021", "", "1", "80000"],
    ["Factura", "110013660801", "CC", "100000000", "03/03/2023", "", "234204", "1", "2", "", "K023", "K023", "", "1", "190000"]
]

ap = pd.DataFrame(ap_list, columns=ap_columns)


us_list = [
    ["CC", "10000000", "SDS001", "4", "NOMBRE", "", "APELLIDO", "", "37", "1", "F", "11", "1", "U"],
    ["CC", "10000000", "SDS001", "4", "NOMBRE", "", "APELLIDO", "", "46", "1", "F", "11", "1", "U"],
    ["CC", "10000000", "SDS001", "4", "NOMBRE", "", "APELLIDO", "", "60", "1", "F", "11", "1", "U"],
    ["CC", "10000000", "SDS001", "4", "NOMBRE", "", "APELLIDO", "", "43", "1", "M", "11", "1", "U"]
]

us = pd.DataFrame(us_list, columns=us_columns)


st.info('Ilustración de la tabla de **Usuarios**', icon="ℹ️")
st.write(us)


st.info('Ilustración de la tabla de **Consultas**', icon="ℹ️")
st.write(ac)


st.info('Ilustración de la tabla de **Procedimientos**', icon="ℹ️")
st.write(ap)


st.info('Ilustración de la tabla de **Facturas**', icon="ℹ️")
st.write(af)