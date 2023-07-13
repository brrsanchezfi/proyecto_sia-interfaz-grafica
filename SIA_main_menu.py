import PyQt5
import sqlite3
from funciones.funciones_materias import *
from funciones.funciones_estudiantes import *
from funciones.funciones_profesores import *
from mainwindows_estuduante import *


SEMESTRE=""


def menu():

    while True:
        print('''BIENVENIDOS AL NUEVO SIA

            1.CRED MATERIAS 
            2.CRED ESTUDIANTES
            3.CRED ESTUDIANTE GRAFICO
            4.CRED PROFESORES
            5.SALIR
            ''')

        opcion=input("Seleccione la opcion: ")

        if opcion in ['1','2','3','4','5']:

            if opcion=='1':
                Materias_menu()
            if opcion=='2':
                Estudiantes_menu()
            if opcion=='3':
                profesor3=profesor()
                profesor3.BBDD_PROFESORES()
                estudiante3=estudiante()
                estudiante3.BBDD_ESTUDIANTES()
                arrancarmenu()
            if opcion=='4':
                Profesor_menu()
            if opcion=='5':
                c=input("Vuelva pronto. Press Enter para salir")
                return

def Materias_menu():
    materias1=materias()
    materias1.BBDD_MATERIAS()

    
    while True:
        print('''MENU CRUD MATERIAS

        1.REGISTAR MATERIA
        2.CONSULTAR MATERIAS
        3.ACTUALIZAR MATERIAS 
        4.BORRAR MATERIA
        5.SALIR
        
        ''')
        opcion=input("Ingrese una opcion: ")

        if opcion in ['1','2','3','4','5']:

            if opcion=='1':
                materias1.C_MATERIA()              
            elif opcion=='2':
                materias1.R_MATERIAS()
            elif opcion=='3':
                materias1.U_MATERIA()
            elif opcion=='4':
                materias1.D_MATERIA()
            elif opcion=='5':
                return

def Estudiantes_menu():
    estudiantes1=estudiante()
    estudiantes1.BBDD_ESTUDIANTES()
    profesor2=profesor()
    profesor2.BBDD_PROFESORES()
    
    while True:
        print('''MENU CRUD Estudiante

       
        
        1.ACTUALIZAR ESTUDIANTE
        2.BORRAR ESTUDIANTE
        3.REGRISTRAR MATERIAS YA TOMADAS
        4.INSCRIBIR MATERIAS NUEVAS
        5.VER HORARIO DEL SEMESTRE
        6.VER HISTORIA ACADEMICA
        7.SALIR
        ''')
        opcion=input("Ingrese una opcion: ")

        if opcion in ['1','2','3','4','5','6','7']:
            if opcion=='1':
                estudiantes1.U_ESTUDIANTE()
            elif opcion=='2':
                estudiantes1.D_ESTUDIANTE('estudiante')
            elif opcion=='3':
                estudiantes1.MATS_ANT_ESTUDIANTE()
            elif opcion=='4':
                estudiantes1.C_BBDD_HORARIO_ESTUDIANTE("2020_02")
            elif opcion=='5':
                estudiantes1.R_HORARIO("2020_02")
            elif opcion=='6':
                estudiantes1.R_HIST_ACADEMICA()
            elif opcion=='7':
                return
        else:
            print("opcion incorrecta")

def Profesor_menu():
    profe=profesor()
    profe.BBDD_PROFESORES()
    estudiante2=estudiante()
    estudiante2.BBDD_ESTUDIANTES()

    while True:
        print('''MENU CRUD PROFESOR

        1.REGISTAR POFESOR
        2.VER TODOS LOS PROFESORES
        3.EDITAR DATOS PROFESOR
        4.BORRAR PROFESOR
        5.SALIR
        
        ''')
        opcion=input("Ingrese una opcion: ")

        if opcion in ['1','2','3','4','5']:

            if opcion=='1':
                profe.C_PROFESOR()
            elif opcion=='2':
                profe.R_PROFESORES()
            elif opcion=='3':
                profe.U_PROFESOR()
            elif opcion=='4':
                profe.D_ESTUDIANTE('profesor')
            elif opcion == '5':
                return

menu()


