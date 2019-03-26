import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_libro_iva_ventas import Ui_form_libro_iva_ventas
from PyQt5.QtCore import pyqtRemoveInputHook
from E_cliente import E_cliente
from E_libro_iva_venta import E_libro_iva_ventas
from E_proveedor import E_proveedor
from E_ejercicio import E_ejercicio
from E_ejercicio_detalle import E_ejercicio_detalle
from w_form_libro_iva_ventas_nuevo import libro_iva_ventas_nuevo

class libro_iva_ventas(QDialog):
    obj_form= Ui_form_libro_iva_ventas()
    lista_proveedor = ""
    obj_cliente = ""


    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_libro_iva_ventas()
        self.obj_form.setupUi(self)
        self.obj_form.btn_buscar.clicked.connect(self.buscar)
        self.obj_form.btn_buscar_compra.clicked.connect(self.buscar_compra)
        self.obj_form.btn_nuevo.clicked.connect(self.nuevo)
        self.obj_form.btn_eliminar.clicked.connect(self.eliminar)

    def eliminar(self):
        obj_e_libro_iva_ventas = E_libro_iva_ventas()



    def nuevo(self):
        self.form_libro_iva_ventas_nuevo = libro_iva_ventas_nuevo()
        self.form_libro_iva_ventas_nuevo.show()

    def buscar_compra(self):
        while (self.obj_form.tw_ventas.rowCount() > 0):
            self.obj_form.tw_ventas.removeRow(0)


        obj_ejercicio = ""
        for item in self.lista_ejercicio:
            if item.descripcion == self.obj_form.cbx_ejercicio.currentText():
                obj_ejercicio = item

        obj_E_ejercicio_detalle = E_ejercicio_detalle()
        self.lista_ejercicio_detalle = obj_E_ejercicio_detalle.buscar_ejercicios_id_ejercicio(obj_ejercicio.id_ejercicio)
        obj_ejercicio_detalle = ""
        for item in self.lista_ejercicio_detalle:
            if item.mes == self.obj_form.cbx_mes.currentText():
                obj_ejercicio_detalle=item

        obj_e_libro_iva_venta = E_libro_iva_ventas()
        grilla = obj_e_libro_iva_venta.get_grila_libro_iva_ventas(obj_ejercicio.id_ejercicio,obj_ejercicio_detalle.id_ejercicio_detalle)

        try:
            for item in grilla:
                rowPosition = self.obj_form.tw_ventas.rowCount()
                self.obj_form.tw_ventas.insertRow(rowPosition)
                self.obj_form.tw_ventas.setItem(rowPosition, 0, QTableWidgetItem(str(item[1])))
                self.obj_form.tw_ventas.setItem(rowPosition, 1, QTableWidgetItem(str(item[2])))
                self.obj_form.tw_ventas.setItem(rowPosition, 2, QTableWidgetItem(str(item[3])))
                self.obj_form.tw_ventas.setItem(rowPosition, 3, QTableWidgetItem(str(item[4])))
        except:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Atencion")
            msgBox.setText('No se encontro registros')
            msgBox.exec_()



    #def limpiar(self):
    #    a=1

    def buscar(self):
        #self.limpiar()
        self.obj_form.cbx_ejercicio.clear()
        if self.obj_form.lne_cuit.text() != "":
            # pyqtRemoveInputHook()
            # import pdb; pdb.set_trace()
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
            # obj_e_cliente= E_proveedor()
            # self.obj_cliente = obj_e_cliente.get_cliente_razon_social(razon_social)
            # if self.obj_cliente == False :
            # "cliente encontrado"
            #    a=1
            # else:
            #    a=2
            # ingrese el cuit nuevamente

