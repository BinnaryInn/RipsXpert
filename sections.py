
import pandas as pd
import numpy as np
from utiles import *

#columns
ac_columns =  ['Número de la factura','Código del prestador de servicios de salud','Tipo de Identificación del Usuario','Número de identificación del usuario en el sistema','Fecha de la consulta','Número de Autorización','Código de consulta','Finalidad de la consulta','Causa externa','Código del Diagnóstico principal','Código del diagnóstico relacionado N° 1','Código del diagnóstico relacionado N° 2','Código del diagnóstico relacionado N° 3','Tipo de diagnóstico principal','Valor de la consulta','Valor de la cuota moderadora','Valor Neto a pagar']
us_columns = ['Tipo de Identificación del Usuario','Número de Identifiación del Usuario en el Sistema','Código Entidad Administradora','Tipo de Usuario','Primer Apellido del usuario','Segundo apellido del usuario','Primer nombre del usuario','Segundo nombre del usuario','Edad','Unidad de medida de la Edad','Sexo','Código del departamento de residencia habitual','Código de municipios de residencia habitual','Zona de residencia habitual']
ap_columns = ['Número de la factura','Código del prestador de servicios de salud','Tipo de Identificación del Usuario','Número de identificación del usuario en el sistema','Fecha del procedimiento','Número de Autorización','Código del procedimiento','Ambito de realización del procedimiento','Finalidad del procedimiento','Personal que atiende','Diagnóstico principal','Código del diagnóstico relacionado','Código del diagnóstico de la Complicación','Forma de realización del acto quirúrgico','Valor del Procedimiento']
af_columns = ['Código del Prestador','Razón Social o Apellidos y nombres del prestador','Tipo de Identificación','Número de Identificación','Número de la factura','Fecha de expedición de la factura','Fecha de Inicio','Fecha final','Código entidad Administradora','Nombre entidad administradora','Número del Contrato','Plan de Beneficios','Número de la póliza','Valor total del pago compartido COPAGO','Valor de la comisión','Valor total de Descuentos','Valor Neto a Pagar por la entidad Contratante']


def constant_params_us(us): 
    #parametros constantes us
    us['Código Entidad Administradora'] = 'SDS001'
    us['Tipo de Usuario'] = '4'
    us['Unidad de medida de la Edad'] = '1'
    us['Código del departamento de residencia habitual'] = '11'
    us['Zona de residencia habitual'] = 'U'
    us['Segundo apellido del usuario'] = ''
    us['Segundo nombre del usuario'] = ''
    us['Código de municipios de residencia habitual'] = '1'
    us = us[us_columns]
    return us

def constant_params_ac(ac,code): 
    #parametros constantes ac
    ac['Código del prestador de servicios de salud'] = '110013660801'
    ac['Código de consulta'] = '890303'
    ac['Finalidad de la consulta'] = '10'
    ac['Causa externa'] = '13'
    ac['Código del diagnóstico relacionado N° 2'] = ''
    ac['Código del diagnóstico relacionado N° 3'] = ''
    ac['Tipo de diagnóstico principal'] = '2'
    ac['Valor de la consulta'] = '0'
    ac['Valor de la cuota moderadora'] = '0'
    ac['Valor Neto a pagar'] = '0'
    ac['Número de Autorización'] = ''
    ac['Número de la factura'] = add_bill_identifier(ac,code)
    ac = ac[ac_columns]
    return ac

def constant_params_ap(ap,code): 
    #parametros constantes ap
    ap['Código del prestador de servicios de salud'] = '110013660801'
    ap['Número de Autorización'] = ''
    ap['Ambito de realización del procedimiento'] = '1'
    ap['Finalidad del procedimiento'] = '2'
    ap['Personal que atiende'] = ''
    ap['Código del diagnóstico de la Complicación'] = ''
    ap['Número de la factura'] = add_bill_identifier(ap,code)
    ap = ap[ap_columns]
    return ap


def constant_params_af(af,code): 
#parametros constantes af
    af['Código del Prestador'] = '110013660801'
    af['Razón Social o Apellidos y nombres del prestador'] = 'ANGIE SOSA'
    af['Tipo de Identificación'] = 'CC'
    af['Número de Identificación'] = '1020830226'
    af['Código entidad Administradora'] = 'SDS001'
    af['Nombre entidad administradora'] = 'SECRETARIA DISTRITAL DE SALUD'
    af['Número del Contrato'] = ''
    af['Plan de Beneficios'] = ''
    af['Número de la póliza'] = ''
    af['Valor total del pago compartido COPAGO'] = '0'
    af['Valor de la comisión'] = '0'
    af['Valor total de Descuentos'] = '0'
    af['Número de la factura'] = add_bill_identifier(af,code)
    return af


