#-------------------------------------------------
#
# Project created by QtCreator 2018-02-12T20:11:37
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = Sistema_Gestion_Contable
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp

HEADERS  += mainwindow.h

FORMS    += mainwindow.ui \
    form_clientes.ui \
    form_libro_diario.ui \
    form_libro_iva_compras.ui \
    form_libro_iva_compras_nuevo.ui \
    form_libro_iva_ventas.ui \
    form_libro_iva_ventas_nuevo.ui \
    form_proveedores.ui \
    form_ejercicio_nuevo.ui \
    form_ejercicio.ui \
    form_plan_cuentas.ui \
    form_cuentas.ui \
    form_asiento.ui \
    form_cuentas_nuevo.ui \
    form_reporte_diario_gral.ui \
    form_reporte_sumas_y_saldos.ui \
    form_reporte_libro_mayor.ui \
    form_inflacion.ui
