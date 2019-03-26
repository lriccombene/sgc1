import sys,datetime, os
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5.QtWidgets import QFileDialog
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle, Frame
from reportlab.platypus import Paragraph, Image
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from form_reporte_diario_gral import Ui_form_reporte_diario_gral
from E_reporte import E_reporte
from E_cliente import E_cliente
from E_ejercicio import E_ejercicio
import subprocess
from E_configuracion import configuracion

class reporte_diario_general(QDialog):
    obj_form= Ui_form_reporte_diario_gral()
    obj_cliente = ""
    lista_ejercicio = ""

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_reporte_diario_gral()
        self.obj_form.setupUi(self)
        self.obj_form.btn_buscar.clicked.connect(self.buscar)
        self.obj_form.btn_imprimir.clicked.connect(self.imprimir)


    def buscar(self):
        #self.limpiar()
        self.obj_form.cbx_ejercicio.clear()
        if self.obj_form.lne_cuit.text() != "":
            # pyqtRemoveInputHook()
            # import pdb; pdb.set_trace()
            cuit = self.obj_form.lne_cuit.text()
            obj_e_cliente = E_cliente()
            self.obj_cliente = obj_e_cliente.get_cliente_cuit_cuil(cuit)
            if self.obj_cliente == False:
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


        elif self.obj_form.lne_razon_social.text() != "":
            razon_social = self.obj_form.lne_razon_social.text()
            # obj_e_cliente= E_proveedor()
            # self.obj_cliente = obj_e_cliente.get_cliente_razon_social(razon_social)
            # if self.obj_cliente == False :
            # "cliente encontrado"
            #    a=1
            # else:
            #    a=2
            # ingrese el cuit nuevamente




    def imprimir(self):

        obj_ejercicio = ""
        for item in self.lista_ejercicio:
                if item.descripcion == self.obj_form.cbx_ejercicio.currentText():
                    obj_ejercicio=item

        obj_e_reporte = E_reporte()
        lista_diario_gral = obj_e_reporte.reporte_diario_general(str(obj_ejercicio.id_ejercicio))

        styleSheet=getSampleStyleSheet()
        otro_estilo= ParagraphStyle('',fontSize =8, textColor = '#000',leftIndent = 150, rightIndent = 50)
        style_barra= ParagraphStyle('',fontSize =10,textColor = '#000',leftIndent = 0,rightIndent = 50)
        texto_principal = ""
        texto_secundario = ParagraphStyle('',fontSize =10,textColor = '#000',leftIndent = 200,rightIndent = 1)
        estilo_texto = ParagraphStyle('',
                fontSize = 7 ,
                        alignment = 0,
                        spaceBefore = 0,
                        spaceAfter = 0,
            textColor = '#000',
            leftIndent = 15 )

        estilo_texto2 = ParagraphStyle('',
            fontSize = 9 ,
            alignment = 0,
            spaceBefore = -1,
            spaceAfter = -1,
            #backColor = '#819FF7',
            textColor = '#000',
            leftIndent = 5 )

        estilo_detalle_cuota= ParagraphStyle('',fontSize =10,textColor = '#000',leftIndent = 0,rightIndent = 0)

        options = QFileDialog.Options()
        story=[]

        P = Paragraph('<b> EJERCICIO N° </b>' + str( obj_ejercicio.descripcion).upper() + " DESDE " + str( obj_ejercicio.fec_inicio) + " al " + str( obj_ejercicio.fec_fin), otro_estilo)
        story.append(P)
        story.append(Spacer(0,-5))

        cabezal = [[Paragraph('''<b> </b>''',styleSheet["BodyText"])],
                    [Paragraph(' <b> FECHA </b> ',estilo_texto),
                     Paragraph('<b> NRO </b> ',estilo_texto),
                    Paragraph('<b> DESCRIPCIÓN </b> ',estilo_texto),
                    Paragraph('<b> DEBE </b> ',estilo_texto),
                    Paragraph('<b> HABER </b> ',estilo_texto)]]

        t = ""

        asiento = ""
        nro=1
        for item in lista_diario_gral:
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()

            if asiento != item[1]:
                fecha = item[0]
                asiento = item[1]

                estilofecha = "<b><font size=6>" + str(item[0]).upper() +"</font></b>"
                estilonro = " <font size=6>" + str(nro) +"</font>"
                estilodescripcion = "<b><font size=6>" + str(item[1]).upper()+ " </font></b>"
                estilodebe = "<font size=6>-</font>"
                estilohaber = "<font size=6>-</font>"

                cabezal.append([Paragraph(estilofecha, estilo_texto2),
                                Paragraph(estilonro, estilo_texto),
                                Paragraph(estilodescripcion, estilo_texto2),
                                Paragraph(estilodebe, estilo_texto2),
                                Paragraph(estilohaber, estilo_texto2)])

                t=Table(cabezal, (60,30,270, 75,75))
                t.setStyle(TableStyle([
                                         ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                                            ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                                            ('BACKGROUND',(0,1),(-1,1),colors.white)
                                            ]))
                #story.append(t)
                nro= nro+1
                estilocodigo = " <font size=6>" + str(item[3]) +"</font>"
                estilonro = " <font size=6>" + "-" +"</font>"
                estilodescripcion = " <font size=6>" + str(item[2])  + " </font>"
                estilodebe = " <font size=6> "+ str(item[4])  +" </font>"
                estilohaber = " <font size=6> "+ str(item[5])  +" </font>"

                cabezal.append([Paragraph(estilocodigo, estilo_texto),
                                Paragraph(estilonro, estilo_texto),
                                Paragraph(estilodescripcion, estilo_texto),
                                Paragraph(estilodebe, estilo_texto),
                                Paragraph(estilohaber, estilo_texto)])


                t=Table(cabezal, (60,30,270, 75,75))
                t.setStyle(TableStyle([
                                         ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                                            ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                                            ('BACKGROUND',(0,1),(-1,1),colors.white)
                                            ]))


            else:
    
                estilocodigo = " <font size=6>" + str(item[3]) +"</font>"
                estilonro = " <font size=6>" + "-" +"</font>"
                estilodescripcion = " <font size=6>" + str(item[2])  + " </font>"
                estilodebe = " <font size=6> "+ str(item[4])  +" </font>"
                estilohaber = " <font size=6> "+ str(item[5])  +" </font>"

                cabezal.append([Paragraph(estilocodigo, estilo_texto),
                                Paragraph(estilonro, estilo_texto),
                                Paragraph(estilodescripcion, estilo_texto),
                                Paragraph(estilodebe, estilo_texto),
                                Paragraph(estilohaber, estilo_texto)])


                t=Table(cabezal, (60,30,270, 75,75))
                t.setStyle(TableStyle([
                                         ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                                            ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                                            ('BACKGROUND',(0,1),(-1,1),colors.white)
                                            ]))
        story.append(t)

        P = Paragraph('<b> RESULTADO </b>' " DEBE " " HABER" , otro_estilo)
        story.append(P)
        story.append(Spacer(0,-5))

  #---------------------------------------CAMBIAR RUTA (LA PALABRA slam2016 POR LA RUTA DESEADA DE LA PC)------------------------------------------------#
        #pyqtRemoveInputHook()
        #import pdb;pdb.set_trace()
        obj_config = configuracion()
        cadena = obj_config.ruta()

        file_path = cadena  + "/pdf/reportes/diario_general"+str(datetime.date.today().year)+"_"+str(datetime.date.today().month)
        #---EJEMPLO de windows: c:/Users/tatilu-----------------------------------------------------------------------#
        if not os.path.exists(file_path):
               os.makedirs(file_path)

        doc=SimpleDocTemplate(file_path +"/diario_general "+  self.obj_cliente.nombre +"_"+self.obj_cliente.apellido+".pdf", pagesize=A4, rightMargin=14,leftMargin=14, topMargin=5,bottomMargin=18)
        doc.build(story )

        msgBox = QMessageBox()
        msgBox.setWindowTitle("Estado de Reporte")
        msgBox.setText("El reporte se ha generado correctamente" )
        msgBox.exec_()

        if sys.platform == 'linux':
            subprocess.call(["xdg-open", file_path +"/diario_general "+  self.obj_cliente.nombre +"_"+self.obj_cliente.apellido+".pdf"])
        else:
            os.startfile( file_path +"/diario_general "+  self.obj_cliente.nombre +"_"+self.obj_cliente.apellido+".pdf")
