import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic,QtCore
from form_libro_iva_compras_nuevo import Ui_form_libro_iva_compras_nuevo
from PyQt5.QtCore import pyqtRemoveInputHook
from E_plan_cuentas import E_plan_cuentas
from E_ejercicio import E_ejercicio
from E_asiento import E_asiento
from E_cliente import E_cliente
from E_proveedor import E_proveedor

class libro_iva_compras_nuevo(QDialog):
    obj_form= Ui_form_libro_iva_compras_nuevo()
    lista_plancuenta =list()
    obj_cliente=""
    lista_asiento=""
    lista_ejercicio=""
    lista_proveedor=""

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_libro_iva_compras_nuevo()
        self.obj_form.setupUi(self)
        self.obj_form.btn_buscar.clicked.connect(self.buscar)
        #self.obj_form.cbx_asiento.clicked.connect(self.agregar_asientos)
        #self.obj_form.cbx_ejercicio.connect(self.selectionchange)
        #self.obj_form.cbx_ejercicio.currentIndexChanged.connect(self.selectionchange)
        #self.obj_form.cbx_ejercicio.installEventFilter(self)

        self.obj_form.cbx_ejercicio.currentIndexChanged.connect(self.selectionchange)



    #def eventFilter(self, widget, event):
    #    pyqtRemoveInputHook()
    #    import pdb; pdb.set_trace()
    #    if event.type() == QtCore.QEvent.FocusOut:
    #        print(event.type())
        #return False


    def limpar(self):
        lista_plancuenta =list()
        obj_cliente=""
        lista_asiento=""
        lista_ejercicio=""
        lista_proveedor=""

    def selectionchange(self,i):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        for item in range(0,1000):
            self.obj_form.cbx_asiento.removeItem(item)

        for item in self.lista_ejercicio:
            if item.descripcion ==self.obj_form.cbx_ejercicio.currentText():
                obj_e_asiento = E_asiento()
                self.lista_asiento =obj_e_asiento.get_asiento_id_ejercicio(item.id_ejercicio)
                for item2 in  self.lista_asiento:
                    self.obj_form.cbx_asiento.addItem(item2.descripcion)


    def buscar(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
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
                msgBox.setText('Cliente se encontra')
                msgBox.exec_()
                self.obj_form.lne_razon_social.setText(self.obj_cliente.razon_social)

                obj_e_ejercicio = E_ejercicio()
                self.lista_ejercicio = obj_e_ejercicio.get_ejercicio_id_cliente(self.obj_cliente.id_cliente)
                for item in self.lista_ejercicio:
                    self.obj_form.cbx_ejercicio.addItem(item.descripcion)

                obj_e_plan_cuenta = E_plan_cuentas()
                self.lista_plancuenta=obj_e_plan_cuenta.get_cuentas_id_cliente(self.obj_cliente.id_cliente)
                for item in self.lista_plancuenta:
                    self.obj_form.cbx_cuenta.addItem(item.descripcion)

                obj_e_proveedor = E_proveedor()
                self.lista_proveedor = obj_e_proveedor.buscar_proveedores(self.obj_cliente.id_cliente)
                for item in self.lista_proveedor:
                    self.obj_form.cbx_proveedor.addItem(item.nombre)



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
