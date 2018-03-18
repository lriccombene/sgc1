import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_proveedores import Ui_form_proveedores
from PyQt5.QtCore import pyqtRemoveInputHook
from E_cliente import E_cliente
from E_proveedor import E_proveedor

class proveedores(QDialog):
    obj_form= Ui_form_proveedores()
    obj_cliente = ""
    lista_clientes = ""
    obj_proveedor = ""
    obj_cliente = ""

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_proveedores()
        self.obj_form.setupUi(self)
        self.obj_form.btn_buscar.clicked.connect(self.buscar_proveedor)
        self.obj_form.btn_guardar.clicked.connect(self.guardar_proveedor)

        obj_e_cliente = E_cliente()
        self.lista_clientes = obj_e_cliente.get_clientes()
        for item in self.lista_clientes:
            self.obj_form.cbx_cliente.addItem(item.razon_social)


    def limpiar(self):
        self.obj_cliente = ""
        self.lista_clientes = ""
        self.obj_proveedor = ""
        self.obj_cliente = ""

    def buscar_id_cliente(self,razon_social_cliente):
        for item in self.lista_clientes:
            if item.razon_social == razon_social_cliente:
                cliente = item
        return cliente

    def guardar_proveedor(self):
        obj_e_proveedor = E_proveedor()
        obj_e_proveedor.nombre = self.obj_form.lne_nombre.text()
        obj_e_proveedor.razon_social = self.obj_form.lne_razon_social_proveedor.text()
        obj_e_proveedor.cuit_cuil = self.obj_form.lne_cuit_proveedor.text()
        obj_e_proveedor.condicion_ante_iva = self.obj_form.cbx_iva.currentText()
        obj_e_proveedor.ref = self.obj_form.lne_ref.text()
        cliente = self.buscar_id_cliente(self.obj_form.cbx_cliente.currentText())
        obj_e_proveedor.id_cliente = cliente.id_cliente
        obj_e_proveedor.guardar(obj_e_proveedor)
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Atencion")
        msgBox.setText('Proveedor se guardo correctamente')
        msgBox.exec_()


    def buscar_proveedor(self):
        self.limpiar()
        obj_proveedor = ""
        cliente = self.buscar_id_cliente(self.obj_form.cbx_cliente.currentText())

        if self.obj_form.lne_cuit.text() !="":
            cuit = self.obj_form.lne_cuit.text()
            obj_e_proveedor= E_proveedor()
            self.obj_proveedor = obj_e_proveedor.get_proveedor_cuit_cuil(cuit, cliente.id_cliente)

        elif self.obj_form.lne_razon_social.text() !="":
            razon_social= self.obj_form.lne_razon_social.text()
            obj_e_proveedor= E_proveedor()
            obj_e_proveedor.get_proveedor_razon_social(razon_social)

        self.obj_form.lne_nombre.setText(self.obj_proveedor.nombre)
        self.obj_form.lne_razon_social_proveedor.setText(self.obj_proveedor.razon_social)
        self.obj_form.lne_cuit_proveedor.setText(self.obj_proveedor.cuit_cuil)

        index_iva = self.obj_form.cbx_iva.findText(str(self.obj_proveedor.condicion_ante_iva))
        self.obj_form.cbx_iva.setCurrentIndex(index_iva)

        self.obj_form.lne_ref.setText(self.obj_proveedor.ref)
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Atencion")
        msgBox.setText('Proveedor encontrado')
        msgBox.exec_()
