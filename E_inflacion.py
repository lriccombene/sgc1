
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric, update,text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_inflacion(base):
      __tablename__="inflacion"
      id_inflacion = Column(Integer, primary_key=True, autoincrement=True)
      nro_mes = Column(Integer)
      mes = Column(String)
      anio =  Column(Integer)
      valor=Column(Numeric)
      session=""

      def __init__(self):
            obj_conexion =  configuracion()
            engine=create_engine(obj_conexion.config())
            Session= sessionmaker(bind=engine)
            self.session=Session()

      @classmethod
      def guardar(cls, obj_inflacion ):

            obj_E_inflacion = cls()
            obj_E_inflacion.anio = obj_inflacion.anio
            obj_E_inflacion.mes = obj_inflacion.mes
            obj_E_inflacion.nro_mes = obj_inflacion.nro_mes
            obj_E_inflacion.valor = obj_inflacion.valor

            obj_E_inflacion.session.add(obj_E_inflacion)
            print("holaaaa")
            try :
                  obj_E_inflacion.session.commit()
                  obj_E_inflacion.session.close()
                  return obj_E_inflacion

            except IntegrityError :
                  obj_E_inflacion.session.rollback()
                  obj_E_inflacion.session.close()
                  return "False"

      def actualizar(self,obj_inflacion):
           
            sql = text('Update inflacion set valor=' + str(obj_inflacion.valor)+' where anio='+ str(obj_inflacion.anio)+ ' and nro_mes=' + str(obj_inflacion.nro_mes))
            result = self.session.execute(sql)
            try:
                  self.session.commit()
                  self.session.close()
                  return result
            except:
                  self.session.close()
                  return False


      def get_inflacion_anio(self, anio):
            lista_E_inflacion = self.session.query(E_inflacion).filter_by(anio=anio).order_by(E_inflacion.nro_mes.asc()).all()
            self.session.close()
            print(len(lista_E_inflacion))
            return lista_E_inflacion

