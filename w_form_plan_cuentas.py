import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_plan_cuentas import Ui_form_plan_cuentas
from PyQt5.QtCore import pyqtRemoveInputHook
from E_plan_cuentas import E_plan_cuentas
from E_cliente import E_cliente

class plan_cuentas(QDialog):
    obj_form= Ui_form_plan_cuentas()
    obj_cliente = ""
    lista_plan_cuentas = ""
    index = ""

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_plan_cuentas()
        self.obj_form.setupUi(self)
        self.obj_form.btn_buscar.clicked.connect(self.buscar)
        self.obj_form.btn_agregar.clicked.connect(self.agregar)
        self.obj_form.btn_modificar.clicked.connect(self.modificar)
        self.obj_form.tw_plan_ctas.cellClicked.connect(self.seleccion_item_plan)

    def modificar(self):
        indexes = [QPersistentModelIndex(index) for index in self.obj_form.tw_plan_ctas.selectionModel().selectedRows()]
        for index in indexes:
            id = int(self.obj_form.tw_plan_ctas.model().data(self.obj_form.tw_plan_ctas.model().index(index.row(), 2)))
            codigo = self.obj_form.tw_plan_ctas.model().data(self.obj_form.tw_plan_ctas.model().index(index.row(), 0))
            descripcion = self.obj_form.tw_plan_ctas.model().data(self.obj_form.tw_plan_ctas.model().index(index.row(), 1))

            obj_plan_cta = E_plan_cuentas()
            obj_plan_cta.actualizar(id, codigo, descripcion)
        self.recargar_grilla()

    def seleccion_item_plan(self,clickedIndex):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        self.index = clickedIndex
        twi0 = self.obj_form.tw_plan_ctas.item(clickedIndex,0)
        codigo = twi0.text()
        twi1 = self.obj_form.tw_plan_ctas.item(clickedIndex,1)
        descripcion = twi1.text()
        self.obj_form.lne_codigo.setText(codigo)
        self.obj_form.lne_descripcion.setText(descripcion)


    def agregar(self):
        rowPosition = self.obj_form.tw_plan_ctas.rowCount()
        self.obj_form.tw_plan_ctas.insertRow(rowPosition)
        self.obj_form.tw_plan_ctas.setItem(rowPosition , 0, QTableWidgetItem(self.obj_form.lne_codigo.text()))
        self.obj_form.tw_plan_ctas.setItem(rowPosition , 1, QTableWidgetItem(self.obj_form.lne_descripcion.text()))
        obj_plan_cta = E_plan_cuentas()
        obj_plan_cta.codigo =self.obj_form.lne_codigo.text()
        obj_plan_cta.descripcion = self.obj_form.lne_descripcion.text()
        obj_plan_cta.id_cliente = self.obj_cliente.id_cliente
        obj_plan_cta.guardar(obj_plan_cta)
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Atencion")
        msgBox.setText('Se grabo correctamente')
        msgBox.exec_()
        self.recargar_grilla()


    def eliminar(self):
        w = QWidget()

        indexes = [QPersistentModelIndex(index) for index in self.obj_form.tw_plan_ctas.selectionModel().selectedRows()]
        if len(indexes) > 1:
            result = QMessageBox.question(w, 'Alerta', "¿Desea eliminar los planes de cuenta?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        else:
            result = QMessageBox.question(w, 'Alerta', "¿Desea eliminar el plan de cuenta?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if result == QMessageBox.Yes:
            obj_plan_cuentas = E_plan_cuentas()
            diccionario_ctas = {}
            for index in indexes:
                id = int(self.obj_form.tw_plan_ctas.model().data(self.obj_form.tw_plan_ctas.model().index(index.row(), 2)))
                resultado = obj_plan_cuentas.eliminar(id)

                if resultado:
                    diccionario_ctas[self.obj_form.tw_plan_ctas.model().data(self.obj_form.tw_plan_ctas.model().index(index.row(), 0))] = self.obj_form.tw_plan_ctas.model().data(self.obj_form.tw_plan_ctas.model().index(index.row(), 1))
                else:
                    print(resultado)
            QMessageBox.about(self, "Acción realizada", "Se han eliminado los siguientes registros: " + str(diccionario_ctas))

            self.recargar_grilla()

    def limpiar(self):
        self.obj_cliente=""
        self.lista_plan_cuentas=""
        while (self.obj_form.tw_plan_ctas.rowCount() > 0):
            self.obj_form.tw_plan_ctas.removeRow(0)

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
                msgBox.setText('Cliente OK')
                msgBox.exec_()
                self.obj_form.lne_razon_social.setText(self.obj_cliente.razon_social)
                self.cargar_grilla(self.obj_cliente )

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

    def cargar_grilla(self, cliente):
        obj_plan_cuentas = E_plan_cuentas()
        self.lista_plan_cuentas = obj_plan_cuentas.get_cuentas_id_cliente(cliente.id_cliente)
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        if self.lista_plan_cuentas != 'False':
            for item in self.lista_plan_cuentas:
                rowPosition = self.obj_form.tw_plan_ctas.rowCount()
                self.obj_form.tw_plan_ctas.insertRow(rowPosition)
                self.obj_form.tw_plan_ctas.setItem(rowPosition , 0, QTableWidgetItem(str(item.codigo)))
                self.obj_form.tw_plan_ctas.setItem(rowPosition , 1, QTableWidgetItem(item.descripcion))

    def recargar_grilla(self):
        self.limpiar()
        cuit = self.obj_form.lne_cuit.text()
        obj_e_cliente = E_cliente()
        self.obj_cliente = obj_e_cliente.get_cliente_cuit_cuil(cuit)
        self.cargar_grilla(self.obj_cliente)






