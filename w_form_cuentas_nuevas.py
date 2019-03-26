import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_cuentas_nuevo import Ui_form_cuentas_nuevo
from PyQt5.QtCore import pyqtRemoveInputHook
from E_cliente import E_cliente
from E_ejercicio import E_ejercicio
from E_asiento import E_asiento
from E_cuenta import E_cuenta

class cuentas_nuevas(QDialog):
    obj_form= Ui_form_cuentas_nuevo()
    id_asiento=""
    lista_ejercicio_cliente =""
    lista_asiento = ""
    lista_cuentas = ""

    def __init__(self,id_asiento):

        QDialog.__init__(self)
        obj_form= Ui_form_cuentas_nuevo()
        self.obj_form.setupUi(self)
        self.obj_form.btn_guardar.clicked.connect(self.guardar)
        obj_e_asiento=E_asiento()
        self.id_asiento= id_asiento
        self.lista_cuentas=obj_e_asiento.get_asiento_plan_cuenta(id_asiento)
        for item in self.lista_cuentas:
            #self.obj_form.cbx_cuenta
            self.obj_form.cbx_cuenta.addItem(item[2]+ " - " + item[0])

    def guardar(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj_e_cuenta= E_cuenta()
        obj_e_asiento=E_asiento()
        lista_cuentas=obj_e_asiento.get_asiento_plan_cuenta(self.id_asiento)

        for item in lista_cuentas:
            combo_string= self.obj_form.cbx_cuenta.currentText()
            pos_caracter= combo_string.find("-") +2
            descripcion_plan= combo_string[(pos_caracter):]
            if item[0] == descripcion_plan:
                obj_e_cuenta.id_plan_cuentas = item[1]
        
        obj_e_cuenta.debe = self.obj_form.lne_debe.text() 
        obj_e_cuenta.haber = self.obj_form.lne_haber.text()
        obj_e_cuenta.id_asiento =  self.id_asiento
        obj_e_cuenta.guardar(obj_e_cuenta)
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Atencion")
        msgBox.setText('Cuenta OK')
        msgBox.exec_()



