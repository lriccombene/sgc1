import sys,datetime,os,subprocess
from decimal import Decimal
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
from E_reporte import E_reporte
from form_reporte_sumas_y_saldos import Ui_form_reporte_sumas_y_saldos
from E_ejercicio import E_ejercicio
from E_cliente import E_cliente
from E_configuracion import configuracion

class reporte_sumas_y_saldos(QDialog):
    obj_form= Ui_form_reporte_sumas_y_saldos()
    lista_ejercicio_cliente =""
    lista_asiento = ""
    lista_cuentas = ""
    asiento = ""
    obj_cliente=""

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_reporte_sumas_y_saldos()
        self.obj_form.setupUi(self)
        self.obj_form.btn_imprimir.clicked.connect(self.imprimir)
        self.obj_form.btn_buscar_2.clicked.connect(self.buscar)


    def imprimir(self):
        obj_ejercicio = ""
        for item in self.lista_ejercicio:
            if item.descripcion == self.obj_form.cbx_ejercicio_2.currentText():
                obj_ejercicio = item

        obj_e_reporte = E_reporte()

        lista_SUMAS_SALDOS = obj_e_reporte.reporte_sumas_saldos(str(obj_ejercicio.id_ejercicio))

        styleSheet = getSampleStyleSheet()
        otro_estilo = ParagraphStyle('', fontName='Times-Roman',fontSize=6, textColor='#000', leftIndent=230, rightIndent=50)
        otro_estilo2 = ParagraphStyle('', fontName='Times-Roman',fontSize=6, textColor='#000', leftIndent=230, rightIndent=50)
        style_barra = ParagraphStyle('', fontSize=10, textColor='#000', leftIndent=0, rightIndent=50)
        texto_principal = ""
        texto_secundario = ParagraphStyle('', fontSize=6, textColor='#000', leftIndent=5, rightIndent=0)
        texto_secundario2 = ParagraphStyle('', fontSize=6, textColor='#150', leftIndent=5, rightIndent=0)
        texto_secundario3 = ParagraphStyle('', fontSize=6, textColor='#FF0000', leftIndent=5, rightIndent=0)
        estilo_resultado = ParagraphStyle('', fontName='Times-Roman', fontSize=6, textColor='#000', leftIndent=1, rightIndent=50)
        estilo_resultado2 = ParagraphStyle('', fontSize=6, textColor='#000', leftIndent=1, rightIndent=0)
        estilo_texto = ParagraphStyle('',
                                      fontSize=6,
                                      alignment=0,
                                      spaceBefore=0,
                                      spaceAfter=0,
                                      #backgroundColor = '#A9D0F5',
                                      textColor='#000',
                                      leftIndent=5)
        estilo_detalle_cuota = ParagraphStyle('', fontSize=10, textColor='#000', leftIndent=0, rightIndent=0)

        options = QFileDialog.Options()
        story = []

        P = Paragraph("<b><u> SUMAS Y SALDOS</u></b> ", otro_estilo)
        story.append(P)
        story.append(Spacer(0, 2))
        P = Paragraph("<b><u>" + str( self.obj_cliente.razon_social).upper() + "</u></b> ", otro_estilo2)
        story.append(P)
        story.append(Spacer(0, -5))

        cabezal = [[Paragraph('''<b> </b>''', styleSheet["BodyText"])],
                   [Paragraph(' <b> CODIGO </b> ', estilo_texto),
                    Paragraph('<b> DESCRIPCIÓN </b> ', estilo_texto),
                    Paragraph('<b> DEBE </b> ', estilo_texto),
                    Paragraph('<b> HABER </b> ', estilo_texto),
                    Paragraph('<b> SALDO </b> ', estilo_texto),
                    Paragraph('<b> S.ACREEDOR </b> ', estilo_texto),
                    Paragraph('<b> S.DEUDOR</b> ', estilo_texto)]]

        t = ""
        asiento = ""
        saldo = 0
        plan = ""

        total_resultado = 0.0
        total_saldo_deudor = 0.0
        total_saldo_acreedor = 0.0

        centena_padre=0
        total_decenamil_padre=0
        obj_centena_padre=""
        bandera_centena=True
        obj_centena_padre_Anterior=""
        mil_padre = 0
        bandera_mil = True
        obj_mil_padre_Anterior=""
        diezmil_padre = 0
        bandera_diezmil = True
        obj_diezmil_padre_Anterior=""


        #pyqtRemoveInputHook()
        #import pdb;pdb.set_trace()


        for item in lista_SUMAS_SALDOS:
            centena_padre =  obj_e_reporte.get_padre_centena(str(item[0]),self.obj_cliente.id_cliente)
            for item2 in centena_padre:

                mil_padre = obj_e_reporte.get_padre_mil(str(item2[1]),self.obj_cliente.id_cliente)

                for item3 in mil_padre:
                    #pyqtRemoveInputHook()
                    #import pdb;pdb.set_trace()
                    diezmil_padre = obj_e_reporte.get_padre_diezmil(str(item3[1]),self.obj_cliente.id_cliente)
                    for item4 in  diezmil_padre:

                        if bandera_diezmil== True:
                            total_diezmil_padre =obj_e_reporte.calcular_diezmil_padre(str(item2[1]),self.obj_cliente.id_cliente)
                            resultado=""
                            for result in total_diezmil_padre:
                                resultado = result


                            bandera_diezmil=False
                            
                            total_resultado =Decimal(resultado[0])-Decimal(resultado[1])
                            estiloCodigo4 = "<font size=6>" + str(item4[1]) + "</font>"
                            estiloDescripcion4 = "<font size=6>" + str(item4[2]) + " </font>"
                            estilodebe4 =  "<font size=6>" + str(round(resultado[0],2)) + " </font>"
                            estilohaber4 =  "<font size=6>" + str(round(resultado[1],2)) + " </font>"
                            estilosaldo4 = "<font size=6>" + str(round(total_resultado,2)) + " </font>"
                            estilosdeudor4="<font size=6>" + str("-") + " </font>"
                            estilosacredoor4="<font size=6>" + str("-") + " </font>"

                            cabezal.append([Paragraph(estiloCodigo4, texto_secundario3),
                                            Paragraph(estiloDescripcion4, texto_secundario3),
                                            Paragraph(estilodebe4, texto_secundario3),
                                            Paragraph(estilohaber4, texto_secundario3),
                                            Paragraph(estilosaldo4, texto_secundario3),
                                            Paragraph(estilosdeudor4, texto_secundario3),
                                            Paragraph(estilosacredoor4, texto_secundario3)])

                        elif obj_diezmil_padre_Anterior[2] != item4[2]:
                            total_diezmil_padre =obj_e_reporte.calcular_diezmil_padre(str(item2[1]),self.obj_cliente.id_cliente)
                            resultado=""
                            for result in total_diezmil_padre:
                                resultado = result
                            try:
                                total_resultado =Decimal(resultado[0])-Decimal(resultado[1])
                            except:
                            	total_resultado =0
                            deberesult=0
                            try:
                                deberesult=round(resultado[0],2)
                            except:
                                deberesult=0
                            haberresult=0  
                            try:
                                haberresult=round(resultado[1],2)
                            except:
                                haberresult=0  
                           
                            estiloCodigo4 = "<font size=6>" + str(item4[1]) + "</font>"
                            estiloDescripcion4 = "<font size=6>" + str(item4[2]) + " </font>"
                            estilodebe4 =  "<font size=6>" + str(deberesult) + " </font>"
                            estilohaber4 =  "<font size=6>" + str(haberresult) + " </font>"
                            estilosaldo4 = "<font size=6>" + str(round(total_resultado,2)) + " </font>"
                            estilosdeudor4="<font size=6>" + str("-") + " </font>"
                            estilosacredoor4="<font size=6>" + str("-") + " </font>"

                            cabezal.append([Paragraph(estiloCodigo4, texto_secundario3),
                                            Paragraph(estiloDescripcion4, texto_secundario3),
                                            Paragraph(estilodebe4, texto_secundario3),
                                            Paragraph(estilohaber4, texto_secundario3),
                                            Paragraph(estilosaldo4, texto_secundario3),
                                            Paragraph(estilosdeudor4, texto_secundario3),
                                            Paragraph(estilosacredoor4, texto_secundario3)])
                        obj_diezmil_padre_Anterior=item4



                    if bandera_mil== True:
                        total_mil_padre =obj_e_reporte.calcular_mil_padre(str(item2[1]),self.obj_cliente.id_cliente)
                        resultado=""
                        for result in total_mil_padre:
                            resultado = result

                        bandera_mil=False
                        total_resultado =float(resultado[0])-float (resultado[1])
                        estiloCodigo3 = "<font size=6>" + str(item3[1]) + "</font>"
                        estiloDescripcion3 = "<font size=6>" + str(item3[2]) + " </font>"
                        estilodebe3 =  "<font size=6>" + str(round(resultado[0],2)) + " </font>"
                        estilohaber3 =  "<font size=6>" + str(round(resultado[1],2)) + " </font>"
                        estilosaldo3 = "<font size=6>" + str(round(total_resultado,2)) + " </font>"
                        estilosdeudor3="<font size=6>" + str("-") + " </font>"
                        estilosacredoor3="<font size=6>" + str("-") + " </font>"

                        cabezal.append([Paragraph(estiloCodigo3, texto_secundario3),
                                        Paragraph(estiloDescripcion3, texto_secundario3),
                                        Paragraph(estilodebe3, texto_secundario3),
                                        Paragraph(estilohaber3, texto_secundario3),
                                        Paragraph(estilosaldo3, texto_secundario3),
                                        Paragraph(estilosdeudor3, texto_secundario3),
                                        Paragraph(estilosacredoor3, texto_secundario3)])

                    elif obj_mil_padre_Anterior[2] != item3[2]:
                        total_mil_padre =obj_e_reporte.calcular_mil_padre(str(item2[1]),self.obj_cliente.id_cliente)
                        resultado=""
                        for result in total_mil_padre:
                            resultado = result
                        try:
                            total_resultado =float(resultado[0])-float (resultado[1])
                        except:
                            total_resultado=0

                                            #total_resultado =(resultado[0])-float (resultado[1])
                        deberesult=0
                        try:
                            deberesult=round(resultado[0],2)
                        except:
                            deberesult=0
                        haberresult=0  
                        try:
                            haberresult=round(resultado[1],2)
                        except:
                            haberresult=0  

                        
                        estiloCodigo3 = "<font size=6>" + str(item3[1]) + "</font>"
                        estiloDescripcion3 = "<font size=6>" + str(item3[2]) + " </font>"
                        estilodebe3 =  "<font size=6>" + str(deberesult) + " </font>"
                        estilohaber3 =  "<font size=6>" + str(haberresult) + " </font>"
                        estilosaldo3 = "<font size=6>" + str(round(total_resultado,2)) + " </font>"
                        estilosdeudor3="<font size=6>" + str("-") + " </font>"
                        estilosacredoor3="<font size=6>" + str("-") + " </font>"

                        cabezal.append([Paragraph(estiloCodigo3, texto_secundario3),
                                        Paragraph(estiloDescripcion3, texto_secundario3),
                                        Paragraph(estilodebe3, texto_secundario3),
                                        Paragraph(estilohaber3, texto_secundario3),
                                        Paragraph(estilosaldo3, texto_secundario3),
                                        Paragraph(estilosdeudor3, texto_secundario3),
                                        Paragraph(estilosacredoor3, texto_secundario3)])
                    obj_mil_padre_Anterior=item3

                if bandera_centena== True:
                    total_centena_padre =obj_e_reporte.calcular_centena_padre(str(item2[1]),self.obj_cliente.id_cliente)
                    resultado=""
                    for result in total_centena_padre:
                        resultado = result


                    bandera_centena=False
                    
                    try:
                        total_resultado =float(resultado[0])-float (resultado[1])
                    except:
                        total_resultado=0
                    #total_resultado =(resultado[0])-float (resultado[1])
                    deberesult=0
                    try:
                        deberesult=round(resultado[0],2)
                    except:
                        deberesult=0
                    haberresult=0  
                    try:
                        haberresult=round(resultado[1],2)
                    
                    except:
                        haberresult=0  


                    estiloCodigo = "<font size=6>" + str(item2[1]) + "</font>"
                    estiloDescripcion = "<font size=6>" + str(item2[2]) + " </font>"
                    estilodebe =  "<font size=6>" + str(deberesult) + " </font>"
                    estilohaber =  "<font size=6>" + str(haberresult) + " </font>"
                    estilosaldo = "<font size=6>" + str(round(total_resultado,2)) + " </font>"
                    estilosdeudor="<font size=6>" + str("-") + " </font>"
                    estilosacredoor="<font size=6>" + str("-") + " </font>"

                    cabezal.append([Paragraph(estiloCodigo, texto_secundario2),
                                    Paragraph(estiloDescripcion, texto_secundario2),
                                    Paragraph(estilodebe, texto_secundario2),
                                    Paragraph(estilohaber, texto_secundario2),
                                    Paragraph(estilosaldo, texto_secundario2),
                                    Paragraph(estilosdeudor, texto_secundario2),
                                    Paragraph(estilosacredoor, texto_secundario2)])
                elif obj_centena_padre_Anterior[2] != item2[2]:
                    total_centena_padre =obj_e_reporte.calcular_centena_padre(str(item2[1]),self.obj_cliente.id_cliente)
                    resultado=""
                    for result in total_centena_padre:
                        resultado = result

                    #total_resultado =(resultado[0])-float (resultado[1])
                    try:
                        total_resultado =float(resultado[0])-float (resultado[1])
                    except:
                        total_resultado=0

                    deberesult=0
                    try:
                            deberesult=round(resultado[0],2)
                    except:
                            deberesult=0
                    haberresult=0  
                    try:
                            haberresult=round(resultado[1],2)
                    except:
                            haberresult=0 
                        
                    estiloCodigo = "<font size=6>" + str(item2[1]) + "</font>"
                    estiloDescripcion = "<font size=6>" + str(item2[2]) + " </font>"
                    estilodebe =  "<font size=6>" + str(deberesult) + " </font>"
                    estilohaber =  "<font size=6>" + str(haberresult) + " </font>"
                    estilosaldo = "<font size=6>" + str(round(total_resultado,2)) + " </font>"
                    estilosdeudor="<font size=6>" + str("-") + " </font>"
                    estilosacredoor="<font size=6>" + str("-") + " </font>"

                    cabezal.append([Paragraph(estiloCodigo, texto_secundario2),
                                    Paragraph(estiloDescripcion, texto_secundario2),
                                    Paragraph(estilodebe, texto_secundario2),
                                    Paragraph(estilohaber, texto_secundario2),
                                    Paragraph(estilosaldo, texto_secundario2),
                                    Paragraph(estilosdeudor, texto_secundario2),
                                    Paragraph(estilosacredoor, texto_secundario2)])

                obj_centena_padre_Anterior=item2


            if plan != item[1]:
                plan = item[1]
                total_resultado = total_resultado  + float(item[4])
                estiloCodigo = "<font size=6>" + str(item[0]) + "</font>"
                estiloDescripcion = "<font size=6>" + str(item[1]) + " </font>"
                estilodebe =  "<font size=6>" + str(round(item[2],2)) + " </font>"
                estilohaber =  "<font size=6>" + str(round(item[3],2)) + " </font>"
                estilosaldo = "<font size=6>" + str(round(item[4],2)) + " </font>"

                if float(item[4]) < 0:
                    total_saldo_deudor = total_saldo_deudor+ float(item[4])
                    estilosdeudor = estilosaldo
                    estilosacredoor = "<font size=6>----</font>"
                else:
                    estilosdeudor ="<font size=6>----</font>"
                    estilosacredoor = estilosaldo
                    total_saldo_acreedor = total_saldo_acreedor + float(item[4])


                cabezal.append([Paragraph(estiloCodigo, texto_secundario),
                                Paragraph(estiloDescripcion, texto_secundario),
                                Paragraph(estilodebe, texto_secundario),
                                Paragraph(estilohaber, texto_secundario),
                                Paragraph(estilosaldo, texto_secundario),
                                Paragraph(estilosdeudor, texto_secundario),
                                Paragraph(estilosacredoor, texto_secundario)])

            t = Table(cabezal, (50, 200, 60, 60, 60, 60,60))
            t.setStyle(TableStyle([
                ('INNERGRID', (0, 1), (-1, -1), 0.25, colors.black),
                ('BOX', (0, 1), (-1, -1), 0.25, colors.black),
                ('BACKGROUND', (0, 1), (-1, 1), colors.white)
            ]))
        story.append(t)

        resultado = [[Paragraph('''<b> </b>''', styleSheet["BodyText"])],
                     [Paragraph(' <b> RESULTADO DEL EJERCICIO : </b> ', estilo_resultado),
                      Paragraph('<b> </b> '""+ str(round(total_resultado,2)), estilo_resultado2),
                      Paragraph('<b> </b> '""+ str(round(total_saldo_deudor,2)), estilo_resultado2),
                      Paragraph('<b> </b> '""+ str(round(total_saldo_acreedor,2)), estilo_resultado2)]]


        #resultado.append([Paragraph("RESULTADO DEL EJERCICIO : "+str(total_resultado), estilo_resultado),
        #                        Paragraph(""+ str(total_saldo_deudor), estilo_resultado),
        #                        Paragraph(""+ str(total_saldo_acreedor), estilo_resultado)])

        t = Table(resultado, (370, 60, 60, 60))
        t.setStyle(TableStyle([
                ('INNERGRID', (0, 1), (-1, -1), 0.25, colors.black),
                ('BOX', (0, 1), (-1, -1), 0.25, colors.black),
                ('BACKGROUND', (0, 1), (-1, 1), colors.white)
            ]))
        story.append(t)

        #P = Paragraph("RESULTADO DEL EJERCICIO : "+str(total_resultado), estilo_resultado)
        #story.append(P)
        #story.append(Spacer(0, 2))

        #P = Paragraph("RESULTADO SALDO DEUDOR : "+str(total_saldo_deudor), estilo_resultado)
        #story.append(P)
        #story.append(Spacer(0, 2))

        #P = Paragraph("RESULTADO SALDO ACREEDOR : "+str(total_saldo_acreedor), estilo_resultado)
        #story.append(P)
        #story.append(Spacer(0, 2))

        # ---------------------------------------CAMBIAR RUTA (LA PALABRA slam2016 POR LA RUTA DESEADA DE LA PC)------------------------------------------------#
        # pyqtRemoveInputHook()
        # import pdb;pdb.set_trace()
        obj_config = configuracion()
        cadena = obj_config.ruta()

        file_path = cadena + "/pdf/reportes/libro_suma_saldos" + str(datetime.date.today().year) + "_" + str(
            datetime.date.today().month)
        # ---EJEMPLO de windows: c:/Users/tatilu-----------------------------------------------------------------------#
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        doc = SimpleDocTemplate(
            file_path + "/libro_suma_saldos " + self.obj_cliente.nombre + "_" + self.obj_cliente.apellido + ".pdf",
            pagesize=A4, rightMargin=14, leftMargin=14, topMargin=5, bottomMargin=18)

        doc.build(story)

        msgBox = QMessageBox()
        msgBox.setWindowTitle("Estado de Reporte")
        msgBox.setText("El reporte se ha generado correctamente")
        msgBox.exec_()

        if sys.platform == 'linux':
            subprocess.call(["xdg-open",
                             file_path + "/libro_suma_saldos " + self.obj_cliente.nombre + "_" + self.obj_cliente.apellido + ".pdf"])
        else:
            os.startfile(
                file_path + "/libro_suma_saldos " + self.obj_cliente.nombre + "_" + self.obj_cliente.apellido + ".pdf")

    def buscar(self):
        # self.limpiar()
        self.obj_form.cbx_ejercicio_2.clear()
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
                    self.obj_form.cbx_ejercicio_2.addItem(item.descripcion)


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


