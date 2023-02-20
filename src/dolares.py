import path
import os
import csv
from datetime import datetime
from src import ingresos
from src import egresos


def compra():
    pesos = input("Pesos: ")
    dolares = input("Dolares: ")
    costo_dolar = input("Costo por dolar: ")
    
    fecha_actual = datetime.now()
    fecha_formateada = fecha_actual.strftime('%Y-%m-%d %H:%M:%S')
    datos = [fecha_formateada, pesos, dolares, costo_dolar]

    archivo = os.path.join(path.FILES_PATH, 'compra_dolares.csv')
    with open(archivo, 'a', encoding='utf-8', newline='') as csv_open:
        writer = csv.writer(csv_open, delimiter=';')
        writer.writerow(datos)

    # hacer un egreso de plata porque se fue a dolares


def venta():
    pesos = input("Pesos: ")
    dolares = input("Dolares: ")
    costo_dolar = input("Costo por dolar: ")
    
    fecha_actual = datetime.now()
    fecha_formateada = fecha_actual.strftime('%Y-%m-%d %H:%M:%S')
    datos = [fecha_formateada, pesos, dolares, costo_dolar]

    archivo = os.path.join(path.FILES_PATH, 'venta_dolares.csv')
    with open(archivo, 'a', encoding='utf-8', newline='') as csv_open:
        writer = csv.writer(csv_open, delimiter=';')
        writer.writerow(datos)

    # hacer un egreso de plata porque se fue a dolares
