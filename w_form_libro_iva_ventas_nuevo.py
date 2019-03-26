import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_libro_iva_ventas_nuevo import Ui_form_libro_iva_ventas_nuevo
from PyQt5.QtCore import pyqtRemoveInputHook
from E_plan_cuentas import E_plan_cuentas
from E_ejercicio import E_ejercicio
from E_cliente import E_cliente
from E_proveedor import E_proveedor
from E_libro_iva_venta import E_libro_iva_ventas
from E_ejercicio_detalle import E_ejercicio_detalle

class libro_iva_ventas_nuevo(QDialog):
    obj_form= Ui_form_libro_iva_ventas_nuevo()
    lista_ejercicio = ""
    lista_proveedor = ""

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_libro_iva_ventas_nuevo()
        self.obj_form.setupUi(self)
        self.obj_form.btn_buscar.clicked.connect(self.buscar)
        self.obj_form.pushButton_2.clicked.connect(self.pushButton_2)

        self.obj_form.lne_10_5.editingFinished.connect(self.sumar)
        self.obj_form.lne_21.editingFinished.connect(self.sumar)
        self.obj_form.lne_monotrib.editingFinished.connect(self.sumar)
        self.obj_form.lne_no_grav.editingFinished.connect(self.sumar)
        self.obj_form.lne_iibb.editingFinished.connect(self.sumar)
        self.obj_form.lne_27.editingFinished.connect(self.sumar)
        self.obj_form.lne_iva.editingFinished.connect(self.sumar)
        self.obj_form.lne_otros.editingFinished.connect(self.sumar)
        self.obj_form.lne_percepcion_iva.editingFinished.connect(self.sumar)

    def sumar(self):
        suma1 =  float(self.obj_form.lne_10_5.text()) + float(self.obj_form.lne_21.text())
        suma2 = float(self.obj_form.lne_monotrib.text()) + float(self.obj_form.lne_no_grav.text()) + float(self.obj_form.lne_iibb.text())
        suma3 = float(self.obj_form.lne_27.text()) + float(self.obj_form.lne_iva.text()) + float(self.obj_form.lne_otros.text())
        suma4 = float(self.obj_form.lne_percepcion_iva.text())
        total = suma1 + suma2 + suma3 + suma4
        self.obj_form.lne_resultado.setText(str(total))

    def limpiar(self):
        self.obj_form.cbx_proveedor.clear()
        self.obj_form.cbx_ejercicio.clear()
        self.lista_ejercicio = ""
        self.lista_proveedor  = ""
        self.lista_ejercicio_detalle = ""

    def buscar(self):
        self.limpiar()

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
                msgBox.setText('Cliente OK')
                msgBox.exec_()
                self.obj_form.lne_razon_social.setText(self.obj_cliente.razon_social)

                obj_e_proveedor = E_proveedor()
                self.lista_proveedor = obj_e_proveedor.buscar_proveedores(self.obj_cliente.id_cliente)
                for item in self.lista_proveedor:
                    self.obj_form.cbx_proveedor.addItem(item.nombre)

                obj_e_ejercicio = E_ejercicio()
                self.lista_ejercicio = obj_e_ejercicio.get_ejercicio_id_cliente(self.obj_cliente.id_cliente)
                for item in self.lista_ejercicio:
                    self.obj_form.cbx_ejercicio.addItem(item.descripcion)



    def pushButton_2(self):

        obj_e_E_libro_iva_ventas = E_libro_iva_ventas()
        obj_e_E_libro_iva_ventas.fecha = self.obj_form.dte_fec_nuevo.text()
        obj_e_E_libro_iva_ventas.nro_comprobante = self.obj_form.lne_comprbante.text()
        obj_proveedor = ""
        for item in self.lista_proveedor:
            if self.obj_form.cbx_proveedor.currentText() == item.nombre:
                obj_proveedor = item

        obj_e_E_libro_iva_ventas.id_proveedor = obj_proveedor.id_proveedor
        obj_e_E_libro_iva_ventas.tipo = self.obj_form.cbx_tipo.currentText()
        obj_e_E_libro_iva_ventas.neto_10_5 = self.obj_form.lne_10_5.text()
        obj_e_E_libro_iva_ventas.neto_21 = self.obj_form.lne_21.text()
        obj_e_E_libro_iva_ventas.neto_27 = self.obj_form.lne_27.text()
        obj_e_E_libro_iva_ventas.neto_27 = self.obj_form.lne_27.text()
        obj_e_E_libro_iva_ventas.iva = self.obj_form.lne_iva.text()
        obj_e_E_libro_iva_ventas.monotributo = self.obj_form.lne_monotrib.text()
        obj_e_E_libro_iva_ventas.impuestos_otros = self.obj_form.lne_otros.text()
        obj_e_E_libro_iva_ventas.percepcion_iva = self.obj_form.lne_percepcion_iva.text()
        obj_e_E_libro_iva_ventas.percepcion_IBB = self.obj_form.lne_iibb.text()
        #obj_e_E_libro_iva_ventas.ref = self.obj_form.lne_ref.text()
        obj_e_E_libro_iva_ventas.no_gravado = self.obj_form.lne_no_grav.text()
        obj_e_E_libro_iva_ventas.id_cliente = self.obj_cliente.id_cliente
        #pyqtRemoveInputHook()
        #import pdb;pdb.set_trace()
        obj_ejercicio = ""
        for item in self.lista_ejercicio:
            if item.descripcion == self.obj_form.cbx_ejercicio.currentText():
                obj_ejercicio= item

        obj_e_E_libro_iva_ventas.id_ejercicio = obj_ejercicio.id_ejercicio

        obj_E_ejercicio_detalle = E_ejercicio_detalle()
        self.lista_ejercicio_detalle = obj_E_ejercicio_detalle.buscar_ejercicios_id_ejercicio(obj_ejercicio.id_ejercicio)
        obj_ejercicio_detalle = ""
        for item in self.lista_ejercicio_detalle:
            if item.mes == self.obj_form.cbx_mes.currentText():
                obj_ejercicio_detalle=item
        obj_e_E_libro_iva_ventas.id_ejercicio_detalle = obj_ejercicio_detalle.id_ejercicio_detalle


        obj_e_E_libro_iva_ventas.guardar(obj_e_E_libro_iva_ventas)
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Atencion")
        msgBox.setText('Registro guardado OK')
        msgBox.exec_()
