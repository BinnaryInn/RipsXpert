import os
import pandas as pd
import numpy as np
import calendar
from unidecode import unidecode
import datetime

def validar_fecha_excel_o_normal(date_str):
    try:
        numero_de_serie_excel = int(date_str)
        if numero_de_serie_excel >= 1:
            fecha_excel = datetime.datetime(1899, 12, 30) + datetime.timedelta(days=numero_de_serie_excel)
            fecha_formateada = fecha_excel.strftime('%d/%m/%Y')
            return str(fecha_formateada)
    except ValueError:
        pass  
    try:
        fecha_obj = datetime.datetime.strptime(date_str, '%d/%m/%Y')
        año_actual = datetime.datetime.now().year
        if 1920 <= fecha_obj.year <= año_actual:
            return str(date_str)
    except ValueError:
        pass
        return np.nan 
    

#year validation
def date_validation(date_str):
    try:
        fecha_obj = datetime.strptime(date_str, '%d/%m/%Y')
        año_actual = datetime.now().year
        if 1920 <= fecha_obj.year <= año_actual:
            return True
        else:
            return False
    except ValueError:
        return False
    
#get age

def extract_age(born_in):
    from datetime import datetime
    try:
        born_in = datetime.strptime(born_in, '%d/%m/%Y')
        fecha_actual = datetime.now()
        age = fecha_actual.year - born_in.year
        if (fecha_actual.month, fecha_actual.day) < (born_in.month, born_in.day):
            age -= 1
        return age
    except ValueError:
        return None
    
#client_code
# def add_bill_identifier(dataframe, number):
#     if isinstance(dataframe, pd.Series):
#         df = pd.DataFrame(dataframe)
#     elif isinstance(dataframe, pd.DataFrame):
#         df = dataframe.copy()
#     else:
#         raise ValueError("La entrada debe ser un DataFrame o una columna de DataFrame.")
#     df['Número de la factura'] = [f'OF{str(int(number+ i))}APSBS188' for i in range(len(df))]
#     return df


def add_bill_identifier(dataframe, number):
    if isinstance(dataframe, pd.Series):
        df = pd.DataFrame(dataframe)
    elif isinstance(dataframe, pd.DataFrame):
        df = dataframe.copy()
    else:
        raise ValueError("La entrada debe ser un DataFrame o una columna de DataFrame.")
    
    bills_code = np.arange(number+1,number+dataframe.shape[0]+1)
    bills = [f'OF{str(bill_code)}APSBS188' for bill_code in bills_code]
    return bills


#Start End Month
def start_end_month(fecha):
    from datetime import datetime
    try:
        fecha_obj = datetime.strptime(fecha, '%d/%m/%Y')
        año = fecha_obj.year
        mes = fecha_obj.month
        primer_dia_mes = datetime(año, mes, 1)
        _, ultimo_dia = calendar.monthrange(año, mes)
        ultimo_dia_mes = datetime(año, mes, ultimo_dia)
        inicio_mes = primer_dia_mes.strftime('%d/%m/%Y')
        fin_mes = ultimo_dia_mes.strftime('%d/%m/%Y')
        
        return (inicio_mes, fin_mes)
    except ValueError:
        return None