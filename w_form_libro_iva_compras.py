import sys,datetime,os,subprocess
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_libro_iva_compras import Ui_form_libro_iva_compras
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5.QtWidgets import QFileDialog
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle, Frame
from reportlab.platypus import Paragraph, Image
from reportlab.lib import colors
from E_configuracion import configuracion
from E_plan_cuentas import E_plan_cuentas
from E_ejercicio import E_ejercicio
from E_asiento import E_asiento
from w_form_libro_iva_compras_nuevo import libro_iva_compras_nuevo
from E_cliente import E_cliente
from E_ejercicio_detalle import E_ejercicio_detalle
from E_libro_iva_compras import E_libro_iva_compras


class libro_iva_compras(QDialog):
    obj_form= Ui_form_libro_iva_compras()
    lista_plancuenta = list()
    obj_cliente = ""
    lista_asiento = ""
    lista_ejercicio = ""

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_libro_iva_compras()
        self.obj_form.setupUi(self)
        self.obj_form.btn_buscar.clicked.connect(self.buscar)
        #self.obj_form.cbx_asiento.clicked.connect(self.agregar_asientos)
        self.obj_form.btn_nuevo.clicked.connect(self.nuevo)
        self.obj_form.btn_buscar_2.clicked.connect(self.grilla)
        #self.obj_form.btn_imprimir.clicked.connect(self.imprimir)



    def imprimir(self):
        obj_ejercicio = ""
        for item in self.lista_ejercicio:
            if item.descripcion == self.obj_form.cbx_ejercicio.currentText():
                obj_ejercicio = item

        obj_e_reporte = E_libro_iva_compras()
        lista_libro_iva_compras = obj_e_reporte.get_reporte_libro_iva_compras(str(obj_ejercicio.id_ejercicio))

        styleSheet = getSampleStyleSheet()
        otro_estilo = ParagraphStyle('', fontSize=8, textColor='#000', leftIndent=150, rightIndent=50)

        style_barra = ParagraphStyle('', fontSize=10, textColor='#000', leftIndent=0, rightIndent=50)
        texto_principal = ""
        texto_secundario = ParagraphStyle('', fontSize=10, textColor='#000', leftIndent=200, rightIndent=1)
        estilo_texto = ParagraphStyle('',
                                      fontSize=7,
                                      alignment=0,
                                      spaceBefore=0,
                                      spaceAfter=0,
                                      # backColor = '#fff',
                                      textColor='#000',
                                      leftIndent=5)
        estilo_detalle_cuota = ParagraphStyle('', fontSize=10, textColor='#000', leftIndent=0, rightIndent=0)

        options = QFileDialog.Options()
        story = []

        P = Paragraph("<u> Libro Iva compras </u> ", otro_estilo)
        story.append(P)
        story.append(Spacer(0, 2))

        título = [[Paragraph('''<b> </b>''', styleSheet["BodyText"])],
                  [Paragraph(' <b> EJERCICIO N° ' + str(obj_ejercicio.descripcion) + ":" '</b>' + "   " + str(
                      obj_ejercicio.fec_inicio) + " al " + str(obj_ejercicio.fec_fin), estilo_texto),
                   Paragraph(' <b>Fecha: ''</b>' + str(datetime.datetime.today()), estilo_texto)]]

        t = Table(título, (250, 250))
        t.setStyle(TableStyle([
            ('INNERGRID', (0, 1), (-1, -1), 0.25, colors.lightblue),
            ('BOX', (0, 1), (-1, -1), 0.25, colors.white),
            ('BACKGROUND', (0, 1), (-1, 1), colors.lightblue)
        ]))

        story.append(t)
        story.append(Spacer(0, -15))

        cabezal = [[Paragraph('''<b> </b>''', styleSheet["BodyText"])],
                   [Paragraph(' <b> FECHA </b> ', estilo_texto),
                    Paragraph('<b> N°Comprobante </b> ', estilo_texto),
                    Paragraph('<b> Tipo </b> ', estilo_texto),
                    Paragraph('<b> Ref </b> ', estilo_texto),
                    Paragraph('<b> Proveedor </b> ', estilo_texto),
                    Paragraph('<b> Condicion ante el iva </b> ', estilo_texto),
                    Paragraph('<b> CUIT </b> ', estilo_texto),
                    Paragraph('<b> 10,5% </b> ', estilo_texto),
                    Paragraph('<b> 21% </b> ', estilo_texto),
                    Paragraph('<b> 27% </b> ', estilo_texto),
                    Paragraph('<b> Monotributo </b> ', estilo_texto),
                    Paragraph('<b> No Grav/op exentas </b> ', estilo_texto),
                    Paragraph('<b> IVA </b> ', estilo_texto),
                    Paragraph('<b> Percp Ibb </b> ', estilo_texto),
                    Paragraph('<b> IMP Gasoil</b> ', estilo_texto),
                    Paragraph('<b> Percp Iva </b> ', estilo_texto),
                    Paragraph('<b> Total </b> ', estilo_texto)]]

        t = ""

        asiento = ""
        saldo = 0
        plan = ""
        pyqtRemoveInputHook()
        import pdb;
        pdb.set_trace()
        for item in lista_libro_iva_compras:

           estilofecha = "<font size=6>" + str(item[1]) + "</font>"
           estilonrocomprovante = "<font size=6>" + str(item[2]) + " </font>"
           estilotipo = "<font size=6>" + str(item[3]) + "</font>"
           estiloref = "<font size=6>" + str(item[4]) + "</font>"
           estiloneto_10_5 = "<font size=6>" + str(item[5]) + "</font>"
           estiloneto_21 = "<font size=6>" + str(item[6]) + "</font>"
           estiloneto_27 = "<font size=6>" + str(item[7]) + "</font>"
           estiloiva = "<font size=6>" + str(item[8]) + "</font>"
           estilomonotributo = "<font size=6>" + str(item[9]) + "</font>"
           estiloimpuestos_otros = "<font size=6>" + str(item[10]) + "</font>"
           estilono_grabado = "<font size=6>" + str(item[11]) + "</font>"
           estilopercepcion_ibb= "<font size=6>" + str(item[12]) + "</font>"
           estilopercepcion_iva = "<font size=6>" + str(item[13]) + "</font>"


           cabezal.append([Paragraph(estilofecha, estilo_texto),
                           Paragraph(estilonrocomprovante, estilo_texto),
                           Paragraph(estilotipo, estilo_texto),
                           Paragraph(estiloref, estilo_texto),
                           Paragraph(estilotipo, estilo_texto),
                           Paragraph(estiloneto_10_5, estilo_texto),
                           Paragraph(estiloneto_21, estilo_texto),
                           Paragraph(estiloneto_27, estilo_texto),
                           Paragraph(estiloiva, estilo_texto),
                           Paragraph(estilomonotributo, estilo_texto),
                           Paragraph(estiloimpuestos_otros, estilo_texto),
                           Paragraph(estilono_grabado, estilo_texto),
                           Paragraph(estilopercepcion_iva, estilo_texto),
                           Paragraph(estilopercepcion_ibb, estilo_texto)])


           t = Table(cabezal, (20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20))
           t.setStyle(TableStyle([
                ('INNERGRID', (0, 1), (-1, -1), 0.25, colors.black),
                ('BOX', (0, 1), (-1, -1), 0.25, colors.black),
                ('BACKGROUND', (0, 1), (-1, 1), colors.white)
            ]))
        story.append(t)

        # ---------------------------------------CAMBIAR RUTA (LA PALABRA slam2016 POR LA RUTA DESEADA DE LA PC)------------------------------------------------#
        # pyqtRemoveInputHook()
        # import pdb;pdb.set_trace()
        obj_config = configuracion()
        cadena = obj_config.ruta()

        file_path = cadena + "/pdf/reportes/libro_iva_compras" + str(datetime.date.today().year) + "_" + str(datetime.date.today().month)
        # ---EJEMPLO de windows: c:/Users/tatilu-----------------------------------------------------------------------#
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        doc = SimpleDocTemplate(file_path + "/libro_iva_compras " + self.obj_cliente.nombre + "_" + self.obj_cliente.apellido + ".pdf",
            pagesize=A4, rightMargin=14, leftMargin=14, topMargin=5, bottomMargin=18)
        doc.build(story)

        msgBox = QMessageBox()
        msgBox.setWindowTitle("Estado de Reporte")
        msgBox.setText("El reporte se ha generado correctamente")
        msgBox.exec_()

        if sys.platform == 'linux':
            subprocess.call(["xdg-open",
                             file_path + "/libro_iva_compras " + self.obj_cliente.nombre + "_" + self.obj_cliente.apellido + ".pdf"])
        else:
            os.startfile(
                file_path + "/libro_iva_compras " + self.obj_cliente.nombre + "_" + self.obj_cliente.apellido + ".pdf")

    def grilla(self):

        obj_ejercicio = ""
        for item in self.lista_ejercicio:
            if item.descripcion == self.obj_form.cbx_ejercicio.currentText():
                obj_ejercicio = item



        obj_E_ejercicio_detalle = E_ejercicio_detalle()
        self.lista_ejercicio_detalle = obj_E_ejercicio_detalle.buscar_ejercicios_id_ejercicio(obj_ejercicio.id_ejercicio)
        obj_ejercicio_detalle = ""

        for item in self.lista_ejercicio_detalle:
            if item.mes == self.obj_form.cbx_mes.currentText():
                obj_ejercicio_detalle=item

        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj_e_libro_iva_compra = E_libro_iva_compras()
        grilla = obj_e_libro_iva_compra.get_grilla_libro_iva_compras(obj_ejercicio.id_ejercicio,obj_ejercicio_detalle.id_ejercicio_detalle)

        for item in grilla:
            rowPosition = self.obj_form.tw_compras.rowCount()
            self.obj_form.tw_compras.insertRow(rowPosition)
            self.obj_form.tw_compras.setItem(rowPosition, 0, QTableWidgetItem(str(item[1])))
            self.obj_form.tw_compras.setItem(rowPosition, 1, QTableWidgetItem(str(item[2])))
            self.obj_form.tw_compras.setItem(rowPosition, 2, QTableWidgetItem(str(item[3])))
            self.obj_form.tw_compras.setItem(rowPosition, 3, QTableWidgetItem(str(item[4])))

    def nuevo(self):
        self.libro_iva_compras_nuevo = libro_iva_compras_nuevo()
        self.libro_iva_compras_nuevo.show()

    def limpar(self):
        lista_plancuenta =list()
        obj_cliente=""
        lista_asiento=""
        lista_ejercicio=""

    def agregar_asientos(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj_e_asiento = E_asiento()
        self.lista_asiento =obj_e_asiento.get_asiento_id_ejercicio()


    def buscar(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        #self.limpiar()
        if self.obj_form.lne_cuit.text() !="":
            cuit = self.obj_form.lne_cuit.text()
            obj_e_cliente= E_cliente()
            self.obj_cliente = obj_e_cliente.get_cliente_cuit_cuil(cuit)
            if self.obj_cliente == False :
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Atencion")
                msgBox.setText('No se encontro el cliente')
                msgBox.exec_()
            else:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Atencion")
                msgBox.setText('Cliente OK')
                msgBox.exec_()
                self.obj_form.lne_razon_social.setText(self.obj_cliente.razon_social)

                obj_e_ejercicio = E_ejercicio()
                self.lista_ejercicio = obj_e_ejercicio.get_ejercicio_id_cliente(self.obj_cliente.id_cliente)
                for item in self.lista_ejercicio:
                    self.obj_form.cbx_ejercicio.addItem(item.descripcion)

                #obj_e_plan_cuenta = E_plan_cuentas()
                #self.lista_plancuenta=obj_e_plan_cuenta.get_cuentas_id_cliente(self.obj_cliente.id_cliente)
                #for item in self.lista_plancuenta:
                #    self.obj_form.cbx_cuenta.addItem(item.descripcion)




        elif self.obj_form.lne_razon_social.text() !="":
            razon_social= self.obj_form.lne_razon_social.text()
            obj_e_cliente= E_proveedor()
            self.obj_cliente = obj_e_cliente.get_cliente_razon_social(razon_social)
            if self.obj_cliente == False :
                #"cliente encontrado"
                a=1
            else:
                a=2
                #ingrese el cuit nuevamente
