import sqlite3
import PyQt5
from tabulate import tabulate 

class materias:
    def __init__(self):
        self.__COD_MATERIA=None
        self.__NOM_MATERIA=None
        self.__COD_FACULTAD=None
        self.__COD_DEPARTAMENTO=None
        self.__NUM_CREDITOS=None
        self.__COD_MATERIA_PRE=None

    def getCOD_MATERIA(self):
        
            return self.__COD_MATERIA,self.__NOM_MATERIA,self.__COD_FACULTAD,self.__COD_DEPARTAMENTO,self.__NUM_CREDITOS,self.__COD_MATERIA_PRE

    def setCOD_MATERIA(self, COD_MATERIA,NOM_MATERIA,COD_FACULTAD,COD_DEPARTAMENTO,NUM_CREDITOS,COD_MATERIA_PRE):
        self.__COD_MATERIA=COD_MATERIA
        self.__NOM_MATERIA=NOM_MATERIA
        self.__COD_FACULTAD=COD_FACULTAD
        self.__COD_DEPARTAMENTO=COD_DEPARTAMENTO
        self.__NUM_CREDITOS=NUM_CREDITOS
        self.__COD_MATERIA_PRE=COD_MATERIA_PRE
       
    def C_MATERIA(self):
        conexion=sqlite3.connect("BBDD_DATOS.db")
        cursor=conexion.cursor()

        COD_MATERIA = input("Ingrese el codigo de la materia: ")
        NOM_MATERIA = input("Ingrese el nombre de la materia: ")
        COD_FACULTAD = input("Ingrese el codigo de la facultad: ")
        COD_DEPARTAMENTO = input("Ingrese el departameto: ")
        NUM_CREDITOS = input("Ingrese el numero de creditos: ")
        COD_MATERIA_PRE = input("Ingrese el codigo de la materia pre-requisito: ")

        self.setCOD_MATERIA(COD_MATERIA,NOM_MATERIA,COD_FACULTAD,COD_DEPARTAMENTO,NUM_CREDITOS,COD_MATERIA_PRE)
    
        DATOS_MATERIAS=self.getCOD_MATERIA()

        try:
            cursor.execute('''INSERT INTO MATERIAS (COD_MATERIA,NOM_MATERIA,COD_FACULTAD,COD_DEPARTAMENTO,NUM_CREDITOS,COD_MATERIA_PRE) VALUES (?,?,?,?,?,?)''',DATOS_MATERIAS)
            conexion.commit()
            cursor.close()
            conexion.close()
        except sqlite3.IntegrityError:
            pause=input("El codigo ya esta en uso: ")
            print(pause)

    def BBDD_MATERIAS(self):
        conexion=sqlite3.connect("BBDD_DATOS.db")
        cursor=conexion.cursor()

        try:
            cursor.execute('''CREATE TABLE MATERIAS(COD_MATERIA VARCHAR(10) PRIMARY KEY,
                            NOM_MATERIA VARCHAR(20),
                            COD_FACULTAD VARCHAR(10),
                            COD_DEPARTAMENTO VARCHAR(10),
                            NUM_CREDITOS INTEGER,
                            COD_MATERIA_PRE VARCHAR(10))
                            ''')
            cursor.close()
            conexion.close()
        except sqlite3.OperationalError:
            print("la DB ya fue creada")
       
    def R_MATERIAS(self):
        conexion=sqlite3.connect("BBDD_DATOS.db")
        cursor=conexion.cursor()
        lista=[]
        lista2=["COD_MATERIA","NOM_MATERIA","COD_FACULTAD","COD_DEPARTAMENTO","NUM_CREDITOS","COD_MATERIA_PRE","BUSCAR COD ESPECIFICO"]
        print("Por que campo desea ordenar la consulta:")
        for j in range(len(lista2)):
            print(str(j)+")"+lista2[j])
        resp=input("Ingrese una opcion:")
        while ord(resp)<48 or ord(resp)>ord(str(len(lista2)-1)):
            resp = input("Opcion incorrecta, Ingrese una opcion valida:")
        if(resp!=str(len(lista2)-1)):

            try:
                cursor.execute("SELECT * FROM MATERIAS ORDER BY {}".format(lista2[int(resp)]))
                DATOS_MATERIAS=list(cursor.fetchall())
                cursor.close()
                conexion.close()
                for i in DATOS_MATERIAS:
                    lista.append(list(i))
                print(tabulate(lista))
            except:
                print("Error")
        else:
            codi=input("ingrese el codigo que desea buscar")
            try:
                cursor.execute("SELECT * FROM MATERIAS WHERE COD_MATERIA LIKE '%{}%'".format(codi))
                DATO_ESPECIFICO = list(cursor.fetchall())
                print(tabulate(DATO_ESPECIFICO))
                cursor.close()
                conexion.close()
            except:
                print("error")

        pause=input("enter para continuar: ")
        return

    def U_MATERIA(self):
        conexion=sqlite3.connect("BBDD_DATOS.db")
        cursor=conexion.cursor()

        COD_MATERIA = input("Ingrese el codigo de la materia: ")
        COD_MATERIA_NEW = input("Ingrese el nuevo codigo de la materia: ")
        NOM_MATERIA = input("Ingrese el nombre de la materia: ")
        COD_FACULTAD = input("Ingrese el codigo de la facultad: ")
        COD_DEPARTAMENTO = input("Ingrese el departameto: ")
        NUM_CREDITOS = input("Ingrese el numero de creditos: ")
        COD_MATERIA_PRE = input("Ingrese el codigo de la materia pre-requisito: ")
        
        try:
            sql=("UPDATE MATERIAS SET COD_MATERIA=" +"'"+COD_MATERIA_NEW+"'"+
                ",NOM_MATERIA=" +"'"+NOM_MATERIA+"'"+
                ",COD_FACULTAD=" +"'"+COD_FACULTAD+"'"+
                ",COD_DEPARTAMENTO=" +"'"+COD_DEPARTAMENTO+"'"+
                ",NUM_CREDITOS=" +"'"+NUM_CREDITOS+"'"+
                ",COD_MATERIA_PRE=" +"'"+COD_MATERIA_PRE+"'"+
                " WHERE COD_MATERIA="+"'"+COD_MATERIA+"'")
            cursor.execute(sql)
            conexion.commit()
            cursor.close()
            conexion.close()
        except sqlite3.IntegrityError:
            pause=input("ERROR EN LOS DATOS INGRESADOS: ")
            print(pause)

    def D_MATERIA(self):
        conexion=sqlite3.connect("BBDD_DATOS.db")
        cursor=conexion.cursor()
        
        COD_MATERIA_DELETE=input("Ingrese el codigo de la materia que desea eliminar= ")

        try:
            cursor.execute("DELETE FROM MATERIAS WHERE COD_MATERIA='{}'".format(COD_MATERIA_DELETE))
            conexion.commit()
            cursor.close()
            conexion.close()
        except:
            print("Error")
            pause=input("Enter para Salir")


