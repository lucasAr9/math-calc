import path
import os
import csv
from datetime import datetime


def movimiento(monto, ingreso, donde):
    fecha_actual = datetime.now()
    fecha_formateada = fecha_actual.strftime('%Y-%m-%d')
    if ingreso:
        tipo = 'ingreso'
    else:
        tipo = 'egreso'
    datos = [fecha_formateada, monto, tipo, donde]

    archivo = os.path.join(path.FILES_PATH, 'ingresos_egresos.csv')
    with open(archivo, 'a+', encoding='utf-8', newline='') as csv_open:
        writer = csv.writer(csv_open, delimiter=';')
        if os.stat(archivo).st_size == 0:
            writer.writerow(['fecha', 'monto', 'tipo', 'movimiento'])
        writer.writerow(datos)
