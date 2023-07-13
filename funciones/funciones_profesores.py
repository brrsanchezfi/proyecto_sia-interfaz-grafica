import sqlite3
from tabulate import tabulate 

from funciones.funciones_estudiantes import *


class profesor(estudiante):
    def __init__(self):
        self.DOC_PROFESOR=None
        self.NOM_PROFESOR=None
        self.APE_PROFESOR=None
        self.CODIGO_MATERIA=None
        self.HORA_INICIO_PROF=None
        self.HORAS_DICTADAS_PROF=None
        self.DIA_CLASE=None

    def BBDD_PROFESORES(self):
        conexion=sqlite3.connect("BBDD_DATOS.db")
        conexion.execute("PRAGMA foreign_keys = 1")
        cursor=conexion.cursor()

        sql=('''CREATE TABLE PROFESORES (DOC_PROFESOR VARCHAR(12) PRIMARY KEY,
            NOM_PROFESOR VARCHAR(30),
            APE_PROFESOR VARCHAR(30),
            COD_MATERIA_PROF VARCHAR(10),
            DIA_CLASE_PROF VARCHAR(10),
            HORA_INICIO_PROF INTEGER,
            HORAS_DICTADAS_PROF INTEGER, 
            FOREIGN KEY(COD_MATERIA_PROF) REFERENCES MATERIAS(COD_MATERIA)) 
            ''')
        try:
            cursor.execute(sql)
            cursor.close()
            conexion.close()

        except:
            print("la base de datos ya fue creada")

    def C_PROFESOR(self):
    
        conexion=sqlite3.connect("BBDD_DATOS.db")
        cursor=conexion.cursor()
        conexion.execute("PRAGMA foreign_keys = 1")

        self.DOC_PROFESOR=input("Ingrese el documento del profesor a  registrar: ")
        self.NOM_PROFESOR=input("Ingrese nombres del profesor: ")
        self.APE_PROFESOR=input("Ingrese apellidos del profesor: ")
        self.CODIGO_MATERIA = input("Ingrese codigo de la materia que dicta el profesor: ")
        self.DIA_CLASE = ""

        while True:
            DIAS = input('''ingrese el dia de la clase
                        1.LUNES
                        2.MARTES
                        3.MIERCOLES
                        4.JUEVES
                        5.VIERNES
                    opcion:''')

            if DIAS in ['1', '2', '3', '4', '5']:
                if DIAS == '1':
                    self.DIA_CLASE = "LUNES"
                    break
                if DIAS == '2':
                    self.DIA_CLASE = "MARTES"
                    break
                if DIAS == '3':
                    self.DIA_CLASE = "MIERCOLES"
                    break
                if DIAS == '4':
                    self.DIA_CLASE = "JUEVES"
                    break
                if DIAS == '5':
                    self.DIA_CLASE = "VIERNES"
                    break

        self.HORA_INICIO = input("Ingrese hora de inicio de la clase: ")
        self.HORAS_DICTADAS = input("Ingrese cantidas de horas dictadas por clase: ")

        DATOS_PROFESOR=(self.DOC_PROFESOR,self.NOM_PROFESOR,self.APE_PROFESOR,self.CODIGO_MATERIA,self.DIA_CLASE,self.HORA_INICIO,self.HORAS_DICTADAS)
        try:
            cursor.execute("INSERT INTO ESTUDIANTES(DOC_ESTUDIANTE,NOM_ESTUDIANTE,APE_ESTUDIANTE,COD_CARRERA,CALIDAD_ESTUDIANTE,PAPA_ACTUAL) VALUES ({},NULL,NULL,NULL,NULL,NULL)".format(self.DOC_PROFESOR))
            cursor.execute("DELETE FROM ESTUDIANTES WHERE DOC_ESTUDIANTE='{}'".format(self.DOC_PROFESOR))
            cursor.execute("INSERT INTO PROFESORES(DOC_PROFESOR, NOM_PROFESOR, APE_PROFESOR, COD_MATERIA_PROF, DIA_CLASE_PROF, HORA_INICIO_PROF, HORAS_DICTADAS_PROF) VALUES (?,?,?,?,?,?,?)",DATOS_PROFESOR)
            conexion.commit()
            cursor.close()
            conexion.close()
        except:
            print("error datos invalidos")

    def R_PROFESORES(self):
        conexion=sqlite3.connect("BBDD_DATOS.db")
        conexion.execute("PRAGMA foreign_keys = 1")
        cursor=conexion.cursor()
        lista = []
        lista2 = ["DOC_PROFESOR", "NOM_PROFESOR", "APE_PROFESOR", "COD_MATERIA_PROF", "DIA_CLASE_PROF", "HORA_INICIO_PROF","HORAS_DICTADAS_PROF","BUSCAR COD ESPECIFICO"]
        print("Por que campo desea ordenar la consulta:")
        for j in range(len(lista2)):
            print(str(j) + ")" + lista2[j])
        resp = input("Ingrese una opcion:")
        while ord(resp) < 48 or ord(resp) > ord(str(len(lista2) - 1)):
            resp = input("Opcion incorrecta, Ingrese una opcion valida:")
        if (resp != str(len(lista2) - 1)):

            try:
                cursor.execute("SELECT * FROM PROFESORES ORDER BY {}".format(lista2[int(resp)]))
                DATOS_MATERIAS = list(cursor.fetchall())
                cursor.close()
                conexion.close()
                for i in DATOS_MATERIAS:
                    lista.append(list(i))
                print(tabulate(lista))
            except:
                print("Error")
        else:
            codi = input("ingrese el codigo que desea buscar")
            try:
                cursor.execute("SELECT * FROM PROFESORES WHERE DOC_PROFESOR LIKE '%{}%'".format(codi))
                DATO_ESPECIFICO = list(cursor.fetchall())
                print(tabulate(DATO_ESPECIFICO))
                cursor.close()
                conexion.close()
            except:
                print("error")

        pause = input("enter para continuar: ")
        return

    def U_PROFESOR(self):
        conexion = sqlite3.connect("BBDD_DATOS.db")
        conexion.execute("PRAGMA foreign_keys = 1")
        cursor = conexion.cursor()

        self.DOC_PROFESOR = input("Ingrese el documento del Profesor que desea actualizar: ")
        self.DOC_PROFESOR_NEW = input("Ingrese el nuevo documento del Profesor: ")
        self.NOM_PROFESOR = input("Ingrese los nombres del Profesor: ")
        self.APE_PROFESOR = input("Ingrese los apellidos del Profesor: ")
        self.COD_MATERIA_PROF = input("Ingrese el codigo de la Materia que dicta: ")
        self.DIA_CLASE = ""
        while True:
            DIAS = input('''ingrese el dia de la clase
                                1.LUNES
                                2.MARTES
                                3.MIERCOLES
                                4.JUEVES
                                5.VIERNES
                            opcion:''')

            if DIAS in ['1', '2', '3', '4', '5']:
                if DIAS == '1':
                    self.DIA_CLASE = "LUNES"
                    break
                if DIAS == '2':
                    self.DIA_CLASE = "MARTES"
                    break
                if DIAS == '3':
                    self.DIA_CLASE = "MIERCOLES"
                    break
                if DIAS == '4':
                    self.DIA_CLASE = "JUEVES"
                    break
                if DIAS == '5':
                    self.DIA_CLASE = "VIERNES"
                    break

        self.HORA_INICIO = input("Ingrese hora de inicio de la clase: ")
        self.HORAS_DICTADAS = input("Ingrese cantidas de horas dictadas por clase: ")

        try:
            sql = ("UPDATE PROFESORES SET DOC_PROFESOR=" + "'" + self.DOC_PROFESOR_NEW + "'" +
                   ",NOM_PROFESOR=" + "'" + self.NOM_PROFESOR + "'" +
                   ",APE_PROFESOR=" + "'" + self.APE_PROFESOR + "'" +
                   ",COD_MATERIA_PROF=" + "'" + self.COD_MATERIA_PROF + "'" +
                   ",DIA_CLASE_PROF=" + "'" + self.DIA_CLASE + "'" +
                   ",HORA_INICIO_PROF=" + "'" + self.HORA_INICIO + "'" +
                   ",HORAS_DICTADAS_PROF=" + "'" + self.HORAS_DICTADAS + "'" +
                   "WHERE DOC_PROFESOR=" + "'" + self.DOC_PROFESOR + "'")
            cursor.execute(sql)
            conexion.commit()
            cursor.close()
            conexion.close()
            pause = input("Profesor actualizado")
        except sqlite3.IntegrityError:
            pause = input("El documento ya esta registrado en otro usuario: ")
            print(pause)

    # def D_PROFESOR(self):
    #     conexion = sqlite3.connect("BBDD_DATOS.db")
    #     cursor = conexion.cursor()

    #     DOC_PROFESOR_DEL = input("Ingrese el documento del Profesor que desea eliminar= ")

    #     try:
    #         cursor.execute("DELETE FROM PROFESORES WHERE DOC_PROFESOR='{}'".format(DOC_PROFESOR_DEL))
    #         conexion.commit()
    #         cursor.close()
    #         conexion.close()
    #         pause = input("El Profesor se borro correctamente")
    #         print(pause)
    #     except:
    #         pause = input("No hay datos")
    #         print(pause)

