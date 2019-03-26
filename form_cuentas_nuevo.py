# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_cuentas_nuevo.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_cuentas_nuevo(object):
    def setupUi(self, form_cuentas_nuevo):
        form_cuentas_nuevo.setObjectName("form_cuentas_nuevo")
        form_cuentas_nuevo.resize(410, 194)
        form_cuentas_nuevo.setStyleSheet("font: 10pt \"Liberation Sans\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(156, 156, 156);\n"
"selection-background-color: rgb(164, 190, 221);\n"
"selection-color: rgb(0, 0, 0);")
        self.gridLayout = QtWidgets.QGridLayout(form_cuentas_nuevo)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(form_cuentas_nuevo)
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
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setMinimumSize(QtCore.QSize(43, 25))
        self.label.setMaximumSize(QtCore.QSize(43, 25))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cbx_cuenta = QtWidgets.QComboBox(self.tab)
        self.cbx_cuenta.setMinimumSize(QtCore.QSize(250, 25))
        self.cbx_cuenta.setMaximumSize(QtCore.QSize(250, 25))
        self.cbx_cuenta.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.cbx_cuenta.setObjectName("cbx_cuenta")
        self.horizontalLayout.addWidget(self.cbx_cuenta)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setMinimumSize(QtCore.QSize(43, 25))
        self.label_2.setMaximumSize(QtCore.QSize(43, 25))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lne_debe = QtWidgets.QLineEdit(self.tab)
        self.lne_debe.setEnabled(True)
        self.lne_debe.setMinimumSize(QtCore.QSize(100, 25))
        self.lne_debe.setMaximumSize(QtCore.QSize(100, 25))
        self.lne_debe.setObjectName("lne_debe")
        self.horizontalLayout_2.addWidget(self.lne_debe)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setMinimumSize(QtCore.QSize(43, 25))
        self.label_3.setMaximumSize(QtCore.QSize(43, 25))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lne_haber = QtWidgets.QLineEdit(self.tab)
        self.lne_haber.setMinimumSize(QtCore.QSize(100, 25))
        self.lne_haber.setMaximumSize(QtCore.QSize(100, 25))
        self.lne_haber.setObjectName("lne_haber")
        self.horizontalLayout_3.addWidget(self.lne_haber)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.btn_guardar = QtWidgets.QPushButton(self.tab)
        self.btn_guardar.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_guardar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.btn_guardar.setStyleSheet("background-color: rgb(119, 149, 177);")
        self.btn_guardar.setObjectName("btn_guardar")
        self.verticalLayout_2.addWidget(self.btn_guardar, 0, QtCore.Qt.AlignRight)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(form_cuentas_nuevo)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form_cuentas_nuevo)

    def retranslateUi(self, form_cuentas_nuevo):
        _translate = QtCore.QCoreApplication.translate
        form_cuentas_nuevo.setWindowTitle(_translate("form_cuentas_nuevo", "Nueva Cuenta"))
        self.label.setText(_translate("form_cuentas_nuevo", "Cuenta:"))
        self.label_2.setText(_translate("form_cuentas_nuevo", "Debe:"))
        self.label_3.setText(_translate("form_cuentas_nuevo", "Haber: "))
        self.btn_guardar.setText(_translate("form_cuentas_nuevo", "Guardar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("form_cuentas_nuevo", "Cuentas"))

