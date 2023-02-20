import path
import os
import csv
from datetime import datetime
from src import ingresos
from src import egresos


def hacer_plazo_fijo():
    monto = input("Monto: ")
    dias = input("Dias: ")
    intereses = input("Intereses: ")
    
    fecha_actual = datetime.now()
    fecha_formateada = fecha_actual.strftime('%Y-%m-%d %H:%M:%S')
    datos = [fecha_formateada, monto, dias, intereses]

    archivo = os.path.join(path.FILES_PATH, 'plazos_fijos.csv')
    with open(archivo, 'a', encoding='utf-8', newline='') as csv_open:
        writer = csv.writer(csv_open, delimiter=';')
        writer.writerow(datos)

    # hacer un egreso de plata porque se fue al plazo fijo


def vencimiento_plazo_fijo():
    # calcular el vencimiento y hacer un ingreso de plata porque volvio
    # a la caja de ahorro
    pass


def baja_plazo_fijo():
    pass
