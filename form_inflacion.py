# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_inflacion.ui'
#
# Created: Sun Mar 24 10:27:51 2019
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_inflacion(object):
    def setupUi(self, form_inflacion):
        form_inflacion.setObjectName("form_inflacion")
        form_inflacion.resize(640, 480)
        self.cbx_anio = QtWidgets.QComboBox(form_inflacion)
        self.cbx_anio.setGeometry(QtCore.QRect(200, 20, 79, 23))
        self.cbx_anio.setObjectName("cbx_anio")
        self.cbx_anio.addItem("")
        self.cbx_anio.addItem("")
        self.cbx_anio.addItem("")
        self.cbx_anio.addItem("")
        self.label = QtWidgets.QLabel(form_inflacion)
        self.label.setGeometry(QtCore.QRect(240, 100, 59, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(form_inflacion)
        self.label_2.setGeometry(QtCore.QRect(240, 130, 59, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(form_inflacion)
        self.label_3.setGeometry(QtCore.QRect(240, 160, 59, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(form_inflacion)
        self.label_4.setGeometry(QtCore.QRect(240, 190, 59, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(form_inflacion)
        self.label_5.setGeometry(QtCore.QRect(240, 220, 59, 15))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(form_inflacion)
        self.label_6.setGeometry(QtCore.QRect(240, 260, 59, 15))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(form_inflacion)
        self.label_7.setGeometry(QtCore.QRect(250, 280, 31, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(form_inflacion)
        self.label_8.setGeometry(QtCore.QRect(240, 310, 59, 15))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(form_inflacion)
        self.label_9.setGeometry(QtCore.QRect(220, 340, 59, 15))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(form_inflacion)
        self.label_10.setGeometry(QtCore.QRect(230, 380, 59, 15))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(form_inflacion)
        self.label_11.setGeometry(QtCore.QRect(220, 410, 59, 15))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(form_inflacion)
        self.label_12.setGeometry(QtCore.QRect(220, 430, 59, 15))
        self.label_12.setObjectName("label_12")
        self.lne_enero = QtWidgets.QLineEdit(form_inflacion)
        self.lne_enero.setGeometry(QtCore.QRect(310, 100, 51, 21))
        self.lne_enero.setObjectName("lne_enero")
        self.lne_febrero = QtWidgets.QLineEdit(form_inflacion)
        self.lne_febrero.setGeometry(QtCore.QRect(310, 130, 51, 21))
        self.lne_febrero.setObjectName("lne_febrero")
        self.lne_marzo = QtWidgets.QLineEdit(form_inflacion)
        self.lne_marzo.setGeometry(QtCore.QRect(310, 160, 51, 21))
        self.lne_marzo.setObjectName("lne_marzo")
        self.lne_abril = QtWidgets.QLineEdit(form_inflacion)
        self.lne_abril.setGeometry(QtCore.QRect(310, 190, 51, 21))
        self.lne_abril.setObjectName("lne_abril")
        self.lne_mayo = QtWidgets.QLineEdit(form_inflacion)
        self.lne_mayo.setGeometry(QtCore.QRect(310, 220, 51, 21))
        self.lne_mayo.setObjectName("lne_mayo")
        self.lne_junio = QtWidgets.QLineEdit(form_inflacion)
        self.lne_junio.setGeometry(QtCore.QRect(310, 250, 51, 21))
        self.lne_junio.setObjectName("lne_junio")
        self.lne_julio = QtWidgets.QLineEdit(form_inflacion)
        self.lne_julio.setGeometry(QtCore.QRect(310, 280, 51, 21))
        self.lne_julio.setObjectName("lne_julio")
        self.lne_agosto = QtWidgets.QLineEdit(form_inflacion)
        self.lne_agosto.setGeometry(QtCore.QRect(310, 310, 51, 21))
        self.lne_agosto.setObjectName("lne_agosto")
        self.lne_septiembre = QtWidgets.QLineEdit(form_inflacion)
        self.lne_septiembre.setGeometry(QtCore.QRect(310, 340, 51, 21))
        self.lne_septiembre.setObjectName("lne_septiembre")
        self.lne_octubre = QtWidgets.QLineEdit(form_inflacion)
        self.lne_octubre.setGeometry(QtCore.QRect(310, 370, 51, 21))
        self.lne_octubre.setObjectName("lne_octubre")
        self.lne_noviembre = QtWidgets.QLineEdit(form_inflacion)
        self.lne_noviembre.setGeometry(QtCore.QRect(310, 400, 51, 21))
        self.lne_noviembre.setObjectName("lne_noviembre")
        self.lne_diciembre = QtWidgets.QLineEdit(form_inflacion)
        self.lne_diciembre.setGeometry(QtCore.QRect(310, 430, 51, 21))
        self.lne_diciembre.setObjectName("lne_diciembre")
        self.btn_guardar = QtWidgets.QPushButton(form_inflacion)
        self.btn_guardar.setGeometry(QtCore.QRect(480, 80, 80, 23))
        self.btn_guardar.setObjectName("btn_guardar")
        self.btn_actualizar = QtWidgets.QPushButton(form_inflacion)
        self.btn_actualizar.setGeometry(QtCore.QRect(480, 120, 80, 23))
        self.btn_actualizar.setObjectName("btn_actualizar")
        self.btn_buscar = QtWidgets.QPushButton(form_inflacion)
        self.btn_buscar.setGeometry(QtCore.QRect(330, 20, 80, 23))
        self.btn_buscar.setObjectName("btn_buscar")

        self.retranslateUi(form_inflacion)
        QtCore.QMetaObject.connectSlotsByName(form_inflacion)

    def retranslateUi(self, form_inflacion):
        _translate = QtCore.QCoreApplication.translate
        form_inflacion.setWindowTitle(_translate("form_inflacion", "Form"))
        self.cbx_anio.setItemText(0, _translate("form_inflacion", "2017"))
        self.cbx_anio.setItemText(1, _translate("form_inflacion", "2018"))
        self.cbx_anio.setItemText(2, _translate("form_inflacion", "2019"))
        self.cbx_anio.setItemText(3, _translate("form_inflacion", "2020"))
        self.label.setText(_translate("form_inflacion", "Enero"))
        self.label_2.setText(_translate("form_inflacion", "febrero"))
        self.label_3.setText(_translate("form_inflacion", "marzo"))
        self.label_4.setText(_translate("form_inflacion", "abril"))
        self.label_5.setText(_translate("form_inflacion", "mayo"))
        self.label_6.setText(_translate("form_inflacion", "junio"))
        self.label_7.setText(_translate("form_inflacion", "julio"))
        self.label_8.setText(_translate("form_inflacion", "agosto"))
        self.label_9.setText(_translate("form_inflacion", "septiembre"))
        self.label_10.setText(_translate("form_inflacion", "octubre"))
        self.label_11.setText(_translate("form_inflacion", "noviembre"))
        self.label_12.setText(_translate("form_inflacion", "diciembre"))
        self.btn_guardar.setText(_translate("form_inflacion", "guardar"))
        self.btn_actualizar.setText(_translate("form_inflacion", "actualizar"))
        self.btn_buscar.setText(_translate("form_inflacion", "buscar"))
