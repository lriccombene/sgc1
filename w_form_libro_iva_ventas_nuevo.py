import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_libro_iva_ventas_nuevo import Ui_form_libro_iva_ventas_nuevo
from PyQt5.QtCore import pyqtRemoveInputHook

class libro_iva_ventas_nuevo(QDialog):
    obj_form= Ui_form_libro_iva_ventas_nuevo()

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_libro_iva_ventas_nuevo()
        self.obj_form.setupUi(self)
