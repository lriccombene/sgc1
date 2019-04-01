# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_balancear_asiento.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_balancear_asiento(object):
    def setupUi(self, form_balancear_asiento):
        form_balancear_asiento.setObjectName("form_balancear_asiento")
        form_balancear_asiento.resize(689, 502)
        self.btn_buscar = QtWidgets.QPushButton(form_balancear_asiento)
        self.btn_buscar.setGeometry(QtCore.QRect(490, 40, 89, 25))
        self.btn_buscar.setObjectName("btn_buscar")
        self.label = QtWidgets.QLabel(form_balancear_asiento)
        self.label.setGeometry(QtCore.QRect(80, 40, 41, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(form_balancear_asiento)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 91, 17))
        self.label_2.setObjectName("label_2")
        self.lne_cuit = QtWidgets.QLineEdit(form_balancear_asiento)
        self.lne_cuit.setGeometry(QtCore.QRect(150, 40, 231, 25))
        self.lne_cuit.setObjectName("lne_cuit")
        self.lne_razon_social = QtWidgets.QLineEdit(form_balancear_asiento)
        self.lne_razon_social.setGeometry(QtCore.QRect(150, 80, 231, 25))
        self.lne_razon_social.setObjectName("lne_razon_social")
        self.tb_asientos = QtWidgets.QTableWidget(form_balancear_asiento)
        self.tb_asientos.setGeometry(QtCore.QRect(60, 260, 551, 192))
        self.tb_asientos.setObjectName("tb_asientos")
        self.tb_asientos.setColumnCount(2)
        self.tb_asientos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_asientos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_asientos.setHorizontalHeaderItem(1, item)
        self.btn_calcular_asientos = QtWidgets.QPushButton(form_balancear_asiento)
        self.btn_calcular_asientos.setGeometry(QtCore.QRect(370, 150, 241, 25))
        self.btn_calcular_asientos.setObjectName("btn_calcular_asientos")
        self.line = QtWidgets.QFrame(form_balancear_asiento)
        self.line.setGeometry(QtCore.QRect(0, 130, 681, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(form_balancear_asiento)
        self.line_2.setGeometry(QtCore.QRect(10, 220, 691, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.cbx_ejercicio = QtWidgets.QComboBox(form_balancear_asiento)
        self.cbx_ejercicio.setGeometry(QtCore.QRect(170, 150, 101, 25))
        self.cbx_ejercicio.setObjectName("cbx_ejercicio")
        self.label_3 = QtWidgets.QLabel(form_balancear_asiento)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 91, 17))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(form_balancear_asiento)
        QtCore.QMetaObject.connectSlotsByName(form_balancear_asiento)

    def retranslateUi(self, form_balancear_asiento):
        _translate = QtCore.QCoreApplication.translate
        form_balancear_asiento.setWindowTitle(_translate("form_balancear_asiento", "Form"))
        self.btn_buscar.setText(_translate("form_balancear_asiento", "Buscar"))
        self.label.setText(_translate("form_balancear_asiento", "CUIT:"))
        self.label_2.setText(_translate("form_balancear_asiento", "Razon Social:"))
        item = self.tb_asientos.horizontalHeaderItem(0)
        item.setText(_translate("form_balancear_asiento", "Fecha"))
        item = self.tb_asientos.horizontalHeaderItem(1)
        item.setText(_translate("form_balancear_asiento", "Asiento"))
        self.btn_calcular_asientos.setText(_translate("form_balancear_asiento", "Calcular Asientos"))
        self.label_3.setText(_translate("form_balancear_asiento", "Ejercicio :"))

