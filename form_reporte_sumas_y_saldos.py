# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_reporte_sumas_y_saldos.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_reporte_sumas_y_saldos(object):
    def setupUi(self, form_reporte_sumas_y_saldos):
        form_reporte_sumas_y_saldos.setObjectName("form_reporte_sumas_y_saldos")
        form_reporte_sumas_y_saldos.resize(754, 141)
        form_reporte_sumas_y_saldos.setStyleSheet("font: 10pt \"Liberation Sans\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(156, 156, 156);\n"
"selection-background-color: rgb(164, 190, 221);\n"
"selection-color: rgb(0, 0, 0);")
        self.gridLayout = QtWidgets.QGridLayout(form_reporte_sumas_y_saldos)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_17 = QtWidgets.QLabel(form_reporte_sumas_y_saldos)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_19.addWidget(self.label_17)
        self.lne_cuit_2 = QtWidgets.QLineEdit(form_reporte_sumas_y_saldos)
        self.lne_cuit_2.setMinimumSize(QtCore.QSize(110, 0))
        self.lne_cuit_2.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lne_cuit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lne_cuit_2.setText("")
        self.lne_cuit_2.setObjectName("lne_cuit_2")
        self.horizontalLayout_19.addWidget(self.lne_cuit_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_18 = QtWidgets.QLabel(form_reporte_sumas_y_saldos)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_20.addWidget(self.label_18)
        self.lne_razon_social_2 = QtWidgets.QLineEdit(form_reporte_sumas_y_saldos)
        self.lne_razon_social_2.setMinimumSize(QtCore.QSize(350, 0))
        self.lne_razon_social_2.setMaximumSize(QtCore.QSize(350, 16777215))
        self.lne_razon_social_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lne_razon_social_2.setObjectName("lne_razon_social_2")
        self.horizontalLayout_20.addWidget(self.lne_razon_social_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_20)
        self.line_2 = QtWidgets.QFrame(form_reporte_sumas_y_saldos)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.btn_buscar_2 = QtWidgets.QPushButton(form_reporte_sumas_y_saldos)
        self.btn_buscar_2.setMinimumSize(QtCore.QSize(75, 50))
        self.btn_buscar_2.setMaximumSize(QtCore.QSize(75, 50))
        self.btn_buscar_2.setStyleSheet("background-color: rgb(119, 149, 177);")
        self.btn_buscar_2.setObjectName("btn_buscar_2")
        self.horizontalLayout_2.addWidget(self.btn_buscar_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(form_reporte_sumas_y_saldos)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_22 = QtWidgets.QLabel(form_reporte_sumas_y_saldos)
        self.label_22.setMinimumSize(QtCore.QSize(60, 0))
        self.label_22.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_22.setObjectName("label_22")
        self.horizontalLayout.addWidget(self.label_22)
        self.cbx_ejercicio_2 = QtWidgets.QComboBox(form_reporte_sumas_y_saldos)
        self.cbx_ejercicio_2.setMinimumSize(QtCore.QSize(110, 0))
        self.cbx_ejercicio_2.setMaximumSize(QtCore.QSize(110, 16777215))
        self.cbx_ejercicio_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.cbx_ejercicio_2.setObjectName("cbx_ejercicio_2")
        self.horizontalLayout.addWidget(self.cbx_ejercicio_2)
        self.line_5 = QtWidgets.QFrame(form_reporte_sumas_y_saldos)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout.addWidget(self.line_5)
        self.btn_buscar_asiento_2 = QtWidgets.QPushButton(form_reporte_sumas_y_saldos)
        self.btn_buscar_asiento_2.setMinimumSize(QtCore.QSize(75, 25))
        self.btn_buscar_asiento_2.setMaximumSize(QtCore.QSize(75, 25))
        self.btn_buscar_asiento_2.setStyleSheet("background-color: rgb(119, 149, 177);")
        self.btn_buscar_asiento_2.setObjectName("btn_buscar_asiento_2")
        self.horizontalLayout.addWidget(self.btn_buscar_asiento_2)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.btn_imprimir = QtWidgets.QPushButton(form_reporte_sumas_y_saldos)
        self.btn_imprimir.setStyleSheet("background-color: rgb(158, 185, 209);")
        self.btn_imprimir.setObjectName("btn_imprimir")
        self.gridLayout.addWidget(self.btn_imprimir, 3, 0, 1, 1)

        self.retranslateUi(form_reporte_sumas_y_saldos)
        QtCore.QMetaObject.connectSlotsByName(form_reporte_sumas_y_saldos)
        form_reporte_sumas_y_saldos.setTabOrder(self.lne_cuit_2, self.lne_razon_social_2)
        form_reporte_sumas_y_saldos.setTabOrder(self.lne_razon_social_2, self.btn_buscar_2)
        form_reporte_sumas_y_saldos.setTabOrder(self.btn_buscar_2, self.cbx_ejercicio_2)
        form_reporte_sumas_y_saldos.setTabOrder(self.cbx_ejercicio_2, self.btn_buscar_asiento_2)
        form_reporte_sumas_y_saldos.setTabOrder(self.btn_buscar_asiento_2, self.btn_imprimir)

    def retranslateUi(self, form_reporte_sumas_y_saldos):
        _translate = QtCore.QCoreApplication.translate
        form_reporte_sumas_y_saldos.setWindowTitle(_translate("form_reporte_sumas_y_saldos", "Reporte Sumas y Saldos"))
        self.label_17.setText(_translate("form_reporte_sumas_y_saldos", "CUIT / CUIL: "))
        self.label_18.setText(_translate("form_reporte_sumas_y_saldos", "Razón Social: "))
        self.btn_buscar_2.setText(_translate("form_reporte_sumas_y_saldos", "Buscar"))
        self.label_22.setText(_translate("form_reporte_sumas_y_saldos", "Ejercicio:"))
        self.btn_buscar_asiento_2.setText(_translate("form_reporte_sumas_y_saldos", "Buscar"))
        self.btn_imprimir.setText(_translate("form_reporte_sumas_y_saldos", "Imprimir "))

