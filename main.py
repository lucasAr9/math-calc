#!/home/luk/Documentos/math-calc/env/bin/python3.11
import path
import time
from src import ingresos_egresos
from src import plazo_fijo
from src import dolares


def menu_principal():
    print("*****************************************************************")
    print("*  1. INGRESAR PLATA.                                           *")
    print("*  2. GASTAR PLATA.                                             *")
    print("*                                                               *")
    print("*  3. Plazo fijo.                                               *")
    print("*  4. Dolares.                                                  *")
    print("*                                                               *")
    print("*  0. Salir.                                                    *")
    print("*****************************************************************")


def menu_plazo_fijo():
    print("1. Hacer nuevo plazo fijo.")
    print("2. Dar de baja un plazo fijo.")
    print("3. Ver plazos fijos actuales.")
    print("4. Ver historial de plazos fijos. (puede demorar en ejecutar)")
    print("0. Volver.")
    opcion = input("Opcion: ")
    if opcion == "1":
        plazo_fijo.hacer_plazo_fijo()
        pass
    elif opcion == "2":
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "0":
        pass
    else:
        print("opcion incorrecta.")


def menu_dolares():
    print("1. Compra.")
    print("2. Venta.")
    print("3. Ver dolares actuales.")
    print("4. Ver historial de Dolares. (puede demorar en ejecutar)")
    print("0. Volver.")
    opcion = input("Opcion: ")
    if opcion == "1":
        dolares.compra()
    elif opcion == "2":
        dolares.venta()
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "0":
        pass
    else:
        print("opcion incorrecta.")


def main():
    salir = False
    while not salir:
        print("/////////////////////////////////////////////////////////////////////////")
        menu_principal()
        opcion = input("Opcion: ")
        if opcion == "1":
            monto = input("Monto: ")
            ingresos_egresos.movimiento(monto, True, 'comun')
        elif opcion == "2":
            monto = input("Monto: ")
            ingresos_egresos.movimiento(monto, False, 'comun')
        elif opcion == "3":
            menu_plazo_fijo()
        elif opcion == "4":
            menu_dolares()
        elif opcion == "0":
            print("Saliendo...")
            time.sleep(1)
            salir = True
            print("Chau")
        else:
            print("Opcion incorrecta.")
        print("/////////////////////////////////////////////////////////////////////////")


if __name__ == "__main__":
    main()
