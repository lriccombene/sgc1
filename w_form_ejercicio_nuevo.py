import sys,datetime
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_ejercicio_nuevo import Ui_form_ejercicio_nuevo
from PyQt5.QtCore import pyqtRemoveInputHook
from E_ejercicio import E_ejercicio
from E_ejercicio_detalle import E_ejercicio_detalle
from E_cliente import E_cliente

class ejercicio_nuevo(QDialog):
    obj_form= Ui_form_ejercicio_nuevo()
    obj_cliente=""

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_ejercicio_nuevo()
        self.obj_form.setupUi(self)
        self.obj_form.btn_buscar.clicked.connect(self.buscar)
        self.obj_form.btn_guardar.clicked.connect(self.guardar)


    def limpiar(self):

        self.obj_cliente=""


    def guardar(self):

        obj_e_ejercicio = E_ejercicio()
        obj_e_ejercicio.descripcion = self.obj_form.lne_descripcion.text()
        obj_e_ejercicio.tipo = self.obj_form.cbx_tipo.currentText()
        obj_e_ejercicio.fec_inicio = self.obj_form.dte_fec_inic.text()
        obj_e_ejercicio.fec_fin = self.obj_form.dte_fec_fin.text()
        obj_e_ejercicio.id_cliente = self.obj_cliente.id_cliente
        obj_ejercicio = obj_e_ejercicio.guardar(obj_e_ejercicio)

        fec_ini = self.obj_form.dte_fec_inic.text()
        obj_date_fec_ini = datetime.datetime.strptime(fec_ini, '%d/%m/%Y')
        mes_inicio = obj_date_fec_ini.month
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        for x in range(0,12):
            mes_final=""
            if x == 0 :
                mes = self.mes(mes_inicio)
                mes_final = mes
            else:
                #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                nuevo_mes = obj_date_fec_ini.month + x
                nuevo_year = obj_date_fec_ini.year
                nuevo_dia = 5
                mes_final = self.mes(nuevo_mes)
                if nuevo_mes > 12 and nuevo_mes < 25:
                    mes_final = nuevo_mes % 12
                    mes_final = self.mes(mes_final)
                    if mes_final == 0:
                        mes_final=self.mes(12)
                        nuevo_year += 1

                mes_final = str(mes_final)

            #print (mes_final)
            obj_E_ejercicio_detalle = E_ejercicio_detalle()
            mes = self.mes(mes_inicio)
            
            obj_E_ejercicio_detalle.mes = mes_final
            obj_E_ejercicio_detalle.estado = "abierto"
            obj_E_ejercicio_detalle.id_ejercicio = obj_ejercicio.id_ejercicio
            obj_E_ejercicio_detalle.nro = x
            obj_E_ejercicio_detalle.guardar(obj_E_ejercicio_detalle)

        msgBox = QMessageBox()
        msgBox.setWindowTitle("Atencion")
        msgBox.setText('Ejercicio OK')
        msgBox.exec_()


    def mes(self,nro):
        if nro == 2 :
            return "Febrero"
        elif nro == 3 :
            return "Marzo"
        elif nro == 4 :
            return "Abril"
        elif nro == 5 :
            return "Mayo"
        elif nro == 6 :
            return "Junio"
        elif nro == 7 :
            return "Julio"
        elif nro == 8 :
            return "Agosto"
        elif nro == 9 :
            return "Septiembre"
        elif nro == 10 :
            return "Octubre"
        elif nro == 11 :
            return "Noviembre"
        elif nro == 12 :
            return "Diciembre"
        elif nro == 1 :
            return "Enero"


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


