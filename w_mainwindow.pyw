import sys,datetime
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem,QMainWindow
from mainwindow import Ui_MainWindow
from PyQt5 import uic
from PyQt5.QtCore import pyqtRemoveInputHook

from w_form_asiento import asiento
from w_form_clientes import clientes
from w_form_cuentas import cuentas
from w_form_ejercicio import ejercicio
from w_form_ejercicio_nuevo import ejercicio_nuevo
from w_form_libro_diario import libro_diario
from w_form_libro_iva_compras import libro_iva_compras
from w_form_libro_iva_compras_nuevo import libro_iva_compras_nuevo
from w_form_libro_iva_ventas import libro_iva_ventas
from w_form_libro_iva_ventas_nuevo import libro_iva_ventas_nuevo
from w_form_plan_cuentas import plan_cuentas
from w_form_proveedores import proveedores
from w_form_cuentas_nuevas import cuentas_nuevas



class Mainwindow(QMainWindow):

    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        self.obj_form_main = Ui_MainWindow()
        self.obj_form_main.setupUi(self)
        self.obj_form_main.actionAsiento.triggered.connect(self.asiento)
        self.obj_form_main.actionClientes.triggered.connect(self.clientes)
        self.obj_form_main.actionBuscar_Cuenta.triggered.connect(self.cuentas)
        self.obj_form_main.actionNueva_Cuenta.triggered.connect(self.cuentas_nuevas)

        self.obj_form_main.actionEjercicio.triggered.connect(self.ejercicio)
        self.obj_form_main.actionNuevo_Ejercicio.triggered.connect(self.ejercicio_nuevo)
        self.obj_form_main.actionLIBRO_DIARIO.triggered.connect(self.libro_diario)
        self.obj_form_main.actionBuscar.triggered.connect(self.libro_iva_compras)
        self.obj_form_main.actionNuevo_2.triggered.connect(self.libro_iva_compras_nuevo)
        self.obj_form_main.actionBuscar_2.triggered.connect(self.libro_iva_ventas)
        self.obj_form_main.actionNuevo.triggered.connect(self.libro_iva_ventas_nuevo)
        self.obj_form_main.actionPlan_Cuentas.triggered.connect(self.plan_cuentas)
        self.obj_form_main.actionAlta_de_proveedores.triggered.connect(self.proveedores)


    def cuentas_nuevas(self):
        self.form_cuentas_nuevas = cuentas_nuevas()
        self.form_cuentas_nuevas.show()


    def asiento(self):
        self.form_asiento = asiento()
        self.form_asiento.show()

    def clientes(self):
        self.form_clientes = clientes()
        self.form_clientes.show()

    def cuentas(self):
        self.form_cuentas = cuentas()
        self.form_cuentas.show()

    def ejercicio(self):
        self.form_ejercicio = ejercicio()
        self.form_ejercicio.show()

    def ejercicio_nuevo(self):
        self.form_ejercicio_nuevo = ejercicio_nuevo()
        self.form_ejercicio_nuevo.show()

    def libro_diario(self):
        self.form_libro_diario = libro_diario()
        self.form_libro_diario.show()

    def libro_iva_compras(self):
        self.form_libro_iva_compras = libro_iva_compras()
        self.form_libro_iva_compras.show()

    def libro_iva_compras_nuevo(self):
        self.form_libro_iva_compras_nuevo = libro_iva_compras_nuevo()
        self.form_libro_iva_compras_nuevo.show()

    def libro_iva_ventas(self):
        self.form_libro_iva_ventas = libro_iva_ventas()
        self.form_libro_iva_ventas.show()

    def libro_iva_ventas_nuevo(self):
        self.form_libro_iva_ventas_nuevo = libro_iva_ventas_nuevo()
        self.form_libro_iva_ventas_nuevo.show()

    def plan_cuentas(self):
        self.form_plan_cuentas = plan_cuentas()
        self.form_plan_cuentas.show()

    def proveedores(self):
        self.form_proveedores = proveedores()
        self.form_proveedores.show()



app = QApplication(sys.argv)
dialogo= Mainwindow()
dialogo.show()

app.exec_()

