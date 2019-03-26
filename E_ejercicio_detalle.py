import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric, update
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_ejercicio_detalle(base):
      __tablename__="ejercicio_detalle"
      id_ejercicio_detalle = Column(Integer, primary_key=True, autoincrement=True)
      mes = Column(String)
      estado = Column(String)
      id_ejercicio =  Column(DateTime)
      nro =  Column(Integer)
      session=""

      # def __init__(self,id_party,create_date,write_uid,write_date,nombre,apellido,tipo,num_doc,estado_civil,num_cliente):
      def __init__(self):
          obj_conexion =  configuracion()
          engine=create_engine(obj_conexion.config())
          Session= sessionmaker(bind=engine)
          self.session=Session()

      @classmethod
      def guardar(cls, obj_ejercicio_detalle ):
            obj_E_ejercicio_detalle = cls()
            obj_E_ejercicio_detalle.mes = obj_ejercicio_detalle.mes
            obj_E_ejercicio_detalle.estado = obj_ejercicio_detalle.estado
            obj_E_ejercicio_detalle.id_ejercicio = obj_ejercicio_detalle.id_ejercicio
            obj_E_ejercicio_detalle.nro = obj_ejercicio_detalle.nro
            obj_E_ejercicio_detalle.session.add(obj_E_ejercicio_detalle)

            try :
                  obj_E_ejercicio_detalle.session.commit()
                  obj_E_ejercicio_detalle.session.close()
                  return True

            except IntegrityError :
                  obj_E_ejercicio_detalle.session.rollback()
                  obj_E_ejercicio_detalle.session.close()
                  return "False"

      def get_ejercicio_detalle(self ):
          obj_ejercicio_detalle = self.session.query(E_ejercicio_detalle).all()
          self.session.close()
          return obj_ejercicio_detalle

      def buscar_ejercicios_id_ejercicio(self,id_ejercicio):
          obj_ejercicio_detalle = self.session.query(E_ejercicio_detalle).filter_by(id_ejercicio=id_ejercicio).all()
          self.session.close()
          return obj_ejercicio_detalle

      def actualizar_estado(self,id_ejer_det, estado):
          u = update(E_ejercicio_detalle).where(E_ejercicio_detalle.id_ejercicio_detalle == id_ejer_det).values(estado= estado)
          self.session.execute(u)
          self.session.commit()
          self.session.close()
