import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_libro_iva_ventas import Ui_form_libro_iva_ventas
from PyQt5.QtCore import pyqtRemoveInputHook

class libro_iva_ventas(QDialog):
    obj_form= Ui_form_libro_iva_ventas()

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_libro_iva_ventas()
        self.obj_form.setupUi(self)
