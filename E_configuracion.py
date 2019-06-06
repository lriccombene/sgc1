class configuracion(object):
    def config(self):
        cadena = 'postgresql://postgres:@localhost:5432/sgcinflacion'

        return cadena

    #lugar donde se descargan archivos local
    def ruta(self):
        
        cadena="/home/slam2016/Documentos/slam/SGC_Vsoft/testInflacion"
        return cadena
    #lugar de donde se obtienen los archivos del servidor
    def ruta_server(self):
        #cadena ="/home/soporte/Documentos/facultad/credired20180108"
        cadena ="/home/user/Documentos/sgc/sgc20180210"

        return cadena

    def host_server(self):
        cadena ='localhost'
        return cadena

    def usu_server(self):
        cadena ='user'
        return cadena

    def pass_server(self):
        cadena ='slam2016'
        return cadena
