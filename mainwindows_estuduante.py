
import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QLineEdit, QPushButton,QRadioButton,QTableWidget,QTableWidgetItem,QMessageBox
from funciones.funciones_estudiantes import *
import sqlite3
#from SIA_main_menu import menu


#from QTable import *


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi("main_win_estudiante.ui", self)     
        self.pushButton.clicked.connect(self.activar1)
        self.pushButton_2.clicked.connect(self.activar2)
        self.pushButton_9.clicked.connect(sys.exit)       #salir

    def activar1(self):
        
        registrar=Dialog()
        registrar.show()
        registrar.exec_()
    
    def activar2(self):
        buscar=Dialog_Buscador()
        buscar.show()
        buscar.exec_()
        

class Dialog(QDialog): #registrar
    def __init__(self):
        super(Dialog,self).__init__()
        uic.loadUi("1_REGISTRAR_ESTUDIANTE.ui", self) 
        self.pushButton.clicked.connect(self.registrar_estudiante)
        self.radio=None
        self.radioButton.toggled.connect(self.calidad)
        self.radioButton_2.toggled.connect(self.calidad)
        self.radioButton_3.toggled.connect(self.calidad)
        self.pushButton_2.clicked.connect(self.salir)#salir

    def salir(self):
        self.accept()

    def calidad(self):

        self.radio = self.sender()

    def registrar_estudiante(self):
        DOC_EST=self.lineEdit.text()
        NOM_EST=self.lineEdit_2.text()
        APE_EST=self.lineEdit_3.text()
        COD_CAR=self.lineEdit_4.text()
        CALIDAD_EST=self.radio.text()

        estudiante1=estudiante()

        estudiante1.C_ESTUDIANTE(DOC_EST,NOM_EST,APE_EST,COD_CAR,CALIDAD_EST)
        

class Dialog_Buscador(QDialog):
    def __init__(self):
        super(Dialog_Buscador,self).__init__()
        uic.loadUi("2_BUSCADOR_ESTUDIANTE.ui", self)
        self.pushButton.clicked.connect(self.lista_1) 
        self.pushButton_2.clicked.connect(self.lista_2) 
        
    def lista_1(self):#ordenar por argumentos

        conexion=sqlite3.connect("BBDD_DATOS.db")
        cursor=conexion.cursor()
        lista=[]
        try:
            cursor.execute("SELECT * FROM ESTUDIANTES ORDER BY {}".format(str(self.comboBox.itemText(self.comboBox.currentIndex()))))
            DATOS_MATERIAS = list(cursor.fetchall())
            cursor.close()
            conexion.close()
            for i in DATOS_MATERIAS:
                lista.append(list(i))
        except:
            QMessageBox.about(self, "Error", "No encontrado")

        lista_1=Dialog_Buscador_lista()
        lista_1.mostrar_lista(lista)
        lista_1.show()
        lista_1.exec_()

    def lista_2(self):#buscar un solo estudiante

        conexion=sqlite3.connect("BBDD_DATOS.db")
        cursor=conexion.cursor()

        try:
            if self.lineEdit.text()=='':
                print(0/0)
            
            cursor.execute("SELECT * FROM ESTUDIANTES WHERE DOC_ESTUDIANTE = '{}'".format(self.lineEdit.text()))
            DATO_ESPECIFICO = list(cursor.fetchall())
            cursor.close()
            conexion.close()

        except:
            QMessageBox.about(self, "Error", "No encontrado")

        lista_2=Dialog_Buscador_lista()
        try:
            lista_2.mostrar_lista(DATO_ESPECIFICO)
        except:
            pass
        lista_2.show()
        lista_2.exec_()


class Dialog_Buscador_lista(QDialog):
    def __init__(self):
        super(Dialog_Buscador_lista,self).__init__()
        uic.loadUi("2_1_LISTA_ESTUDIANTES.ui", self)   
        
        self.tableWidget.setColumnCount(6)

    def mostrar_lista(self, datos):
        self.tableWidget.setRowCount(len(datos))
        row=0
        try:
            for i in datos:
                col=0
                for j in i:
                    cellinfo=QTableWidgetItem(j)
                    self.tableWidget.setItem(row, col, cellinfo)
                    col+=1
                row+=1
        except:
            QMessageBox.about("Error", "No encontrado")
   

def arrancarmenu():
    
    app = QApplication(sys.argv)
    GUI = MainWindow()
    GUI.show()
    app.exec_()
   



