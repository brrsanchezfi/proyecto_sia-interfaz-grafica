import sqlite3
from tabulate import tabulate 
from tkinter import messagebox




#from funciones.funciones_materias import *
# from funciones.funciones_estudiantes import *
#from funciones_profesores import *

class estudiante():

    def __init__(self):
        self.DOC_ESTUDIANTE=None
        self.NOM_ESTUDIANTE =None
        self.APE_ESTUDIANTE =None
        self.COD_CARRERA =None
        self.CALIDAD_ESTUDIANTE=None 
        self.PAPA_ACTUAL=None

    def BBDD_ESTUDIANTES(self):
        conexion=sqlite3.connect("BBDD_DATOS.db")
        cursor=conexion.cursor()

        sql=('''CREATE TABLE ESTUDIANTES (DOC_ESTUDIANTE VARCHAR(12) PRIMARY KEY,
            NOM_ESTUDIANTE VARCHAR(30),
            APE_ESTUDIANTE VARCHAR(30),
            COD_CARRERA VARCHAR(10),
            CALIDAD_ESTUDIANTE VARCHAR(15),
            PAPA_ACTUAL INTEGER)''')
        try:
            cursor.execute(sql)
            cursor.close()
            conexion.close()

        except:
            print("la base de datos ya fue creada")

    def C_BBDD_HISTORIA_ACADEMICA_ESTUDIANTES(self,docu):
        conexion=sqlite3.connect("BBDD_HISTORIA_ACADEMICA.db")
        cursor=conexion.cursor()
        try:
            cursor.execute("CREATE TABLE HISTORIA_ACADEMICA_{}(DOC VARCHAR(12), COD_MATERIA VARCHAR(10), CREDITOS INTEGER,NOTA INTEGER)".format(docu))
            conexion.commit()
            cursor.close()
            conexion.close()
        except:
            pause=input("Ha ocurrido un error")

    def C_ESTUDIANTE(self, DOC_EST, NOM_EST, APE_EST, COD_CAR, CALIDAD_EST):
        conexion=sqlite3.connect("BBDD_DATOS.db")
        cursor=conexion.cursor()

        self.DOC_ESTUDIANTE =DOC_EST
        self.NOM_ESTUDIANTE =NOM_EST
        self.APE_ESTUDIANTE =APE_EST
        self.COD_CARRERA =COD_CAR
        self.CALIDAD_ESTUDIANTE=CALIDAD_EST    
        
        DATOS_ESTUDIANTE=(self.DOC_ESTUDIANTE,self.NOM_ESTUDIANTE,self.APE_ESTUDIANTE,self.COD_CARRERA,self.CALIDAD_ESTUDIANTE)
        try:
            cursor.execute("INSERT INTO PROFESORES(DOC_PROFESOR, NOM_PROFESOR, APE_PROFESOR, COD_MATERIA_PROF, DIA_CLASE_PROF, HORA_INICIO_PROF, HORAS_DICTADAS_PROF) VALUES ({},NULL,NULL,NULL,NULL,NULL,NULL)".format(self.DOC_ESTUDIANTE))
            cursor.execute("DELETE FROM PROFESORES WHERE DOC_PROFESOR='{}'".format(self.DOC_ESTUDIANTE))
            cursor.execute("INSERT INTO ESTUDIANTES(DOC_ESTUDIANTE,NOM_ESTUDIANTE,APE_ESTUDIANTE,COD_CARRERA,CALIDAD_ESTUDIANTE,PAPA_ACTUAL) VALUES (?,?,?,?,?,NULL)",DATOS_ESTUDIANTE)
            
            conexion.commit()
            self.C_BBDD_HISTORIA_ACADEMICA_ESTUDIANTES(self.DOC_ESTUDIANTE)
            cursor.close()
            conexion.close()
            print("REGISTRADO")
        except sqlite3.IntegrityError:
            print("dato repetido")
            #messagebox.showinfo("documento en uso", "error")

    def R_ESTUDIANTES(self):
        conexion=sqlite3.connect("BBDD_DATOS.db")
        cursor=conexion.cursor()
        lista = []
        lista2 = ["DOC_ESTUDIANTE", "NOM_ESTUDIANTE", "APE_ESTUDIANTE", "COD_CARRERA", "CALIDAD_ESTUDIANTE", "PAPA_ACTUAL","BUSCAR COD ESPECIFICO"]
        print("Por que campo desea ordenar la consulta:")
        for j in range(len(lista2)):
            print(str(j) + ")" + lista2[j])

        resp = input("Ingrese una opcion:")

        while ord(resp) < 48 or ord(resp) > ord(str(len(lista2) - 1)):
            resp = input("Opcion incorrecta, Ingrese una opcion valida:")
        if (resp != str(len(lista2) - 1)):

            try:
                cursor.execute("SELECT * FROM ESTUDIANTES ORDER BY {}".format(lista2[int(resp)]))
                DATOS_MATERIAS = list(cursor.fetchall())
                cursor.close()
                conexion.close()
                for i in DATOS_MATERIAS:
                    lista.append(list(i))
                print(tabulate(lista))
            except:
                print("Error")
        else:
            codi = input("ingrese el documento que desea buscar")
            try:
                cursor.execute("SELECT * FROM ESTUDIANTES WHERE DOC_ESTUDIANTE LIKE '%{}%'".format(codi))
                DATO_ESPECIFICO = list(cursor.fetchall())
                print(tabulate(DATO_ESPECIFICO))
                cursor.close()
                conexion.close()
            except:
                print("error")

        pause = input("enter para continuar: ")
        return

    def U_ESTUDIANTE(self):
        conexion=sqlite3.connect("BBDD_DATOS.db")
        cursor=conexion.cursor()

        self.DOC_ESTUDIANTE=input("Ingrese el documento del estudiante que desea actualizar: ")
        self.DOC_ESTUDIANTE_NEW =input("Ingrese el nuevo documento del estudiente: ")
        self.NOM_ESTUDIANTE =input("Ingrese los nombres del estudiante: ")
        self.APE_ESTUDIANTE =input("Ingrese los apellidos del estudiante: ")
        self.COD_CARRERA =input("Ingrese el codigo de la carrera: ")
        self.CALIDAD_ESTUDIANTE=""     
        while True:
            opcion =input('''Escoja la calidad de estudiante 
                1.Matriculado
                2.Graduado
                3.Pérdida de cupo 

                Opcion:''')

            if opcion in ['1','2','3']:
                if opcion=='1':
                    self.CALIDAD_ESTUDIANTE="Matriculado"
                    break
                elif opcion=='2':
                    self.CALIDAD_ESTUDIANTE="Graduado"
                    break
                elif opcion=='3':
                    self.CALIDAD_ESTUDIANTE="Pérdida de cupo"
                    break
            else:
                pause=input("opcion no valida, reintentar")

        try:
            sql=("UPDATE ESTUDIANTES SET DOC_ESTUDIANTE=" +"'"+ self.DOC_ESTUDIANTE_NEW +"'"+
                ",NOM_ESTUDIANTE=" +"'"+ self.NOM_ESTUDIANTE +"'"+
                ",APE_ESTUDIANTE=" +"'"+ self.APE_ESTUDIANTE +"'"+
                ",COD_CARRERA=" +"'"+ self.COD_CARRERA +"'"+
                ",CALIDAD_ESTUDIANTE="+"'"+self.CALIDAD_ESTUDIANTE+"'"+
                "WHERE DOC_ESTUDIANTE="+"'"+ self.DOC_ESTUDIANTE+"'")
            cursor.execute(sql)
            conexion.commit()
            cursor.close()
            conexion.close()
            pause=input("Estudiante actualizado")
        except sqlite3.IntegrityError:
            pause=input("El documento ya esta registrado en otro usuario: ")
            print(pause)

    def D_ESTUDIANTE(self, tabla):

        conexion=sqlite3.connect("BBDD_DATOS.db")
        cursor=conexion.cursor()
        
        DOC_ESTUDIANTE_DEL=input("Ingrese el documento del estudiante que desea eliminar= ")
        p=''
        c=''
        if tabla=='estudiante':
            p='ESTUDIANTES'
            c='DOC_ESTUDIANTE'
      
        elif tabla=='profesor':
            p='PROFESORES'
            c='DOC_PROFESOR'
        


        try:
            sql=("DELETE FROM {} WHERE {}={}".format(p,c,DOC_ESTUDIANTE_DEL))
            print(sql)
            cursor.execute(sql)
            conexion.commit()
            cursor.close()
            conexion.close()
            pause=input("El "+ tabla + " se borro correctamente")
            print(pause)
        except:
            pause=input("No hay datos")
            print(pause)



            
            

    def MATS_ANT_ESTUDIANTE(self):
        while True:
            c = input("Desea continuar e ingresar materias ya vistas a un estudiante: s/n")
            while c != "s" and c != "n":
                c = input("Opcion incorrecta, continuar e inscribir materias?: s/n")
            if c == "n":
                break
            DOC_ESTUDIANTE_C_HORARIO = input("Ingrese el documento del estudiante para ingresar materias ya tomadas")
            conexion = sqlite3.connect("BBDD_HISTORIA_ACADEMICA.db")
            cursor = conexion.cursor()
            try:
                cursor.execute("SELECT COD_MATERIA FROM HISTORIA_ACADEMICA_{}".format(DOC_ESTUDIANTE_C_HORARIO))
                DATOS_P = list(cursor.fetchall())
                cursor.close()
                conexion.close()
            except:
                t=input("El documento no existe, Enter para continuar")
                conexion.close()
                continue
            DATOS = []
            for h in range(len(DATOS_P)):
                DATOS.append(DATOS_P[h][0])
            while True:
                d = input("Desea continuar con el estudiante{}: s/n".format(DOC_ESTUDIANTE_C_HORARIO))
                while d != "s" and d != "n":
                    d = input("Opcion incorrecta, continuar e inscribir materias?: s/n")
                if d == "n":
                    break
                conexion = sqlite3.connect("BBDD_DATOS.db")
                cursor = conexion.cursor()
                COD_MATERIA_INSCRIBIR = input("Ingrese el codigo de la materia a ingresar a la historia academica")
                try:
                    cursor.execute("SELECT NOM_MATERIA,NUM_CREDITOS,COD_MATERIA_PRE FROM MATERIAS WHERE COD_MATERIA='{}'".format(COD_MATERIA_INSCRIBIR))
                    DATOS_PRERRE = list(cursor.fetchall())
                    if (DATOS_PRERRE[0][2] != ""):
                        print(DATOS_PRERRE[0][2])
                        print(DATOS)
                        if (DATOS_PRERRE[0][2] not in DATOS):
                            k=input("¡ERROR!, No puede haber visto esta materia sin haber visto sus prerrequisitos, Enter para continuar")
                            conexion.close()
                            continue
                except:
                    conexion.close()
                    t=input("Error, el codigo de la materia no existe, Enter para continuar")
                    continue
                conexion = sqlite3.connect("BBDD_HISTORIA_ACADEMICA.db")
                cursor = conexion.cursor()
                try:
                    DAT_HIST_ACAD = [DOC_ESTUDIANTE_C_HORARIO, COD_MATERIA_INSCRIBIR, DATOS_PRERRE[0][1]]
                    cursor.execute("INSERT INTO HISTORIA_ACADEMICA_{}(DOC,COD_MATERIA,CREDITOS,NOTA) VALUES (?,?,?,NULL)".format(DOC_ESTUDIANTE_C_HORARIO), DAT_HIST_ACAD)
                    conexion.commit()
                    cursor.close()
                    conexion.close()
                except:
                    t=input("algun Error ha ocurrido, Enter para continuar")
                    conexion.close()
                    continue

    def C_BBDD_HORARIO_ESTUDIANTE(self,SEMESTRE):
        while True:
            c=input("Desea continuar e inscribir materias: s/n")
            while c!="s" and c!="n":
                c = input("Opcion incorrecta, continuar e inscribir materias?: s/n")
            if c=="n":
                break
            DOC_ESTUDIANTE_C_HORARIO = input("Ingrese el documento del estudiante que desea incribir materia")
            conexion = sqlite3.connect("BBDD_HISTORIA_ACADEMICA.db")
            cursor = conexion.cursor()
            try:
                cursor.execute("SELECT COD_MATERIA FROM HISTORIA_ACADEMICA_{}".format(DOC_ESTUDIANTE_C_HORARIO))
                DATOS_P = list(cursor.fetchall())
                cursor.close()
                conexion.close()
            except:
                t=input("El documento es incorrecto, Enter para continua")
                conexion.close()
                continue
            DATOS=[]
            for h in range(len(DATOS_P)):
                DATOS.append(DATOS_P[h][0])
            conexion = sqlite3.connect("BBDD_DATOS.db")
            cursor = conexion.cursor()
            try:
                cursor.execute("SELECT NOM_ESTUDIANTE,APE_ESTUDIANTE,COD_CARRERA,CALIDAD_ESTUDIANTE FROM ESTUDIANTES WHERE DOC_ESTUDIANTE='{}'".format(DOC_ESTUDIANTE_C_HORARIO))
                CALIDAD = list(cursor.fetchall())
            except:
                t=input("Un Error ha ocurrido, Enter para continuar")
                conexion.close()
                continue
            if(CALIDAD[0][3]!="Matriculado"):
                t=input("el usuario no esta habilitado para inscribir materias, Enter para continuar")
                conexion.close()
                continue
            while True:
                d = input("Desea inscribir con {}: s/n".format(DOC_ESTUDIANTE_C_HORARIO))
                while d != "s" and d != "n":
                    d = input("Opcion incorrecta, continuar e inscribir materias?: s/n")
                if d == "n":
                    break
                conexion = sqlite3.connect("BBDD_DATOS.db")
                cursor = conexion.cursor()
                COD_MATERIA_INSCRIBIR = input("Ingrese el codigo de la materia que desea incribir")
                try:
                    cursor.execute("SELECT NOM_MATERIA,NUM_CREDITOS,COD_MATERIA_PRE FROM MATERIAS WHERE COD_MATERIA='{}'".format(COD_MATERIA_INSCRIBIR))
                    DATOS_PRERRE = list(cursor.fetchall())
                    if(DATOS_PRERRE[0][2] != ""):
                        print(DATOS_PRERRE[0][2])
                        print(DATOS)
                        if(DATOS_PRERRE[0][2] not in DATOS):
                            print("No cuenta con los prerrequisitos para inscribir esta materia")
                            conexion.close()
                            continue
                except:
                    t=input("Error, ¡El codigo no existe!, Enter para continuar")
                    conexion.close()
                    continue
                try:
                    cursor.execute("SELECT NOM_PROFESOR,APE_PROFESOR,DIA_CLASE_PROF, HORA_INICIO_PROF, HORAS_DICTADAS_PROF FROM PROFESORES WHERE COD_MATERIA_PROF='{}'".format(COD_MATERIA_INSCRIBIR))
                    DATOS1 = list(cursor.fetchall())
                    cursor.close()
                    conexion.close()
                except:
                    t=input("Error al ejecutar, Enter para continuar")
                    conexion.close()
                    continue
                if(len(DATOS1)==0):
                    t=input("No hay maestro dictando esta materia ahora mismo, Enter para continuar")
                    continue
                print("los siguientes maestros dictan la misma clase, ejia uno:")
                for l in range(len(DATOS1)):
                    print(str(l)+")",DATOS1[l])
                elecc=input()
                while (ord(elecc)<48 or ord(elecc)>ord(str(len(DATOS1)-1))):
                    elecc=input("Opcion incorrecta, Ingrese una opcion valida:")
                DATOS1=DATOS1[int(elecc)]
                conexion = sqlite3.connect("BBDD_HORARIO_ESTUDIANTES.db")
                cursor = conexion.cursor()
                try:
                    cursor.execute("CREATE TABLE HORARIO_" + SEMESTRE + "_{}(COD_MATERIA VARCHAR(10) UNIQUE,NOM_MATERIA VARCHAR(30),NUM_CREDITOS INTEGER,NOM_PROF VARCHAR(30),APE_PROF VARCHAR(30), DIA_CLASE VARCHAR(10),HORA_INICIO INTEGER,HORAS_DICTADAS INTEGER)".format(DOC_ESTUDIANTE_C_HORARIO))
                    conexion.commit()
                except:
                    print("realizando analisis")
                try:
                    cursor.execute("SELECT DIA_CLASE, HORA_INICIO, HORAS_DICTADAS FROM HORARIO_" + SEMESTRE + "_{}".format(DOC_ESTUDIANTE_C_HORARIO))
                    DATOS_HORARIO = list(cursor.fetchall())
                except:
                    print("Error analizando base de datos")
                    conexion.close()
                    continue
                continuar=True
                for y in range(len(DATOS_HORARIO)):
                    if(DATOS1[2]==DATOS_HORARIO[y][0]):
                        if(DATOS1[3]+DATOS1[4]>DATOS_HORARIO[y][1] and DATOS1[3]+DATOS1[4]<DATOS_HORARIO[y][1]+DATOS_HORARIO[y][2]):
                            print("Hay clases solapandose")
                            continuar=False
                            break
                if(continuar==False):
                    conexion.close()
                    continue
                try:
                    print(DATOS_PRERRE)
                    print(DATOS1)
                    DATOS_MATERIA=[COD_MATERIA_INSCRIBIR,DATOS_PRERRE[0][0],DATOS_PRERRE[0][1],DATOS1[0],DATOS1[1],DATOS1[2],DATOS1[3],DATOS1[4]]
                    cursor.execute("INSERT INTO HORARIO_" + SEMESTRE + "_{}(COD_MATERIA,NOM_MATERIA,NUM_CREDITOS,NOM_PROF,APE_PROF, DIA_CLASE,HORA_INICIO,HORAS_DICTADAS) VALUES (?,?,?,?,?,?,?,?)".format(DOC_ESTUDIANTE_C_HORARIO),DATOS_MATERIA)
                    conexion.commit()
                    cursor.close()
                    conexion.close()
                except:
                    print("error al inscribir materia")
                    conexion.close()
                    continue
                conexion = sqlite3.connect("BBDD_ALUMNOS_IN_ASIGNATURA.db")
                cursor = conexion.cursor()
                try:
                    cursor.execute("CREATE TABLE HORARIO_ASIGNATURA_" + SEMESTRE + "_{}(DOC_ESTUDIANTE VARCHAR(12) PRIMARY KEY,NOM_ESTUDIANTE VARCHAR(30),APE_ESTUDIANTE VARCHAR(30),COD_CARRERA VARCHAR(10),NOTA INTEGER)".format(COD_MATERIA_INSCRIBIR))
                    conexion.commit()
                except:
                    print("Ingresando datos a lista de clase")
                DAT_HOR_ASIG=[DOC_ESTUDIANTE_C_HORARIO,CALIDAD[0][0],CALIDAD[0][1],CALIDAD[0][2]]
                try:
                    cursor.execute("INSERT INTO HORARIO_ASIGNATURA_" + SEMESTRE + "_{}(DOC_ESTUDIANTE,NOM_ESTUDIANTE,APE_ESTUDIANTE,COD_CARRERA,NOTA) VALUES (?,?,?,?,NULL)".format(COD_MATERIA_INSCRIBIR), DAT_HOR_ASIG)
                    conexion.commit()
                    cursor.close()
                    conexion.close()
                except:
                    t=input("algo raro ha pasado, Enter para continuar")
                    conexion.close()
                    continue

                conexion = sqlite3.connect("BBDD_HISTORIA_ACADEMICA.db")
                cursor = conexion.cursor()
                try:
                    DAT_HIST_ACAD = [DOC_ESTUDIANTE_C_HORARIO,COD_MATERIA_INSCRIBIR,DATOS_PRERRE[0][1]]
                    cursor.execute("INSERT INTO HISTORIA_ACADEMICA_{}(DOC,COD_MATERIA,CREDITOS,NOTA) VALUES (?,?,?,NULL)".format(DOC_ESTUDIANTE_C_HORARIO), DAT_HIST_ACAD)
                    conexion.commit()
                    cursor.close()
                    conexion.close()

                except:
                    t=input("algo raro ha pasado X2")
                    conexion.close()
                    continue
        return

    def R_HORARIO(self,SEMESTRE):
        DOC_ESTUDIANTE = input("Ingrese el documento del estudiante: ")
        lista = []
        lista2 = ["COD_MATERIA", "NOM_MATERIA", "NUM_CREDITOS", "NOM_PROF","APE_PROF","DIA_CLASE","HORA_INICIO","HORAS_DICTADAS","BUSCAR COD MATERIA ESPECIFICO"]
        print("Por que campo desea ordenar la consulta:")
        for j in range(len(lista2)):
            print(str(j) + ")" + lista2[j])
        resp = input("Ingrese una opcion:")
        while ord(resp) < 48 or ord(resp) > ord(str(len(lista2) - 1)):
            resp = input("Opcion incorrecta, Ingrese una opcion valida:")
        conexion = sqlite3.connect("BBDD_HORARIO_ESTUDIANTES.db")
        cursor = conexion.cursor()
        if (resp != str(len(lista2) - 1)):
            try:
                sql = ("SELECT * FROM HORARIO_" + SEMESTRE + "_{} ORDER BY {}".format(DOC_ESTUDIANTE, lista2[int(resp)]))
                cursor.execute(sql)
                Horario = cursor.fetchall()
                print(tabulate(Horario))
                cursor.close()
                conexion.close()
                pause = input("continuar")
            except:
                pause = input("Documento no encontrado")
                conexion.close()
        else:
            codi = input("ingrese el codigo que desea buscar")
            try:
                cursor.execute("SELECT * FROM HORARIO_"+SEMESTRE+"_{} WHERE COD_MATERIA LIKE '%{}%'".format(DOC_ESTUDIANTE,codi))
                DATO_ESPECIFICO = list(cursor.fetchall())
                print(tabulate(DATO_ESPECIFICO))
                pause=input("Enter para continuar")
                cursor.close()
                conexion.close()
            except:
                pause=input("Codigo Erroneo, Enter para continuar")
                conexion.close()

    def R_HIST_ACADEMICA(self):
        DOC_ESTUDIANTE = input("Ingrese el documento del estudiante: ")
        lista = []
        lista2 = ["DOC", "COD_MATERIA", "CREDITOS", "NOTA"]
        print("Por que campo desea ordenar la consulta:")
        for j in range(len(lista2)):
            print(str(j) + ")" + lista2[j])
        resp = input("Ingrese una opcion:")
        while ord(resp) < 48 or ord(resp) > ord(str(len(lista2) - 1)):
            resp = input("Opcion incorrecta, Ingrese una opcion valida:")
        conexion=sqlite3.connect("BBDD_HISTORIA_ACADEMICA.db")
        cursor=conexion.cursor()
        try:
            sql = ("SELECT COD_MATERIA,CREDITOS,NOTA FROM HISTORIA_ACADEMICA_{} ORDER BY {}".format(DOC_ESTUDIANTE,lista2[int(resp)]))
            cursor.execute(sql)
            Historia=cursor.fetchall()
            print(tabulate(Historia))
            cursor.close()
            conexion.close()
            pause=input("continuar")
        except:
            pause=input("Documento no encontrado")
            conexion.close()



import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


