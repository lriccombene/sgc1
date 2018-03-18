import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_ejercicio import Ui_form_ejercicio
from PyQt5.QtCore import pyqtRemoveInputHook
from E_cliente import E_cliente
from E_ejercicio import E_ejercicio
from E_ejercicio_detalle import E_ejercicio_detalle
from w_form_ejercicio_nuevo import ejercicio_nuevo

class ejercicio(QDialog):
    obj_form= Ui_form_ejercicio()
    obj_cliente=""
    lista_ejercicio =""
    list_detalle =""
    index=""

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_ejercicio()
        self.obj_form.setupUi(self)
        self.obj_form.btn_buscar.clicked.connect(self.buscar)
        self.obj_form.btn_cerrar.clicked.connect(self.cerrar)
        self.obj_form.tw_ejercicio.cellClicked.connect(self.seleccion_item_ejercicio)
        self.obj_form.tw_detalle_ejerc.cellClicked.connect(self.seleccion_item_detalle)
        self.obj_form.btn_nuevo.clicked.connect(self.nuevo)

    def nuevo(self):
        self.form_ejercicio_nuevo = ejercicio_nuevo()
        self.form_ejercicio_nuevo.show()

    def cerrar(self):
        count = 0
        for item2 in self.list_detalle:
            if self.index == str(count):
                obj_e_ejer_detalle = E_ejercicio_detalle()
                obj_e_ejer_detalle.actualizar_estado(item2.id_ejercicio_detalle,"Cerrado")

            count = count + 1

    def seleccion_item_detalle(self, clickedIndex):
        twi0 = self.obj_form.tw_detalle_ejerc.item(clickedIndex,0)
        self.index = twi0.text()


    def seleccion_item_ejercicio(self,clickedIndex):

        twi0 = self.obj_form.tw_ejercicio.item(clickedIndex,1)
        nr = twi0.text()
        count=0
        for item in self.lista_ejercicio :
            if count == clickedIndex:
                #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                obj_e_ejer_det=E_ejercicio_detalle()
                self.list_detalle=obj_e_ejer_det.buscar_ejercicios_id_ejercicio(item.id_ejercicio)

                for item2 in self.list_detalle:
                    rowPosition = self.obj_form.tw_detalle_ejerc.rowCount()
                    self.obj_form.tw_detalle_ejerc.insertRow(rowPosition)

                    self.obj_form.tw_detalle_ejerc.setItem(rowPosition , 0, QTableWidgetItem(str(item2.nro)))
                    self.obj_form.tw_detalle_ejerc.setItem(rowPosition , 1, QTableWidgetItem(item2.mes))
                    self.obj_form.tw_detalle_ejerc.setItem(rowPosition , 2, QTableWidgetItem(item2.estado))
            count = count+1

    def limpiar(self):
        self.obj_cliente=""
        self.lista_ejercicio =""
        self.list_detalle= ""
        self.index = ""


    def buscar(self):
        self.limpiar()
        if self.obj_form.lne_cuit.text() !="":
            cuit = self.obj_form.lne_cuit.text()
            obj_e_cliente= E_cliente()
            self.obj_cliente = obj_e_cliente.get_cliente_cuit_cuil(cuit)
            if self.obj_cliente == False :
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Atencion")
                msgBox.setText('No se encontro el cliente')
                msgBox.exec_()
            else:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Atencion")
                msgBox.setText('Cliente se encuentra')
                msgBox.exec_()
                self.obj_form.ln_nombre.setText(self.obj_cliente.razon_social)
                obj_e_ejercicio = E_ejercicio()
                self.lista_ejercicio = obj_e_ejercicio.get_ejercicio_id_cliente(self.obj_cliente.id_cliente)
                #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                for item in self.lista_ejercicio:
                    rowPosition = self.obj_form.tw_ejercicio.rowCount()
                    self.obj_form.tw_ejercicio.insertRow(rowPosition)
                    self.obj_form.tw_ejercicio.setItem(rowPosition , 0, QTableWidgetItem(str(item.fec_inicio.year)+"-"+str(item.fec_fin.year)))
                    self.obj_form.tw_ejercicio.setItem(rowPosition , 1, QTableWidgetItem(item.descripcion))
                    self.obj_form.tw_ejercicio.setItem(rowPosition , 2, QTableWidgetItem(item.tipo))

        elif self.obj_form.lne_razon_social.text() !="":
            razon_social= self.obj_form.lne_razon_social.text()
            obj_e_cliente= E_proveedor()
            self.obj_cliente = obj_e_cliente.get_cliente_razon_social(razon_social)
            if self.obj_cliente == False :
                #"cliente encontrado"
                a=1
            else:
                a=2
                #ingrese el cuit nuevamente

