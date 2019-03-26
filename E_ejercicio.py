
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric, update,text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_ejercicio(base):
      __tablename__="ejercicio"
      id_ejercicio= Column(Integer, primary_key=True, autoincrement=True)
      tipo = Column(String)
      descripcion = Column(String)
      anio =  Column(DateTime)
      fec_inicio =  Column(DateTime)
      fec_fin =  Column(DateTime)
      id_cliente = Column(Integer)
      session=""

      # def __init__(self,id_party,create_date,write_uid,write_date,nombre,apellido,tipo,num_doc,estado_civil,num_cliente):
      def __init__(self):
            obj_conexion =  configuracion()
            engine=create_engine(obj_conexion.config())
            Session= sessionmaker(bind=engine)
            self.session=Session()

      @classmethod
      def guardar(cls, obj_ejercicio ):

            obj_E_ejercicio = cls()
            obj_E_ejercicio.tipo = obj_ejercicio.tipo
            obj_E_ejercicio.descripcion = obj_ejercicio.descripcion
            obj_E_ejercicio.anio = obj_ejercicio.anio
            obj_E_ejercicio.fec_inicio = obj_ejercicio.fec_inicio
            obj_E_ejercicio.fec_fin = obj_ejercicio.fec_fin
            obj_E_ejercicio.id_cliente = obj_ejercicio.id_cliente
            obj_E_ejercicio.session.add(obj_E_ejercicio)

            try :
                  obj_E_ejercicio.session.commit()
                  obj_E_ejercicio.session.close()
                  obj_ejercicio = obj_E_ejercicio.buscar_ejercio_id_cliente_descripcion(obj_ejercicio.id_cliente, obj_ejercicio.descripcion)
                  return obj_ejercicio
            except IntegrityError :
                  obj_E_ejercicio.session.rollback()
                  obj_E_ejercicio.session.close()
                  return "False"

      def get_ejercicio_id_cliente(self,id_cliente):
            list_ejercicio = self.session.query(E_ejercicio).filter_by(id_cliente=str(id_cliente)).all()
            self.session.close()
            return list_ejercicio

      def get_ejercicio(self):
            list_ejercicio = self.session.query(E_ejercicio).all()
            self.session.close()
            return list_ejercicio

      def get_ejercicio_id_ejercicio(self, id_ejercicio):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            obj_ejercicio = self.session.query(E_ejercicio).filter_by(id_ejercicio=str(id_ejercicio)).first()
            self.session.close()
            return obj_ejercicio

      def buscar_ejercio_id_cliente_descripcion(self,id_cliente, descripcion):

            obj_ejercicio = self.session.query(E_ejercicio).filter_by(id_cliente = id_cliente, descripcion=descripcion).first()
            self.session.close()
            return obj_ejercicio


      def actualizar_ejercicio(self,obj_ejercicio):
          u = update(E_ejercicio).where(E_ejercicio.id_cliente == obj_ejercicio.id_cliente).values(tipo = obj_ejercicio.tipo, descripcion = obj_ejercicio.descripcion,anio = obj_ejercicio.anio, fec_inicio = obj_ejercicio.fec_inicio,fec_fin = obj_ejercicio.fec_fin)
          self.session.execute(u)
          self.session.commit()
          self.session.close()

      def eliminar_ejercicio(self,id_ejercicio):
           
            sql = text('delete from ejercicio where id_ejercicio=' + str(id_ejercicio))
            result = self.session.execute(sql)
            try:
                  self.session.commit()
                  self.session.close()
                  return result
            except:
                  self.session.close()
                  return False


