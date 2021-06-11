""" Reto 6 Informes de Vacunacion
    incorpora al modulo informe_vacuna.py
    Tu nombre aquí
    Junio XX-XX """

#---------------- Zona librerias------------
#-*- coding: utf-8 -*-
import informe_vacuna as iv
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================


#----------Definición de Funciones (Dividir)------------
def menu():
    print("\n")
    print("=======================================================")
    print("Bienvenido al Reto 6")
    print("Vacunas:\n")
    print("1. Cargar datos ejemplo")
    print("2. Manual")
    print("3. Listar Datos")
    print("4. Grafico General")
    print("5. Salir")
    print(" ")
    op=int(input("Seleccione una opcion:  "))
    return op

#Programa de Caida Libre
flag=1
while flag==1:
    op=menu()
    if op==1: lista_pacientes=iv.leer_archivo()
    elif op==2: iv.grafico_etapas(lista_pacientes)     
    elif op==3: iv.grafico_vacunas(lista_pacientes)   #iv.listar_datos(lista_pacientes)
    elif op==4: iv.grafico_general(lista_pacientes)
    elif op==5: break
    else: print("Opción no valida, intente de nuevo")

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación
# =====================================================================


#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================