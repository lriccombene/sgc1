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
    lista_proveedores =""
    cuit_cuil = ""

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_proveedores()
        self.obj_form.setupUi(self)
        self.obj_form.btn_buscar.clicked.connect(self.buscar_proveedor)
        self.obj_form.btn_guardar.clicked.connect(self.guardar_proveedor)
        self.obj_form.tw_proveedores.cellClicked.connect(self.seleccion_proveedor)

        #obj_e_cliente = E_cliente()
        #self.lista_clientes = obj_e_cliente.get_clientes()
        #for item in self.lista_clientes:
        #    self.obj_form.cbx_cliente.addItem(item.razon_social)

    def seleccion_proveedor(self,clickedIndex):
        self.index = clickedIndex
        twi0 = self.obj_form.tw_proveedores.item(clickedIndex,0)
        self.cuit_cuil = twi0.text()



    def eliminar(self,):
        w = QWidget()
        result = QMessageBox.question(w, 'Alerta', " Dejea eliminar proveedor?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if result == QMessageBox.Yes:
            obj_proveedor = E_proveedor  ()
            if self.lista_proveedores != 'False':
                for item in self.proveedores:
                    if(item.cuit_cuil == self.cuit_cuil ):
                        obj_proveedor.eliminar(item.id_proveedor)



    def limpiar(self):
        self.obj_cliente = ""
        self.lista_clientes = ""
        self.obj_proveedor = ""
        self.lista_proveedores =""
        while (self.obj_form.tw_proveedores.rowCount() > 0):
            self.obj_form.tw_proveedores.removeRow(0)


    def buscar_id_cliente(self,razon_social_cliente):
        for item in self.lista_clientes:
            if item.razon_social == razon_social_cliente:
                cliente = item
        return cliente

    def guardar_proveedor(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj_e_proveedor = E_proveedor()
        obj_e_proveedor.nombre = self.obj_form.lne_nombre.text()
        obj_e_proveedor.razon_social = self.obj_form.lne_razon_social_proveedor.text()
        obj_proveedor = obj_e_proveedor.get_proveedor_cuit_cuil(self.obj_form.lne_cuit_proveedor.text(),self.obj_cliente.id_cliente)

        bandera = False
        try:
            a = obj_proveedor.id
        except:
            bandera=True

        obj_e_proveedor.cuit_cuil = self.obj_form.lne_cuit_proveedor.text()
        obj_e_proveedor.condicion_ante_iva = self.obj_form.cbx_iva.currentText()
        obj_e_proveedor.ref = self.obj_form.lne_ref.text()
        #cliente = self.buscar_id_cliente(self.obj_form.cbx_cliente.currentText())
        obj_e_proveedor.id_cliente =  self.obj_cliente.id_cliente
        if bandera == True:
            obj_e_proveedor.guardar(obj_e_proveedor)
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Atencion")
            msgBox.setText('Proveedor se guardo correctamente')
            msgBox.exec_()


    def buscar_proveedor(self):
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
                #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                self.obj_form.lne_razon_social.setText(self.obj_cliente.razon_social)
                obj_e_proveedor= E_proveedor()
                self.lista_proveedores = obj_e_proveedor.buscar_proveedores(self.obj_cliente.id_cliente)
                for item in self.lista_proveedores:
                    rowPosition = self.obj_form.tw_proveedores.rowCount()
                    self.obj_form.tw_proveedores.insertRow(rowPosition)

                    self.obj_form.tw_proveedores.setItem(rowPosition , 0, QTableWidgetItem(str(item.cuit_cuil)))
                    self.obj_form.tw_proveedores.setItem(rowPosition , 1, QTableWidgetItem(item.nombre))
                    self.obj_form.tw_proveedores.setItem(rowPosition , 2, QTableWidgetItem(item.razon_social))

                msgBox = QMessageBox()
                msgBox.setWindowTitle("Atencion")
                msgBox.setText('Cliente OK')
                msgBox.exec_()


