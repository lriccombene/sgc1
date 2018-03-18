import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_asiento import Ui_form_asiento
from PyQt5.QtCore import pyqtRemoveInputHook
from E_cliente import E_cliente
from E_ejercicio import E_ejercicio
from E_ejercicio_detalle import E_ejercicio_detalle
from E_asiento import E_asiento

class asiento(QDialog):
    obj_form= Ui_form_asiento()
    obj_cliente=""
    lista_ejercicio=""
    obj_cliente=""


    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_asiento()
        self.obj_form.setupUi(self)
        self.obj_form.btn_buscar.clicked.connect(self.buscar)
        self.obj_form.btn_guardar.clicked.connect(self.guardar)


    def guardar(self):

        obj_ejercicio= ""
        for item in self.lista_ejercicio :
            if item.descripcion == self.obj_form.cbx_ejercicio.currentText():
                obj_ejercicio=item

        obj_ejer_detalle = E_ejercicio_detalle()
        list_ejer_detalle = obj_ejer_detalle.buscar_ejercicios_id_ejercicio(obj_ejercicio.id_ejercicio)
        obj_ejer_detalle = ""
        for item in list_ejer_detalle:
            if item.mes == self.obj_form.cbx_mes.currentText():
                obj_ejer_detalle =item

        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj_asiento = E_asiento()
        obj_asiento.id_cliente = self.obj_cliente.id_cliente
        obj_asiento.id_ejercicio = obj_ejercicio.id_ejercicio
        obj_asiento.id_ejercicio_detalle = obj_ejer_detalle.id_ejercicio_detalle
        obj_asiento.fecha = self.obj_form.dte_fecha.text()
        obj_asiento.descripcion = self.obj_form.lne_descripcion.text()
        obj_asiento.guardar(obj_asiento)
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Atencion")
        msgBox.setText('Se grabo correctamente')
        msgBox.exec_()


    def limpriar(self):
        self.lista_ejercicio = ""
        self.obj_cliente = ""

    def buscar(self):
        #self.limpiar()
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
                self.obj_form.lne_razon_social.setText(self.obj_cliente.razon_social)
                obj_e_ejercicio = E_ejercicio()
                self.lista_ejercicio = obj_e_ejercicio.get_ejercicio_id_cliente(self.obj_cliente.id_cliente)
                for item in self.lista_ejercicio:
                    self.obj_form.cbx_ejercicio.addItem(item.descripcion)


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

        def buscar_asiento_id_asiento(self,id_asiento):
            obj_e_asiento=E_asiento()
            lista_asiento= obj_e_asiento.get_asiento_plan_cuenta(id_asiento)
            return lista_asiento

