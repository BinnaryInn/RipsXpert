import pandas as pd
import numpy as np
from utiles import *
import streamlit as st
from utiles import *
from sections import *
import time


st.title("Check Bill Page :rainbow[RIPS Xpert]")
st.sidebar.success("Bill History")

st.info('A continuación, te mostraré el **código de factura** más reciente almacenado',icon='ℹ️')

def cook_breakfast():
    msg = st.toast('Gathering ingredients...')
    time.sleep(1)
    msg.toast('Cooking...')
    time.sleep(1)
    msg.toast('Ready!', icon = "🥞")



if st.button('Obtener la factura más reciente'):
    archivo = 'example/bill.txt'
    with open(archivo, 'r') as file:
        retrieve_bill = file.read()
        cook_breakfast()
        st.success(f"**Número de Factura**: {retrieve_bill}",icon="✅")