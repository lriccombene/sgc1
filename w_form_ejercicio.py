import sys
from decimal import *
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_ejercicio import Ui_form_ejercicio
from PyQt5.QtCore import pyqtRemoveInputHook
from E_cliente import E_cliente
from E_ejercicio import E_ejercicio
from E_ejercicio_detalle import E_ejercicio_detalle
from E_asiento import E_asiento
from E_inflacion import E_inflacion
from E_cuenta import E_cuenta
from w_form_ejercicio_nuevo import ejercicio_nuevo

class ejercicio(QDialog):
    obj_form= Ui_form_ejercicio()
    obj_cliente=""
    lista_ejercicio =""
    list_detalle =""
    index=""
    id_ejercicio=0
    

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_ejercicio()
        self.obj_form.setupUi(self)
        self.obj_form.btn_buscar.clicked.connect(self.buscar)
        self.obj_form.btn_cerrar.clicked.connect(self.cerrar)
        self.obj_form.tw_ejercicio.cellClicked.connect(self.seleccion_item_ejercicio)
        self.obj_form.tw_detalle_ejerc.cellClicked.connect(self.seleccion_item_detalle)
        self.obj_form.btn_nuevo.clicked.connect(self.nuevo)
        self.obj_form.btn_eliminar.clicked.connect(self.eliminar_ejercicio)
        self.obj_form.btn_inflacion.clicked.connect(self.calcular_inflacion)

    def eliminar_ejercicio(self):
        obj_ejercicio= E_ejercicio()

        obj_ejercicio.eliminar_ejercicio(self.id_ejercicio)



    def nuevo(self):
        self.form_ejercicio_nuevo = ejercicio_nuevo()
        self.form_ejercicio_nuevo.show()

    def cerrar(self):
        count = 0
        for item2 in self.list_detalle:
            if self.index == str(count):
                obj_e_ejer_detalle = E_ejercicio_detalle()
                obj_e_ejer_detalle.actualizar_estado(item2.id_ejercicio_detalle,"Cerrado")

            count = count + 1

    def seleccion_item_detalle(self, clickedIndex):
        twi0 = self.obj_form.tw_detalle_ejerc.item(clickedIndex,0)
        self.index = twi0.text()


    def seleccion_item_ejercicio(self,clickedIndex):
        column_id_ejercicio = self.obj_form.tw_ejercicio.item(clickedIndex,3)
        self.id_ejercicio = column_id_ejercicio.text()

        twi0 = self.obj_form.tw_ejercicio.item(clickedIndex,1)
        nr = twi0.text()
        count=0
        for item in self.lista_ejercicio :
            if count == clickedIndex:
                #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                obj_e_ejer_det=E_ejercicio_detalle()
                self.list_detalle=obj_e_ejer_det.buscar_ejercicios_id_ejercicio(item.id_ejercicio)

                for item2 in self.list_detalle:
                    rowPosition = self.obj_form.tw_detalle_ejerc.rowCount()
                    self.obj_form.tw_detalle_ejerc.insertRow(rowPosition)

                    self.obj_form.tw_detalle_ejerc.setItem(rowPosition , 0, QTableWidgetItem(str(item2.nro)))
                    self.obj_form.tw_detalle_ejerc.setItem(rowPosition , 1, QTableWidgetItem(item2.mes))
                    self.obj_form.tw_detalle_ejerc.setItem(rowPosition , 2, QTableWidgetItem(item2.estado))
            count = count+1

    def limpiar(self):
        self.obj_cliente=""
        self.lista_ejercicio =""
        self.list_detalle= ""
        self.index = ""
        while (self.obj_form.tw_detalle_ejerc.rowCount() > 0):
            self.obj_form.tw_detalle_ejerc.removeRow(0)
        while (self.obj_form.tw_ejercicio.rowCount() > 0):
            self.obj_form.tw_ejercicio.removeRow(0)


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
                self.obj_form.ln_nombre.setText(self.obj_cliente.razon_social)
                obj_e_ejercicio = E_ejercicio()
                self.lista_ejercicio = obj_e_ejercicio.get_ejercicio_id_cliente(self.obj_cliente.id_cliente)

                for item in self.lista_ejercicio:
                    rowPosition = self.obj_form.tw_ejercicio.rowCount()
                    self.obj_form.tw_ejercicio.insertRow(rowPosition)
                    self.obj_form.tw_ejercicio.setItem(rowPosition , 0, QTableWidgetItem(str(item.fec_inicio.year)+"-"+str(item.fec_fin.year)))
                    self.obj_form.tw_ejercicio.setItem(rowPosition , 1, QTableWidgetItem(item.descripcion))
                    self.obj_form.tw_ejercicio.setItem(rowPosition , 2, QTableWidgetItem(item.tipo))
                    self.obj_form.tw_ejercicio.setItem(rowPosition, 3, QTableWidgetItem(str(item.id_ejercicio)))

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

    def calcular_inflacion(self):
        #obtener el cliente 
        #obtener el año o ejercicio
        #obtener todos los asiente agrupados por mes
        #obtener todas las cuentas de esos asientos marcadas con inflacion
        #insertar cuenta (idem) con la inflacion calculada respetando deb o haber
        #inserta cuenta recpam con debe o a haber
        obj_asiento=E_asiento()
        obj_cuenta= E_cuenta()
        obj_inflacion = E_inflacion()
        cliente= self.obj_cliente
        ejercicio=self.id_ejercicio
        obj_ejercicio = E_ejercicio()

        result= obj_ejercicio.get_ejercicio_id_ejercicio(self.id_ejercicio)
        #buscar la lista de indices de inflacion para ese ejercicio
        anio=str(result.fec_inicio)[0:4]

        lista_inflacion=obj_inflacion.get_inflacion_anio(anio)

        for item in self.list_detalle:
            #busco en la lista 
            item_inflacion = lista_inflacion[item.nro]
            indice_inflacion=item_inflacion.valor

            lista_asientos=obj_asiento.get_asientos_detalle_ejercicio(item.id_ejercicio_detalle)
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            for item2 in lista_asientos:
                #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                obj_cuenta.borrar_cuentas_de_inflacion(item2.id_asiento)
                list_ctas_por_asient=obj_asiento.get_cuentas_asiento_filtro_inflacion(item2.id_asiento)
                asiento_debe=0
                asiento_haber=0
                asiento_id=0
                bandera_recpam_debe=False
                bandera_recpam_haber=False

                for item3 in list_ctas_por_asient:
                    #calcular valor inflacion para esa cuenta (indice * debe o haber)/100
                    #   "item3."id_plan_cuentas ,debe , haber , "item3."id_asiento 
                    #insertar cuenta idem con el calcula de la inflacion para esa cuenta
                    obj_cuenta.id_plan_cuentas =item3.id_plan_cuentas
                    if item3.debe !=0 :
                        #pyqtRemoveInputHook()
                        #import pdb; pdb.set_trace()
                        obj_cuenta.debe =(Decimal(indice_inflacion) * Decimal(item3.debe)/ 100)
                        obj_cuenta.haber = 0
                        asiento_debe=asiento_debe+obj_cuenta.debe
                        bandera_recpam_debe=True
                    else:
                        obj_cuenta.debe = 0
                        obj_cuenta.haber =( Decimal(indice_inflacion) * Decimal(item3.haber))/100
                        asiento_debe=asiento_haber + obj_cuenta.haber
                        bandera_recpam_haber=True

                    if obj_cuenta.debe !=0 or obj_cuenta.haber !=0:
                        obj_cuenta.id_asiento = item2.id_asiento
                        asiento_id=item2.id_asiento
                        obj_cuenta.guardar(obj_cuenta,  True)
               
                if bandera_recpam_haber:
                    #pyqtRemoveInputHook()
                    #import pdb; pdb.set_trace()
                    x= obj_asiento.get_id_plan_cuenta(asiento_id,"recpam")
                    obj_cuenta.id_plan_cuentas =x.id_cuenta
                    obj_cuenta.debe= 0
                    obj_cuenta.haber = 0
                    obj_cuenta.id_asiento =asiento_id
                    obj_cuenta.guardar(obj_cuenta,  True)

                if bandera_recpam_debe:
                    #pyqtRemoveInputHook()
                    #import pdb; pdb.set_trace()
                    x= obj_asiento.get_id_plan_cuenta(asiento_id,"recpam")
                    obj_cuenta.id_plan_cuentas =x.id_cuenta
                    obj_cuenta.debe = 0
                    obj_cuenta.haber = 0
                    obj_cuenta.id_asiento =asiento_id
                    obj_cuenta.guardar(obj_cuenta,  True)







            