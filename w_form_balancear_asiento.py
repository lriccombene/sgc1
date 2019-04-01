import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem,QWidget
from PyQt5 import uic
from form_balancear_asiento import Ui_form_balancear_asiento
from PyQt5.QtCore import pyqtRemoveInputHook
from E_asiento import E_asiento
from E_cliente import E_cliente



class balancear_asiento(QWidget):
    obj_form = Ui_form_balancear_asiento()
    obj_cliente = ""

    def __init__(self):
        QDialog.__init__(self)
        self.obj_form.setupUi(self)
        self.obj_form.btn_buscar.clicked.connect(self.buscar)
        self.obj_form.btn_calcular_asientos.clicked.connect(self.calcular)

    def limpiar(self):
        self.obj_cliente =""


    def calcular(self):
        a=1

    def buscar(self):
        # self.limpiar()
        if self.obj_form.lne_cuit.text() != "":
            cuit = self.obj_form.lne_cuit.text()
            obj_e_cliente = E_cliente()
            self.obj_cliente = obj_e_cliente.get_cliente_cuit_cuil(cuit)
            if self.obj_cliente == False:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Atencion")
                msgBox.setText('No se encontro el cliente')
                msgBox.exec_()
            else:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Atencion")
                msgBox.setText('Cliente OK')
                msgBox.exec_()
                self.obj_form.lne_razon_social.setText(self.obj_cliente.razon_social)
                obj_e_ejercicio = E_ejercicio()
                self.lista_ejercicio = obj_e_ejercicio.get_ejercicio_id_cliente(self.obj_cliente.id_cliente)
                for item in self.lista_ejercicio:
                    self.obj_form.cbx_ejercicio.addItem(item.descripcion)


        elif self.obj_form.lne_razon_social.text() != "":
            razon_social = self.obj_form.lne_razon_social.text()
            obj_e_cliente = E_proveedor()
            self.obj_cliente = obj_e_cliente.get_cliente_razon_social(razon_social)
            if self.obj_cliente == False:
                # "cliente encontrado"
                a = 1
            else:
                a = 2
                # ingrese el cuit nuevamente