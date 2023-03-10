import path
import os
import csv
from datetime import datetime
from src import ingresos_egresos


def hacer_plazo_fijo():
    monto = input("Monto: ")
    dias = input("Dias: ")
    intereses = input("Intereses: ")
    
    fecha_actual = datetime.now()
    fecha_formateada = fecha_actual.strftime('%Y-%m-%d')
    datos = [fecha_formateada, monto, dias, intereses]

    archivo = os.path.join(path.FILES_PATH, 'plazos_fijos.csv')
    with open(archivo, 'a+', encoding='utf-8', newline='') as csv_open:
        writer = csv.writer(csv_open, delimiter=';')
        if os.stat(archivo).st_size == 0:
            writer.writerow(['fecha', 'monto', 'dias', 'interes'])
        writer.writerow(datos)

    ingresos_egresos.movimiento(monto, False, 'plazo fijo')


def baja_plazo_fijo():
    pass


def vencimiento_plazo_fijo():
    # calcular el vencimiento y hacer un ingreso de plata porque volvio
    # a la caja de ahorro
    pass
