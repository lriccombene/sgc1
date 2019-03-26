

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric, update,text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_cuenta(base):
      __tablename__="cuentas"
      id_cuenta = Column(Integer, primary_key=True, autoincrement=True)
      id_plan_cuentas = Column(Integer)
      debe = Column(Numeric)
      haber =  Column(Numeric)
      id_asiento = Column(DateTime)
      inflacion = Column(Boolean)
      session=""

      def __init__(self):
            obj_conexion =  configuracion()
            engine=create_engine(obj_conexion.config())
            Session= sessionmaker(bind=engine)
            self.session=Session()

      @classmethod
      def guardar(cls, obj_cuenta, inflacion=False ):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            obj_E_cuenta = cls()
            obj_E_cuenta.id_plan_cuentas = obj_cuenta.id_plan_cuentas
            obj_E_cuenta.debe = obj_cuenta.debe
            obj_E_cuenta.haber = obj_cuenta.haber
            obj_E_cuenta.id_asiento = obj_cuenta.id_asiento
            obj_E_cuenta.inflacion = inflacion
            obj_E_cuenta.session.add(obj_E_cuenta)
            try :
                  obj_E_cuenta.session.commit()
                  obj_E_cuenta.session.close()
                  return obj_E_cuenta

            except IntegrityError :
                  obj_E_cuenta.session.rollback()
                  obj_E_cuenta.session.close()
                  return "False"

      def get_cuenta_id_asiento(self, id_asiento):
            lista_E_cuenta = self.session.query(E_cuenta).filter_by(id_asiento=id_asiento).order_by(E_cuenta.id_plan_cuentas.asc()).all()
            self.session.close()
            return lista_E_cuenta

      def get_cuentas_filtro_inflacion(self, id_asiento):
           
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            sql = text('select p.descripcion, p.id_cuenta, p.codigo from asiento a inner join cliente c on c.id_cliente= a.id_cliente inner join plan_cuentas p on p.id_cliente = c.id_cliente where a.id_asiento = ' + str(id_asiento) + ' ORDER BY p.codigo ASC')
            result = self.session.execute(sql)
            try:
                self.session.close()
                return result
            except :
                self.session.close()
                return False


            self.session.close()
            return lista_E_cuenta



      def actualizar(self,obj_cuenta):
            u = update(E_cuenta).where(E_cuenta.id_cuenta == obj_cuenta.id_cuenta).values(debe=obj_cuenta.debe, haber = obj_cuenta.haber,id_asiento = obj_cuenta.id_asiento)
            self.session.execute(u)
            self.session.commit()
            self.session.close()

      def eliminar(self,id_asiento):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            sql= text('delete from cuentas where id_asiento=' + str(id_asiento))
            result = self.session.execute(sql)
            try:
                self.session.commit()
                self.session.close()
                return result
            except :
                self.session.close()
                return False

      def eliminar_cuenta(self,id_cuenta):

            sql= text('delete from cuentas where id_cuenta=' + str(id_cuenta))
            result = self.session.execute(sql)
            try:
                self.session.commit()
                self.session.close()
                return result
            except :
                self.session.close()
                return False
      def borrar_cuentas_de_inflacion(self,id_asiento):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            sql= text('delete from cuentas where id_asiento=' + str(id_asiento)+ ' and inflacion=True')
            result = self.session.execute(sql)
            try:
                self.session.commit()
                self.session.close()

                return result
            except :
                self.session.close()
                return False
