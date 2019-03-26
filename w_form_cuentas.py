import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic, QtCore
from form_cuentas import Ui_form_cuentas
from PyQt5.QtCore import pyqtRemoveInputHook
from E_cliente import E_cliente
from E_ejercicio import E_ejercicio
from E_asiento import E_asiento
from E_cuenta import E_cuenta
from w_form_cuentas_nuevas import cuentas_nuevas
from E_plan_cuentas import E_plan_cuentas

class cuentas(QDialog):
    obj_form= Ui_form_cuentas()
    asientos=""
    lista_ejercicio_cliente =""
    lista_asiento = ""
    lista_cuentas = ""
    asiento = ""
    codigo_cuenta=0

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_cuentas()
        self.obj_form.setupUi(self)
        self.obj_form.btn_buscar.clicked.connect(self.buscar)
        self.obj_form.btn_buscar_asiento.clicked.connect(self.buscar_asiento)
        self.obj_form.tw_asiento.cellClicked.connect(self.seleccion_item_asiento)
        self.obj_form.tw_cuentas.cellClicked.connect(self.seleccion_item_cuenta)
        self.obj_form.btn_nueva_cuenta.clicked.connect(self.cuenta_nuevo)
        self.obj_form.btn_eliminar.clicked.connect(self.eliminar)
        self.obj_form.btn_eliminar_cuenta.clicked.connect(self.eliminar_cuenta)

    #self.seleccion_item_cuenta
    def seleccion_item_cuenta(self, clickedIndex):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        twi_codigo = self.obj_form.tw_cuentas.item(clickedIndex, 4)
        self.codigo_cuenta = twi_codigo.text()




    def eliminar_cuenta(self):
        
        obj_cuenta = E_cuenta()
        obj_cuenta.eliminar_cuenta(self.codigo_cuenta)



    def eliminar(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj_asiento = E_asiento()
        obj_asiento.eliminar(self.asiento.id_asiento)

        obj_cuenta = E_cuenta()
        obj_cuenta.eliminar(self.asiento.id_asiento)
        



    def cuenta_nuevo(self):

        self.form_cuentas_nuevas = cuentas_nuevas(self.asiento.id_asiento)
        self.form_cuentas_nuevas.show()


    def seleccion_item_asiento(self, clickedIndex):
        while (self.obj_form.tw_cuentas.rowCount() > 0):
            self.obj_form.tw_cuentas.removeRow(0)
        twi0 = self.obj_form.tw_asiento.item(clickedIndex,1)
        self.index = twi0.text()
        twi1 = self.obj_form.tw_asiento.item(clickedIndex,0)
        self.fecha = twi1.text()
        
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        
        for item in self.lista_asiento :
            if item.descripcion ==self.index and str(self.fecha) ==str(item.fecha) :
                self.asiento = item
        print("\n El id_asiento es: " + str(self.asiento.id_asiento))

        obj_e_cuentas = E_cuenta()
        self.lista_cuentas = obj_e_cuentas.get_cuenta_id_asiento(self.asiento.id_asiento)

        print("\n Este asiento tiene: " + str(len(self.lista_cuentas)) + " operaciones.")

        for item in self.lista_cuentas:
            print("SELECT * FROM plan_cuentas WHERE id_cuenta = " + str(item.id_plan_cuentas))
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            obj_E_plan_cuentas = E_plan_cuentas()
            try:
                #int(item.id_plan_cuentas)
                obj_plan = obj_E_plan_cuentas.get_cuenta_id_cuenta(item.id_plan_cuentas)
                print("plan_cuentas.id_cuenta: " + str(obj_plan.id_cuenta))
                print("plan_cuentas.codigo: " + str(obj_plan.codigo))
                print("plan_cuentas.descripcion: " + str(obj_plan.descripcion))
                print("plan_cuentas.id_cliente: " + str(obj_plan.id_cliente))
                rowPosition = self.obj_form.tw_cuentas.rowCount()
                self.obj_form.tw_cuentas.insertRow(rowPosition)
                self.obj_form.tw_cuentas.setItem(rowPosition, 0, QTableWidgetItem(str(obj_plan.codigo)))
                self.obj_form.tw_cuentas.setItem(rowPosition, 1, QTableWidgetItem(str(obj_plan.descripcion)))
                self.obj_form.tw_cuentas.setItem(rowPosition, 2, QTableWidgetItem(str(item.debe)))
                self.obj_form.tw_cuentas.setItem(rowPosition, 3, QTableWidgetItem(str(item.haber)))
                self.obj_form.tw_cuentas.setItem(rowPosition, 4, QTableWidgetItem(str(item.id_cuenta)))
            except:
                continue
                #return False
        self.obj_form.tw_cuentas.sortItems(0, QtCore.Qt.AscendingOrder)


    def limpiar(self):
        self.obj_cliente = ""
        self.lista_plan_cuentas = ""
        self.asientos = ""
        self.lista_ejercicio_cliente = ""
        self.lista_cuentas = ""
        self.obj_form.cbx_ejercicio.clear()
        while (self.obj_form.tw_asiento.rowCount() > 0):
            self.obj_form.tw_asiento.removeRow(0)
        while (self.obj_form.tw_cuentas.rowCount() > 0):
            self.obj_form.tw_cuentas.removeRow(0)

    def buscar_asiento(self):
        while (self.obj_form.tw_asiento.rowCount() > 0):
            self.obj_form.tw_asiento.removeRow(0)
        while (self.obj_form.tw_cuentas.rowCount() > 0):
            self.obj_form.tw_cuentas.removeRow(0)

        obj_ejercicio = ""
        asiento_descripcion =self.obj_form.cbx_ejercicio.currentText()

        for item in self.lista_ejercicio_cliente:
            if item.descripcion == asiento_descripcion:
                obj_ejercicio=item

        obj_e_asiento = E_asiento()
        self.lista_asiento= obj_e_asiento.get_asiento_id_ejercicio(obj_ejercicio.id_ejercicio)
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        for item in self.lista_asiento:
            rowPosition = self.obj_form.tw_asiento.rowCount()
            self.obj_form.tw_asiento.insertRow(rowPosition)
            self.obj_form.tw_asiento.setItem(rowPosition , 0, QTableWidgetItem(str(item.fecha)))
            self.obj_form.tw_asiento.setItem(rowPosition , 1, QTableWidgetItem(item.descripcion))



    def buscar(self):
        self.limpiar()
        if self.obj_form.lne_cuit.text() !="":
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
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
                msgBox.setText('Cliente OK')
                msgBox.exec_()
                self.obj_form.lne_razon_social.setText(self.obj_cliente.razon_social)


        elif self.obj_form.lne_razon_social.text() !="":
            razon_social= self.obj_form.lne_razon_social.text()
            #obj_e_cliente= E_proveedor()
            #self.obj_cliente = obj_e_cliente.get_cliente_razon_social(razon_social)
            #if self.obj_cliente == False :
                #"cliente encontrado"
            #    a=1
            #else:
            #    a=2
                #ingrese el cuit nuevamente

        obj_e_ejercicio = E_ejercicio()
        self.lista_ejercicio_cliente = obj_e_ejercicio.get_ejercicio_id_cliente(self.obj_cliente.id_cliente)
        for item in self.lista_ejercicio_cliente:
            self.obj_form.cbx_ejercicio.addItem(item.descripcion)



