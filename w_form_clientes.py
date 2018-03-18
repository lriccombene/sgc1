import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_clientes import Ui_form_clientes
from PyQt5.QtCore import pyqtRemoveInputHook
from E_cliente import E_cliente


class clientes(QDialog):
    obj_form = Ui_form_clientes()
    obj_cliente = ""

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_clientes()
        self.obj_form.setupUi(self)
        self.obj_form.btn_buscar.clicked.connect(self.buscar)
        self.obj_form.btn_grabar.clicked.connect(self.guardar)
        self.obj_form.btn_modificar.clicked.connect(self.modificar)
        self.obj_form.btn_eliminar.clicked.connect(self.eliminar)


    def limpiar(self):
        self.obj_cliente =""

    def eliminar(self):
        obj_e_cliente= E_cliente()
        obj_e_cliente.eliminar(self.obj_cliente.id_cliente)



    def modificar(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj_e_cliente = E_cliente()
        obj_e_cliente.nombre =  self.obj_form.lne_nombre.text()
        obj_e_cliente.apellido =  self.obj_form.lne_apellido.text()
        obj_e_cliente.razon_social =  self.obj_form.lne_razon_social_nuevo.text()
        obj_e_cliente.cuit_cuil =  self.obj_form.lne_cuit_nuevo.text()
        obj_e_cliente.inicio_actividad =  self.obj_form.dte_fec_actividad.text()
        obj_e_cliente.condicion_ante_iva =  self.obj_form.cbx_iva.currentText()
        obj_e_cliente.IBB =  self.obj_form.lne_iibb.text()
        obj_e_cliente.matricula =  self.obj_form.lne_matricula.text()
        obj_e_cliente.descripcion_actividad =  self.obj_form.lne_actividad.text()
        obj_e_cliente.direccion =  self.obj_form.lne_domicilio.text()
        obj_e_cliente.telefono =  self.obj_form.lne_telefono.text()
        obj_e_cliente.celular =  self.obj_form.lne_celular.text()
        obj_e_cliente.email =  self.obj_form.lne_email.text()
        obj_e_cliente.nombre_contacto =  self.obj_form.lne_contacto.text()
        obj_e_cliente.actualizar(obj_e_cliente,self.obj_cliente.id_cliente)
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Atencion")
        msgBox.setText('Cliente se modifico correctamente')
        msgBox.exec_()



    def guardar(self):
        obj_e_cliente = E_cliente()
        obj_e_cliente.nombre =  self.obj_form.lne_nombre.text()
        obj_e_cliente.apellido =  self.obj_form.lne_apellido.text()
        obj_e_cliente.razon_social =  self.obj_form.lne_razon_social_nuevo.text()
        obj_e_cliente.cuit_cuil =  self.obj_form.lne_cuit_nuevo.text()
        obj_e_cliente.inicio_actividad =  self.obj_form.dte_fec_actividad.text()
        obj_e_cliente.condicion_ante_iva =  self.obj_form.cbx_iva.currentText()
        obj_e_cliente.IBB =  self.obj_form.lne_iibb.text()
        obj_e_cliente.matricula =  self.obj_form.lne_matricula.text()
        obj_e_cliente.descripcion_actividad =  self.obj_form.lne_actividad.text()
        obj_e_cliente.direccion =  self.obj_form.lne_domicilio.text()
        obj_e_cliente.telefono =  self.obj_form.lne_telefono.text()
        obj_e_cliente.celular =  self.obj_form.lne_celular.text()
        obj_e_cliente.email =  self.obj_form.lne_email.text()
        obj_e_cliente.nombre_contacto =  self.obj_form.lne_contacto.text()
        obj_e_cliente.guardar(obj_e_cliente)
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Atencion")
        msgBox.setText('Cliente se guardo correctamente')
        msgBox.exec_()

    def buscar(self):
        self.limpiar()
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        if self.obj_form.lne_cuit.text() !="":
            cuit = self.obj_form.lne_cuit.text()
            obj_e_cliente= E_cliente()
            self.obj_cliente = obj_e_cliente.get_cliente_cuit_cuil(cuit)

        elif self.obj_form.lne_razon_social.text() !="":
            razon_social= self.obj_form.lne_razon_social.text()
            obj_e_cliente= E_proveedor()
            self.obj_cliente = obj_e_cliente.get_cliente_razon_social(razon_social)

        self.obj_form.lne_nombre.setText(self.obj_cliente.nombre)
        self.obj_form.lne_apellido.setText(self.obj_cliente.apellido)
        self.obj_form.lne_razon_social_nuevo.setText(self.obj_cliente.razon_social)
        self.obj_form.lne_cuit_nuevo.setText(self.obj_cliente.cuit_cuil)
        self.obj_form.dte_fec_actividad.setDate(self.obj_cliente.inicio_actividad)

        index_iva = self.obj_form.cbx_iva.findText(str(self.obj_cliente.condicion_ante_iva))
        self.obj_form.cbx_iva.setCurrentIndex(index_iva)

        self.obj_form.lne_iibb.setText(self.obj_cliente.IBB)
        self.obj_form.lne_matricula.setText(self.obj_cliente.matricula)
        self.obj_form.lne_actividad.setText(self.obj_cliente.descripcion_actividad)
        self.obj_form.lne_domicilio.setText(self.obj_cliente.direccion)
        self.obj_form.lne_telefono.setText(self.obj_cliente.telefono)
        self.obj_form.lne_celular.setText(self.obj_cliente.celular)
        self.obj_form.lne_email.setText(self.obj_cliente.email)
        self.obj_form.lne_contacto.setText(self.obj_cliente.nombre_contacto)

        msgBox = QMessageBox()
        msgBox.setWindowTitle("Atencion")
        msgBox.setText('Se encontro el cliente')
        msgBox.exec_()







