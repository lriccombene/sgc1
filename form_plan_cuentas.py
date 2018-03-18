# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_plan_cuentas.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_plan_cuentas(object):
    def setupUi(self, form_plan_cuentas):
        form_plan_cuentas.setObjectName("form_plan_cuentas")
        form_plan_cuentas.resize(640, 453)
        form_plan_cuentas.setStyleSheet("color: rgb(3, 3, 3);\n"
"background-color: rgb(44, 43, 58);\n"
"font: 10pt \"Liberation Sans\";\n"
"color: rgb(252, 252, 252);\n"
"selection-background-color: rgb(155, 155, 185);")
        self.gridLayout_2 = QtWidgets.QGridLayout(form_plan_cuentas)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_15 = QtWidgets.QLabel(form_plan_cuentas)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.lne_cuit = QtWidgets.QLineEdit(form_plan_cuentas)
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
        self.label_16 = QtWidgets.QLabel(form_plan_cuentas)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.lne_razon_social = QtWidgets.QLineEdit(form_plan_cuentas)
        self.lne_razon_social.setMinimumSize(QtCore.QSize(350, 0))
        self.lne_razon_social.setMaximumSize(QtCore.QSize(350, 16777215))
        self.lne_razon_social.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lne_razon_social.setObjectName("lne_razon_social")
        self.verticalLayout_3.addWidget(self.lne_razon_social)
        self.horizontalLayout_15.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem)
        self.btn_buscar = QtWidgets.QPushButton(form_plan_cuentas)
        self.btn_buscar.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_buscar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.btn_buscar.setStyleSheet("background-color: rgb(64, 63, 78);")
        self.btn_buscar.setObjectName("btn_buscar")
        self.horizontalLayout_15.addWidget(self.btn_buscar, 0, QtCore.Qt.AlignBottom)
        self.gridLayout_2.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(form_plan_cuentas)
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
        self.tw_plan_ctas = QtWidgets.QTableWidget(self.tab)
        self.tw_plan_ctas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_plan_ctas.setObjectName("tw_plan_ctas")
        self.tw_plan_ctas.setColumnCount(2)
        self.tw_plan_ctas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tw_plan_ctas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tw_plan_ctas.setHorizontalHeaderItem(1, item)
        self.tw_plan_ctas.horizontalHeader().setDefaultSectionSize(300)
        self.gridLayout.addWidget(self.tw_plan_ctas, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(form_plan_cuentas)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(form_plan_cuentas)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lne_codigo = QtWidgets.QLineEdit(form_plan_cuentas)
        self.lne_codigo.setMinimumSize(QtCore.QSize(100, 25))
        self.lne_codigo.setMaximumSize(QtCore.QSize(100, 25))
        self.lne_codigo.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lne_codigo.setObjectName("lne_codigo")
        self.horizontalLayout.addWidget(self.lne_codigo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(form_plan_cuentas)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lne_descripcion = QtWidgets.QLineEdit(form_plan_cuentas)
        self.lne_descripcion.setMinimumSize(QtCore.QSize(400, 25))
        self.lne_descripcion.setMaximumSize(QtCore.QSize(400, 25))
        self.lne_descripcion.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lne_descripcion.setText("")
        self.lne_descripcion.setObjectName("lne_descripcion")
        self.horizontalLayout_2.addWidget(self.lne_descripcion)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.btn_agregar = QtWidgets.QPushButton(form_plan_cuentas)
        self.btn_agregar.setObjectName("btn_agregar")
        self.horizontalLayout_3.addWidget(self.btn_agregar)
        self.btn_modificar = QtWidgets.QPushButton(form_plan_cuentas)
        self.btn_modificar.setObjectName("btn_modificar")
        self.horizontalLayout_3.addWidget(self.btn_modificar, 0, QtCore.Qt.AlignRight)
        self.btn_eliminar = QtWidgets.QPushButton(form_plan_cuentas)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.horizontalLayout_3.addWidget(self.btn_eliminar, 0, QtCore.Qt.AlignRight)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.retranslateUi(form_plan_cuentas)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form_plan_cuentas)
        form_plan_cuentas.setTabOrder(self.lne_cuit, self.lne_razon_social)
        form_plan_cuentas.setTabOrder(self.lne_razon_social, self.btn_buscar)
        form_plan_cuentas.setTabOrder(self.btn_buscar, self.tabWidget)
        form_plan_cuentas.setTabOrder(self.tabWidget, self.tw_plan_ctas)
        form_plan_cuentas.setTabOrder(self.tw_plan_ctas, self.lne_codigo)
        form_plan_cuentas.setTabOrder(self.lne_codigo, self.lne_descripcion)
        form_plan_cuentas.setTabOrder(self.lne_descripcion, self.btn_agregar)
        form_plan_cuentas.setTabOrder(self.btn_agregar, self.btn_modificar)
        form_plan_cuentas.setTabOrder(self.btn_modificar, self.btn_eliminar)

    def retranslateUi(self, form_plan_cuentas):
        _translate = QtCore.QCoreApplication.translate
        form_plan_cuentas.setWindowTitle(_translate("form_plan_cuentas", "Plan de Cuentas"))
        self.label_15.setText(_translate("form_plan_cuentas", "CUIT / CUIL: "))
        self.label_16.setText(_translate("form_plan_cuentas", "Razón Social: "))
        self.btn_buscar.setText(_translate("form_plan_cuentas", "Buscar"))
        item = self.tw_plan_ctas.horizontalHeaderItem(0)
        item.setText(_translate("form_plan_cuentas", "Código"))
        item = self.tw_plan_ctas.horizontalHeaderItem(1)
        item.setText(_translate("form_plan_cuentas", "Descripción"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("form_plan_cuentas", "Plan de Cuentas "))
        self.label_3.setText(_translate("form_plan_cuentas", "Plan"))
        self.label.setText(_translate("form_plan_cuentas", "Código: "))
        self.label_2.setText(_translate("form_plan_cuentas", "Descripción:"))
        self.btn_agregar.setText(_translate("form_plan_cuentas", "Agregar"))
        self.btn_modificar.setText(_translate("form_plan_cuentas", "Modificar"))
        self.btn_eliminar.setText(_translate("form_plan_cuentas", "Eliminar"))

