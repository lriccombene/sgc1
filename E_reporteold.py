import sys,datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric, update,text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion



base = declarative_base()
class E_reporte(base):
    __tablename__="libro_iva_ventas"
    id_libro_iva_ventas = Column(Integer, primary_key=True, autoincrement=True)

    session = ""

    def __init__(self):
        obj_conexion = configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session = Session()

    def reporte_diario_general(self, id_ejercicio):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        sql = text('select  a.fecha, a.descripcion asiento, '+
                   ' (select descripcion from plan_cuentas' +
                   ' where id_cuenta=c.id_plan_cuentas) descripcion ,' +
                   '(select codigo from plan_cuentas where id_cuenta=c.id_plan_cuentas) codigo, '+
                   ' c.debe,c.haber' +
                   ' from asiento a ' +
                   ' inner join ejercicio e  on  a.id_ejercicio = e.id_ejercicio ' +
                   ' inner join cuentas c on a.id_asiento = c.id_asiento ' +
                   ' where e.id_ejercicio =' + id_ejercicio + '  order by a.fecha' )

        result = self.session.execute(sql)
        try:
            return result
        except :
            self.session.close()
            return False


    def reporte_libro_mayor(self, id_ejercicio):
        sql = text('select e.descripcion, e.fec_inicio, e.fec_fin,' +
                  'a.descripcion,a.fecha, c.debe, c.haber,' +
                  '(select descripcion from plan_cuentas where id_cuenta= c.id_plan_cuentas) plan , ' +
                  '(select codigo from plan_cuentas where id_cuenta= c.id_plan_cuentas) codigo ' +
                  'from ejercicio e ' +
                  'inner join asiento a on e.id_ejercicio = a.id_ejercicio ' +
                  'inner join cuentas c on a.id_asiento = c.id_asiento ' +
                  'where e.id_ejercicio =' + id_ejercicio + ' order by plan ,a.fecha' )

        result = self.session.execute(sql)
        try:
            return result
        except :
            self.session.close()
            return False

   
    def reporte_sumas_saldos(self, id_ejercicio):
        sql = text('select p.codigo, p.descripcion, ' +
                    'SUM(c.debe), SUM(c.haber), ' +
                    '(SUM(c.debe)-SUM(c.haber)) saldo ' +
                    'from ejercicio e  ' +
                    'inner join asiento a on e.id_ejercicio = a.id_ejercicio ' +
                    'inner join cuentas c on a.id_asiento = c.id_asiento ' +
                    'inner join plan_cuentas p on c.id_plan_cuentas = p.id_cuenta ' +
                    'where e.id_ejercicio =' + id_ejercicio + ' GROUP BY codigo, p.descripcion order by p.codigo; ' )

        result = self.session.execute(sql)
        try:
            return result
        except :
            self.session.close()
            return False

    def get_padre_centena(self,codigo,id_cliente):

        centena_padre = codigo[:3]
        centena_padre =centena_padre+'00'
        centena_padre ="'"+ centena_padre+"'"
        #pyqtRemoveInputHook()
        #import pdb;pdb.set_trace()
        sql = text('select * from  plan_cuentas' +
                    ' where id_cliente =' + str(id_cliente) +' and codigo='+ centena_padre )

        result = self.session.execute(sql)
        try:
            return result

        except :
            self.session.close()
            return False

    def get_padre_mil(self,codigo,id_cliente):

        centena_padre = codigo[:2]
        centena_padre =centena_padre+'000'
        centena_padre ="'"+ centena_padre+"'"
        #pyqtRemoveInputHook()
        #import pdb;pdb.set_trace()
        sql = text('select * from  plan_cuentas' +
                    ' where id_cliente =' + str(id_cliente) +' and codigo='+ centena_padre )

        result = self.session.execute(sql)
        try:
            return result

        except :
            self.session.close()
            return False

    def get_padre_diezmil(self,codigo,id_cliente):

        centena_padre = codigo[:1]
        centena_padre =centena_padre+'0000'
        centena_padre ="'"+ centena_padre+"'"
        #pyqtRemoveInputHook()
        #import pdb;pdb.set_trace()
        sql = text('select * from  plan_cuentas' +
                    ' where id_cliente =' + str(id_cliente) +' and codigo='+ centena_padre )

        result = self.session.execute(sql)
        try:
            return result

        except :
            self.session.close()
            return False


    def calcular_centena_padre(self,codigo,id_cliente):
        centena_padre = codigo[:3]
        centena_padre ="'00"+ centena_padre+"%'"
        codigo = "'"+ codigo+"'"
        sql = text('select sum(debe) debe, sum(haber) haber from  plan_cuentas pc ' +
                    ' inner join cuentas c on pc.id_cuenta = c.id_plan_cuentas ' +
                    ' where id_cliente =' + str(id_cliente) +' and codigo like '+ centena_padre+
                    ' and codigo <>'+ codigo )

        result = self.session.execute(sql)
        try:
            return result

        except :
            self.session.close()
            return False

    def calcular_mil_padre(self,codigo,id_cliente):
        centena_padre = codigo[:2]
        centena_padre ="'"+ centena_padre+"%'"
        codigo = "'"+ codigo+"'"
        sql = text('select sum(debe) debe, sum(haber) haber from  plan_cuentas pc ' +
                    ' inner join cuentas c on pc.id_cuenta = c.id_plan_cuentas ' +
                    ' where id_cliente =' + str(id_cliente) +' and codigo like '+ centena_padre+
                    ' and codigo <>'+ codigo )

        result = self.session.execute(sql)
        try:
            return result

        except :
            self.session.close()
            return False

    def calcular_diezmil_padre(self,codigo,id_cliente):
        centena_padre = codigo[:1]
        centena_padre ="'"+ centena_padre+"%'"
        codigo = "'"+ codigo+"'"
        sql = text('select sum(debe) debe, sum(haber) haber from  plan_cuentas pc ' +
                    ' inner join cuentas c on pc.id_cuenta = c.id_plan_cuentas ' +
                    ' where id_cliente =' + str(id_cliente) +' and codigo like '+ centena_padre+
                    ' and codigo <>'+ codigo )

        result = self.session.execute(sql)
        try:
            return result

        except :
            self.session.close()
            return False



