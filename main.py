#!/home/luk/Documentos/math-calc/env/bin/python3.11
import path
import time
from src import ingresos
from src import egresos
from src import plazo_fijo


def menu_plazo_fijo():
    print("1. Hacer nuevo plazo fijo.")
    print("2. Dar de baja un plazo fijo.")
    print("3. Ver plazos fijos actuales.")
    print("4. Ver historial de plazos fijos. (puede demorar en ejecutar)")
    plazo_fijo.hacer_plazo_fijo()
    pass


def menu_dolares():
    print("1. Compra.")
    print("2. Venta.")
    print("3. Ver dolares actuales.")
    print("4. Ver historial de Dolares. (puede demorar en ejecutar)")
    pass


def main():
    salir = False
    while salir == False:
        print("///////////////////////////////////////////////////////////")
        print("*****************************************")
        print("*  1. INGRESAR DINERO.                  *")
        print("*  2. QUITAR DINERO.                    *")
        print("*                                       *")
        print("*  3. Plazo fijo.                       *")
        print("*  4. Dolares.                          *")
        print("*                                       *")
        print("*  5. Consultar estadisticas de 1 y 2.  *")
        print("*                                       *")
        print("*  0. Salir.                            *")
        print("*****************************************")
        opcion = input("Opcion: ")
        if opcion == "1":
            time.sleep(1)
            pass
        elif opcion == "2":
            time.sleep(1)
            pass
        elif opcion == "3":
            time.sleep(1)
            menu_plazo_fijo()
            pass
        elif opcion == "4":
            time.sleep(1)
            menu_dolares()
            pass
        elif opcion == "5":
            time.sleep(1)
            pass
        elif opcion == "0":
            print("Saliendo...")
            time.sleep(1)
            salir = True
            print("Chau")
            print("///////////////////////////////////////////////////////////")
        else:
            print("opcion incorrecta.")
        print("///////////////////////////////////////////////////////////")


if __name__ == "__main__":
    main()
