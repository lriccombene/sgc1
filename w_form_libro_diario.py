import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_libro_diario import Ui_form_libro_diario
from PyQt5.QtCore import pyqtRemoveInputHook

class libro_diario(QDialog):
    obj_form= Ui_form_libro_diario()

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_libro_diario()
        self.obj_form.setupUi(self)
