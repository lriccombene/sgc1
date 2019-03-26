import sys,datetime,os,subprocess
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem
from PyQt5 import uic
from form_reporte_libro_mayor import Ui_form_reporte_libro_mayor
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5.QtWidgets import QFileDialog
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle, Frame
from reportlab.platypus import Paragraph, Image
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from E_reporte import E_reporte
from E_ejercicio import E_ejercicio
from E_cliente import E_cliente
from E_configuracion import configuracion

class reporte_libro_mayor(QDialog):
    obj_form= Ui_form_reporte_libro_mayor()
    asientos=""
    lista_ejercicio_cliente =""
    lista_asiento = ""
    lista_cuentas = ""
    asiento = ""

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_reporte_libro_mayor()
        self.obj_form.setupUi(self)
        self.obj_form.btn_imprimir.clicked.connect(self.imprimir)
        self.obj_form.btn_buscar_2.clicked.connect(self.buscar)


    def buscar(self):
        #self.limpiar()
        self.obj_form.cbx_ejercicio.clear()
        if self.obj_form.lne_cuit_2.text() != "":
            # pyqtRemoveInputHook()
            # import pdb; pdb.set_trace()
            cuit = self.obj_form.lne_cuit_2.text()
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
                self.obj_form.lne_razon_social_2.setText(self.obj_cliente.razon_social)

                obj_e_ejercicio = E_ejercicio()
                self.lista_ejercicio = obj_e_ejercicio.get_ejercicio_id_cliente(self.obj_cliente.id_cliente)
                for item in self.lista_ejercicio:
                    self.obj_form.cbx_ejercicio.addItem(item.descripcion)


        elif self.obj_form.lne_razon_social_2.text() != "":
            razon_social = self.obj_form.lne_razon_social_2.text()
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
        lista_diario_gral = obj_e_reporte.reporte_libro_mayor(str(obj_ejercicio.id_ejercicio))

        styleSheet=getSampleStyleSheet()
        otro_estilo= ParagraphStyle('',fontSize =8, textColor = '#000',leftIndent = 150, rightIndent = 50)

        style_barra= ParagraphStyle('',fontSize =10,textColor = '#000',leftIndent = 0,rightIndent = 50)
        texto_principal = ParagraphStyle('',fontName='Times-Roman',fontSize =6,textColor = '#000', spaceBefore = -15,leftIndent = 195,rightIndent = 50)
        texto_principal2 = ParagraphStyle('',fontName='Times-Roman',fontSize =6,textColor = '#000', spaceBefore = -15,leftIndent = 200,rightIndent = 50)
        texto_secundario = ParagraphStyle('',fontSize =10,textColor = '#000',leftIndent = 200,rightIndent = 1)
        estilo_texto = ParagraphStyle('',
                fontSize = 7 ,
                        alignment = 0,
                        spaceBefore = 0,
                        spaceAfter = 0,
            #backColor = '#fff',
            textColor = '#000',
            leftIndent = 5 )
        estilo_cuenta = ParagraphStyle('',
                fontSize = 7 ,
                        alignment = 0,
                        spaceBefore = -15,
                        spaceAfter = -10,
            #backColor = '#fff',
            textColor = '#000',
            leftIndent = 200 )
        estilo_texto_plan_cta = ParagraphStyle('',
                fontSize = 7 ,
                        alignment = 0,
                        spaceBefore = 0,
                        spaceAfter = 0,
            backColor = '#ff9933',
            textColor = '#000',
            leftIndent = 5 )



        estilo_detalle_cuota= ParagraphStyle('',fontSize =10,textColor = '#000',leftIndent = 0,rightIndent = 0)

        options = QFileDialog.Options()
        story=[]

        título = [[Paragraph('''<b> </b>''',styleSheet["BodyText"])],
                  [Paragraph("<b><u> MAYORES:     " +str (self.obj_cliente.razon_social).upper() + "</u></b> ", texto_principal)]]
        subtítulo = [[Paragraph('''<b> </b>''',styleSheet["BodyText"])],
                   [Paragraph(' <b> (</b>'  + str(obj_ejercicio.fec_inicio) + 'AL' + str(obj_ejercicio.fec_fin) + '<b>) </b>' ,texto_principal2)]]


        t=Table(título, (550))
        t.setStyle(TableStyle([
                                    ('INNERGRID', (0,1), (-1,-1), 0.25, colors.white),
                                    ('BOX', (0,1), (-1,-1), 0.25, colors.white),
                                    ('BACKGROUND',(0,1),(-1,1),colors.white)
                                    ]))

        story.append(t)
        story.append(Spacer(0,-10))

        t=Table(subtítulo, (550))
        t.setStyle(TableStyle([
                                    ('INNERGRID', (0,1), (-1,-1), 0.25, colors.white),
                                    ('BOX', (0,1), (-1,-1), 0.25, colors.white),
                                    ('BACKGROUND',(0,1),(-1,1),colors.white)
                                    ]))

        story.append(t)
        story.append(Spacer(0,1))

        #cabezal = [[Paragraph('''<b> </b>''',styleSheet["BodyText"])],
        #           [Paragraph(' <b> FECHA </b> ',estilo_texto),
        #           Paragraph('<b> DESCRIPCIÓN </b> ',estilo_texto),
        #           Paragraph('<b> DEBE </b> ',estilo_texto),
        #           Paragraph('<b> HABER </b> ',estilo_texto),
        #           Paragraph('<b> SALDO </b> ',estilo_texto)]]


        t = ""

        asiento = ""
        saldo=0
        plan=""
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        totales = False
        totaldebe = 0
        totalhaber = 0

        for item in lista_diario_gral:

            if plan != item[7]:

                if totales:
                    estilofecha = "<font size=10>-- </font>"
                    estiloplan = "<font size=10>TOTAL </font>"
                    estilodebe = "<font size=10>"+ str(totaldebe) +"</font>"
                    estilohaber = "<font size=10>"+ str(totalhaber) +"</font>"

                    cabezal.append([Paragraph(estilofecha, estilo_texto_plan_cta),
                                    Paragraph(estiloplan, estilo_texto_plan_cta),
                                    Paragraph(estilodebe, estilo_texto_plan_cta),
                                    Paragraph(estilohaber, estilo_texto_plan_cta)])

                    t=Table(cabezal, (60,160, 90,90,100))
                    t.setStyle(TableStyle([
                                         ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                                            ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                                            ('BACKGROUND',(0,1),(-1,1),colors.white)
                                            ]))
                    story.append(t)

                título = [[Paragraph('''<b> </b>''',styleSheet["BodyText"])],
                          [Paragraph( "<b>"  + str(item[8]) + str(item[7]) + "</b>",estilo_cuenta)]]


                t=Table(título, (500))
                t.setStyle(TableStyle([
                                            ('INNERGRID', (0,1), (-1,-1), 0.25, colors.white),
                                            ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                                            ('BACKGROUND',(0,1),(-1,1),colors.white)
                                            ]))

                story.append(t)
                story.append(Spacer(0,-15))

                cabezal = [[Paragraph('''<b> </b>''',styleSheet["BodyText"])],
                   [Paragraph(' <b> FECHA </b> ',estilo_texto),
                   Paragraph('<b> DESCRIPCIÓN </b> ',estilo_texto),
                   Paragraph('<b> DEBE </b> ',estilo_texto),
                   Paragraph('<b> HABER </b> ',estilo_texto),
                   Paragraph('<b> SALDO </b> ',estilo_texto)]]

                totaldebe = 0
                totalhaber = 0
                plan = item[7]

                #estilofecha = "<font size=10>" + str(item[8]) +"</font>"
                #estiloplan = "<font size=10>" + str(item[7])+ " </font>"
                #estilodebe = "<font size=10>-</font>"
                #estilohaber = "<font size=10>-</font>"


                #cabezal.append([Paragraph(estilofecha, estilo_texto_plan_cta),
                #                Paragraph(estiloplan, estilo_texto_plan_cta),
                #                Paragraph(estilodebe, estilo_texto_plan_cta),
                #                Paragraph(estilohaber, estilo_texto_plan_cta)])
                saldo=0

                estilofecha2 = " <font size=6>" + str(item[4]) +"</font>"
                estilodescripcion2 = " <font size=6>" + str(item[3])  + " </font>"
                estilodebe2 = " <font size=6> "+ str(round(item[5],2))  +" </font>"
                estilohaber2 = " <font size=6> "+ str(round(item[6],2))  +" </font>"
                #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                saldo = float(saldo) -float(item[6]) +float(item[5])
                estilosaldo2 = " <font size=6> "+ str(saldo)  +" </font>"


                cabezal.append([Paragraph(estilofecha2, estilo_texto),
                                Paragraph(estilodescripcion2, estilo_texto),
                                Paragraph(estilodebe2, estilo_texto),
                                Paragraph(estilohaber2, estilo_texto),
                                Paragraph(estilosaldo2, estilo_texto)])
                totales=True
                totaldebe = round(totaldebe + float(item[5]),2)
                totalhaber = round(totalhaber + float(item[6]),2)




            else:
                estilofecha2 = " <font size=6>" + str(item[4]) +"</font>"
                estilodescripcion2 = " <font size=6>" + str(item[3])  + " </font>"
                estilodebe2 = " <font size=6> "+ str(round(item[5],2))  +" </font>"
                estilohaber2 = " <font size=6> "+ str(round(item[6],2))  +" </font>"
                #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                saldo = round(float(saldo) -float(item[6]) +float(item[5]),2)
                estilosaldo2 = " <font size=6> "+ str(saldo)  +" </font>"


                cabezal.append([Paragraph(estilofecha2, estilo_texto),
                                Paragraph(estilodescripcion2, estilo_texto),
                                Paragraph(estilodebe2, estilo_texto),
                                Paragraph(estilohaber2, estilo_texto),
                                Paragraph(estilosaldo2, estilo_texto)])

                totaldebe = round(totaldebe + float(item[5]),2)
                totalhaber = round(totalhaber + float(item[6]),2)



        estilofecha = "<font size=10>-- </font>"
        estiloplan = "<font size=10>TOTAL </font>"
        estilodebe = "<font size=10>"+ str(round(totaldebe,2)) +"</font>"
        estilohaber = "<font size=10>"+ str(round(totalhaber,2)) +"</font>"
        cabezal.append([Paragraph(estilofecha, estilo_texto_plan_cta),
                                    Paragraph(estiloplan, estilo_texto_plan_cta),
                                    Paragraph(estilodebe, estilo_texto_plan_cta),
                                    Paragraph(estilohaber, estilo_texto_plan_cta)])


        t=Table(cabezal, (100,100, 100,100,100))
        t.setStyle(TableStyle([
                                         ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                                            ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                                            ('BACKGROUND',(0,1),(-1,1),colors.white)
                                            ]))
        story.append(t)


  #---------------------------------------CAMBIAR RUTA (LA PALABRA slam2016 POR LA RUTA DESEADA DE LA PC)------------------------------------------------#
        #pyqtRemoveInputHook()
        #import pdb;pdb.set_trace()
        obj_config = configuracion()
        cadena = obj_config.ruta()

        file_path = cadena  + "/pdf/reportes/libro_mayor"+str(datetime.date.today().year)+"_"+str(datetime.date.today().month)
        #---EJEMPLO de windows: c:/Users/tatilu-----------------------------------------------------------------------#
        if not os.path.exists(file_path):
               os.makedirs(file_path)

        doc=SimpleDocTemplate(file_path +"/libro_mayor "+  self.obj_cliente.nombre +"_"+self.obj_cliente.apellido+".pdf", pagesize=A4, rightMargin=14,leftMargin=14, topMargin=5,bottomMargin=18)
        doc.build(story )

        msgBox = QMessageBox()
        msgBox.setWindowTitle("Estado de Reporte")
        msgBox.setText("El reporte se ha generado correctamente" )
        msgBox.exec_()

        if sys.platform == 'linux':
            subprocess.call(["xdg-open", file_path +"/libro_mayor "+  self.obj_cliente.nombre +"_"+self.obj_cliente.apellido+".pdf"])
        else:
            os.startfile( file_path +"/libro_mayor "+  self.obj_cliente.nombre +"_"+self.obj_cliente.apellido+".pdf")
