import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from form_inflacion import Ui_form_inflacion
from PyQt5.QtCore import pyqtRemoveInputHook
from E_inflacion import E_inflacion


class inflacion(QWidget):
    obj_form= Ui_form_inflacion()
    


    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_inflacion()
        self.obj_form.setupUi(self)
        self.obj_form.btn_buscar.clicked.connect(self.buscar)
        self.obj_form.btn_guardar.clicked.connect(self.guardar)
        self.obj_form.btn_actualizar.clicked.connect(self.actualizar)



    def actualizar(self):
        obj_inflacion=E_inflacion()
        obj_inflacion.anio= self.obj_form.cbx_anio.currentText()
        
        obj_inflacion.nro_mes = 1
        obj_inflacion.valor = self.obj_form.lne_enero.text()
        obj_inflacion.actualizar(obj_inflacion)

        obj_inflacion.nro_mes = 2
        obj_inflacion.valor = self.obj_form.lne_febrero.text()
        obj_inflacion.actualizar(obj_inflacion)

        obj_inflacion.nro_mes = 3
        obj_inflacion.valor = self.obj_form.lne_marzo.text()
        obj_inflacion.actualizar(obj_inflacion)

        obj_inflacion.nro_mes = 4
        obj_inflacion.valor = self.obj_form.lne_abril.text()
        obj_inflacion.actualizar(obj_inflacion)

        obj_inflacion.nro_mes = 5
        obj_inflacion.valor = self.obj_form.lne_mayo.text()
        obj_inflacion.actualizar(obj_inflacion)

        obj_inflacion.nro_mes = 6
        obj_inflacion.valor = self.obj_form.lne_junio.text()
        obj_inflacion.actualizar(obj_inflacion)
        
        obj_inflacion.nro_mes = 7
        obj_inflacion.valor = self.obj_form.lne_julio.text()
        obj_inflacion.actualizar(obj_inflacion)

        obj_inflacion.nro_mes = 8
        obj_inflacion.valor = self.obj_form.lne_agosto.text()
        obj_inflacion.actualizar(obj_inflacion)

        obj_inflacion.nro_mes = 9
        obj_inflacion.valor = self.obj_form.lne_septiembre.text()
        obj_inflacion.actualizar(obj_inflacion)

        obj_inflacion.nro_octubre = 10
        obj_inflacion.valor = self.obj_form.lne_octubre.text()
        obj_inflacion.actualizar(obj_inflacion)

        obj_inflacion.nro_mes = 11
        obj_inflacion.valor = self.obj_form.lne_noviembre.text()
        obj_inflacion.actualizar(obj_inflacion)

        obj_inflacion.nro_mes = 12
        obj_inflacion.valor = self.obj_form.lne_diciembre.text()
        obj_inflacion.actualizar(obj_inflacion)
        
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Atencion")
        msgBox.setText('Se actualizo correctamente')
        msgBox.exec_()


    def guardar(self):
        obj_inflacion=E_inflacion()
        anio= self.obj_form.cbx_anio.currentText()
        list_inflacion= obj_inflacion.get_inflacion_anio(anio)
        if (len(list_inflacion) ==0 ):
            obj_inflacion=E_inflacion()
            obj_inflacion.anio= self.obj_form.cbx_anio.currentText()
            
            obj_inflacion.nro_mes = 1
            obj_inflacion.mes = "enero"
            obj_inflacion.valor = self.obj_form.lne_enero.text()
            obj_inflacion.guardar(obj_inflacion)

            obj_inflacion.nro_mes = 2
            obj_inflacion.mes = "febrero"
            obj_inflacion.valor = self.obj_form.lne_febrero.text()
            obj_inflacion.guardar(obj_inflacion)

            obj_inflacion.nro_mes = 3
            obj_inflacion.mes = "marzo"
            obj_inflacion.valor = self.obj_form.lne_marzo.text()
            obj_inflacion.guardar(obj_inflacion)

            obj_inflacion.nro_mes = 4
            obj_inflacion.mes = "abril"
            obj_inflacion.valor = self.obj_form.lne_abril.text()
            obj_inflacion.guardar(obj_inflacion)

            obj_inflacion.nro_mes = 5
            obj_inflacion.mes = "mayo"
            obj_inflacion.valor = self.obj_form.lne_mayo.text()
            obj_inflacion.guardar(obj_inflacion)

            obj_inflacion.nro_mes = 6
            obj_inflacion.mes = "junio"
            obj_inflacion.valor = self.obj_form.lne_junio.text()
            obj_inflacion.guardar(obj_inflacion)
            
            obj_inflacion.nro_mes = 7
            obj_inflacion.mes = "julio"
            obj_inflacion.valor = self.obj_form.lne_julio.text()
            obj_inflacion.guardar(obj_inflacion)

            obj_inflacion.nro_mes = 8
            obj_inflacion.mes = "agosto"
            obj_inflacion.valor = self.obj_form.lne_agosto.text()
            obj_inflacion.guardar(obj_inflacion)

            obj_inflacion.nro_mes = 9
            obj_inflacion.mes = "septiembre"
            obj_inflacion.valor = self.obj_form.lne_septiembre.text()
            obj_inflacion.guardar(obj_inflacion)

            obj_inflacion.nro_mes = 10
            obj_inflacion.mes = "octubre"
            obj_inflacion.valor = self.obj_form.lne_octubre.text()
            obj_inflacion.guardar(obj_inflacion)

            obj_inflacion.nro_mes = 11
            obj_inflacion.mes = "noviembre"
            obj_inflacion.valor = self.obj_form.lne_noviembre.text()
            obj_inflacion.guardar(obj_inflacion)

            obj_inflacion.nro_mes = 12
            obj_inflacion.mes = "diciembre"
            obj_inflacion.valor = self.obj_form.lne_diciembre.text()
            obj_inflacion.guardar(obj_inflacion)
        else:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Atencion")
            msgBox.setText('Ya existe inflacion para ese año')
            msgBox.exec_()
           
        

    def buscar(self):
        anio= self.obj_form.cbx_anio.currentText()
        obj_inflacion=E_inflacion()
        list_inflacion= obj_inflacion.get_inflacion_anio(anio)
        for item in list_inflacion:
            if item.nro_mes== 1:
                self.obj_form.lne_enero.setText(str(item.valor))
            if item.nro_mes== 2:
                self.obj_form.lne_febrero.setText(str(item.valor))
            if item.nro_mes== 3:
                self.obj_form.lne_marzo.setText(str(item.valor))
            if item.nro_mes== 4:
                self.obj_form.lne_abril.setText(str(item.valor))
            if item.nro_mes== 5:
                self.obj_form.lne_mayo.setText(str(item.valor))
            if item.nro_mes== 6:
                self.obj_form.lne_junio.setText(str(item.valor))
            if item.nro_mes== 7:
                self.obj_form.lne_julio.setText(str(item.valor))
            if item.nro_mes== 8:
                self.obj_form.lne_agosto.setText(str(item.valor))
            if item.nro_mes== 9:
                self.obj_form.lne_septiembre.setText(str(item.valor))
            if item.nro_mes==10:
                self.obj_form.lne_octubre.setText(str(item.valor))
            if item.nro_mes== 11:
                self.obj_form.lne_noviembre.setText(str(item.valor))
            if item.nro_mes== 12:
                self.obj_form.lne_diciembre.setText(str(item.valor))






