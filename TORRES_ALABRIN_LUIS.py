# EVALUACION FINAL TRANSVESAL

import random
import csv

trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]

def asignar_sueldos_aleatorios():
    sueldos_trabajadores = []
    for i in range(10):
        sueldo = random.randint(300000, 2500000)
        sueldos_trabajadores.append(sueldo)
    return sueldos_trabajadores

def clasificar_sueldos(trabajadores, sueldos_aleatorios):
    sueldo_bajo = []
    sueldo_medio = []
    sueldo_alto = []
    for i in range(len(trabajadores)):
        nombre = trabajadores[i]
        salario = sueldos_aleatorios[i]
        
        if salario < 800000:
            sueldo_bajo.append((nombre, salario))
        elif 800000 <= salario <= 2000000:
            sueldo_medio.append((nombre, salario))
        else:
            sueldo_alto.append((nombre, salario))
            
    print(f"Sueldos menores a $800.000 TOTAL: {len(sueldo_bajo)}")
    print("Nombre empleado    Sueldo")
    for nombre, salario in sueldo_bajo:
        print(f"{nombre:<20} ${salario:,}")
        
    print(f"\nSueldos entre $800.000 y $2.000.000 TOTAL: {len(sueldo_medio)}")
    print("Nombre empleado    Sueldo")
    for nombre, salario in sueldo_medio:
        print(f"{nombre:<20} ${salario:,}")
        
    print(f"\nSueldos superiores a $2.000.000 TOTAL: {len(sueldo_alto)}")
    print("Nombre empleado    Sueldo")
    for nombre, salario in sueldo_alto:
        print(f"{nombre:<20} ${salario:,}")
        
    print(f"\nTOTAL SUELDOS: ${sum(sueldos_aleatorios):,}")

def ver_estadisticas(sueldos_aleatorios):
    sueldo_maximo = max(sueldos_aleatorios)
    sueldo_minimo = min(sueldos_aleatorios)
    promedio_sueldos = sum(sueldos_aleatorios) / len(sueldos_aleatorios)
    #media_geometrica = pow(sueldos_aleatorios, 1/10)
    
    print(f"El sueldo más alto es: ${sueldo_maximo:,}")
    print(f"El sueldo más bajo es: ${sueldo_minimo:,}")
    print(f"El promedio de sueldos es: ${promedio_sueldos:,}")
    #print(f"La media geometrica es: ${media_geometrica:,}")
    
def reporte_sueldos(trabajadores, sueldos_aleatorios):
    with open("reporte_sueldos.csv", "w") as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"])
        for trabajador, sueldo in zip(trabajadores, sueldos_aleatorios):
            desc_salud = sueldo * 0.07
            desc_afp = sueldo * 0.12
            sueldo_liquido = sueldo - desc_salud - desc_afp
            writer.writerow([trabajador, sueldo, desc_salud, desc_afp, sueldo_liquido])
        print("Reporte_sueldos.csv creado exitosamente")
        
def salir_del_programa():
    print("Finalizando el programa ...")
    print("Desarrollado por Luis Torres")
    print("RUT 25.922.398-9")
            
sueldos_aleatorios = []

while True:
    print("**********[MENU DE OPCIONES]**********")
    print("1.- Asignar sueldos aleatorios")
    print("2.- Clasificar sueldos")
    print("3.- Ver estadisticas")
    print("4.- Reporte de sueldos")
    print("5.- Salir del programa")
    print("**************************************")
    try:
        opcion = int(input("Seleccionar una opcion (1-5): "))
        if opcion == 1:
            sueldos_aleatorios = asignar_sueldos_aleatorios()
            print("Sueldos aleatorios correctamente asignados")
        elif opcion == 2:
            if not sueldos_aleatorios:
                print("Debes ingresar sueldos aleatoriamente")
            else:
                clasificar_sueldos(trabajadores, sueldos_aleatorios)
        elif opcion == 3:
            if not sueldos_aleatorios:
                print("Debes ingresar sueldos aleatoriamente")
            else:
                ver_estadisticas(sueldos_aleatorios)
        elif opcion == 4:
            if not sueldos_aleatorios:
                print("Debes ingresar sueldos aleatoriamente")
            else:
                reporte_sueldos(trabajadores, sueldos_aleatorios)
        elif opcion == 5:
            salir_del_programa()
            break
        else:
            print("Opcion no valida")
    except ValueError:
        print("Debes ingresar un valor numerico del 1 al 5")