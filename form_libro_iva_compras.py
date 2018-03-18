# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_libro_iva_compras.ui'
#
# Created: Wed Feb 14 21:25:25 2018
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_libro_iva_compras(object):
    def setupUi(self, form_libro_iva_compras):
        form_libro_iva_compras.setObjectName("form_libro_iva_compras")
        form_libro_iva_compras.resize(753, 412)
        form_libro_iva_compras.setStyleSheet("color: rgb(3, 3, 3);\n"
"background-color: rgb(44, 43, 58);\n"
"font: 10pt \"Liberation Sans\";\n"
"color: rgb(252, 252, 252);\n"
"selection-background-color: rgb(155, 155, 185);")
        self.gridLayout_2 = QtWidgets.QGridLayout(form_libro_iva_compras)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_15 = QtWidgets.QLabel(form_libro_iva_compras)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.lne_cuit = QtWidgets.QLineEdit(form_libro_iva_compras)
        self.lne_cuit.setMinimumSize(QtCore.QSize(110, 0))
        self.lne_cuit.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lne_cuit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lne_cuit.setText("")
        self.lne_cuit.setObjectName("lne_cuit")
        self.verticalLayout_2.addWidget(self.lne_cuit)
        self.horizontalLayout_15.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_16 = QtWidgets.QLabel(form_libro_iva_compras)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.lne_razon_social = QtWidgets.QLineEdit(form_libro_iva_compras)
        self.lne_razon_social.setMinimumSize(QtCore.QSize(350, 0))
        self.lne_razon_social.setMaximumSize(QtCore.QSize(350, 16777215))
        self.lne_razon_social.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lne_razon_social.setObjectName("lne_razon_social")
        self.verticalLayout_3.addWidget(self.lne_razon_social)
        self.horizontalLayout_15.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem)
        self.btn_buscar = QtWidgets.QPushButton(form_libro_iva_compras)
        self.btn_buscar.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_buscar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.btn_buscar.setStyleSheet("background-color: rgb(64, 63, 78);")
        self.btn_buscar.setObjectName("btn_buscar")
        self.horizontalLayout_15.addWidget(self.btn_buscar)
        self.gridLayout_2.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(form_libro_iva_compras)
        self.tabWidget.setStyleSheet("QTabWidget{\n"
"background-color: rgb(123, 121, 143);\n"
"}\n"
"QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.tw_compras = QtWidgets.QTableWidget(self.tab)
        self.tw_compras.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_compras.setObjectName("tw_compras")
        self.tw_compras.setColumnCount(4)
        self.tw_compras.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_compras.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_compras.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_compras.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_compras.setHorizontalHeaderItem(3, item)
        self.tw_compras.horizontalHeader().setDefaultSectionSize(175)
        self.gridLayout.addWidget(self.tw_compras, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lne_resultado_uno = QtWidgets.QLineEdit(self.tab)
        self.lne_resultado_uno.setMinimumSize(QtCore.QSize(0, 25))
        self.lne_resultado_uno.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lne_resultado_uno.setObjectName("lne_resultado_uno")
        self.horizontalLayout_4.addWidget(self.lne_resultado_uno)
        self.lne_resultado_dos = QtWidgets.QLineEdit(self.tab)
        self.lne_resultado_dos.setMinimumSize(QtCore.QSize(0, 25))
        self.lne_resultado_dos.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lne_resultado_dos.setObjectName("lne_resultado_dos")
        self.horizontalLayout_4.addWidget(self.lne_resultado_dos)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_eliminar = QtWidgets.QPushButton(self.tab)
        self.btn_eliminar.setMinimumSize(QtCore.QSize(75, 25))
        self.btn_eliminar.setMaximumSize(QtCore.QSize(75, 25))
        self.btn_eliminar.setStyleSheet("background-color: rgb(64, 63, 78);")
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.horizontalLayout.addWidget(self.btn_eliminar)
        self.btn_modificar = QtWidgets.QPushButton(self.tab)
        self.btn_modificar.setStyleSheet("background-color: rgb(64, 63, 78);")
        self.btn_modificar.setObjectName("btn_modificar")
        self.horizontalLayout.addWidget(self.btn_modificar)
        self.btn_nuevo = QtWidgets.QPushButton(self.tab)
        self.btn_nuevo.setStyleSheet("background-color: rgb(64, 63, 78);")
        self.btn_nuevo.setObjectName("btn_nuevo")
        self.horizontalLayout.addWidget(self.btn_nuevo)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.retranslateUi(form_libro_iva_compras)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form_libro_iva_compras)
        form_libro_iva_compras.setTabOrder(self.lne_cuit, self.lne_razon_social)
        form_libro_iva_compras.setTabOrder(self.lne_razon_social, self.btn_buscar)
        form_libro_iva_compras.setTabOrder(self.btn_buscar, self.tabWidget)
        form_libro_iva_compras.setTabOrder(self.tabWidget, self.btn_eliminar)
        form_libro_iva_compras.setTabOrder(self.btn_eliminar, self.btn_nuevo)
        form_libro_iva_compras.setTabOrder(self.btn_nuevo, self.btn_modificar)
        form_libro_iva_compras.setTabOrder(self.btn_modificar, self.tw_compras)
        form_libro_iva_compras.setTabOrder(self.tw_compras, self.lne_resultado_uno)
        form_libro_iva_compras.setTabOrder(self.lne_resultado_uno, self.lne_resultado_dos)

    def retranslateUi(self, form_libro_iva_compras):
        _translate = QtCore.QCoreApplication.translate
        form_libro_iva_compras.setWindowTitle(_translate("form_libro_iva_compras", "Libro IVA Compras"))
        self.label_15.setText(_translate("form_libro_iva_compras", "CUIT / CUIL: "))
        self.label_16.setText(_translate("form_libro_iva_compras", "Razón Social: "))
        self.btn_buscar.setText(_translate("form_libro_iva_compras", "Buscar"))
        item = self.tw_compras.horizontalHeaderItem(0)
        item.setText(_translate("form_libro_iva_compras", "Fecha"))
        item = self.tw_compras.horizontalHeaderItem(1)
        item.setText(_translate("form_libro_iva_compras", "N° Comprobante"))
        item = self.tw_compras.horizontalHeaderItem(2)
        item.setText(_translate("form_libro_iva_compras", "Proveedor"))
        item = self.tw_compras.horizontalHeaderItem(3)
        item.setText(_translate("form_libro_iva_compras", "Neto"))
        self.label_3.setText(_translate("form_libro_iva_compras", "Resultado: "))
        self.btn_eliminar.setText(_translate("form_libro_iva_compras", "Eliminar"))
        self.btn_modificar.setText(_translate("form_libro_iva_compras", "Actualizar"))
        self.btn_nuevo.setText(_translate("form_libro_iva_compras", "Nuevo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("form_libro_iva_compras", "Libro IVA Compras "))

