
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric, update,text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_asiento(base):
      __tablename__="asiento"
      id_asiento = Column(Integer, primary_key=True, autoincrement=True)
      id_cliente = Column(Integer)
      id_ejercicio = Column(Integer)
      id_ejercicio_detalle = Column(Integer)
      fecha =  Column(DateTime)
      descripcion =  Column(String)
      session=""

      def __init__(self):
            obj_conexion =  configuracion()
            engine=create_engine(obj_conexion.config())
            Session= sessionmaker(bind=engine)
            self.session=Session()

      @classmethod
      def guardar(cls, obj_asiento ):

            obj_E_asiento = cls()
            obj_E_asiento.id_cliente = obj_asiento.id_cliente
            obj_E_asiento.id_ejercicio = obj_asiento.id_ejercicio
            obj_E_asiento.id_ejercicio_detalle = obj_asiento.id_ejercicio_detalle
            obj_E_asiento.fecha = obj_asiento.fecha
            obj_E_asiento.descripcion = obj_asiento.descripcion
            obj_E_asiento.session.add(obj_E_asiento)
            try :
                  obj_E_asiento.session.commit()
                  obj_E_asiento.session.close()
                  return obj_E_asiento

            except IntegrityError :
                  obj_E_asiento.session.rollback()
                  obj_E_asiento.session.close()
                  return "False"

      def get_asiento_id_asiento(self, id_asiento):
            obj_E_asiento = self.session.query(E_asiento).filter_by(id_asiento=str(id_asiento)).first()
            self.session.close()
            return obj_E_asiento

      def actualizar(self,obj_asiento):
            u = update(E_asiento).where(E_asiento.id_asiento == obj_asiento.id_asiento).values(fecha=obj_asiento.fecha, descripcion = obj_asiento.descripcion,id_ejercicio_detalle = obj_asiento.id_ejercicio_detalle, id_ejercicio = obj_asiento.id_ejercicio)
            self.session.execute(u)
            self.session.commit()
            self.session.close()

      def get_asiento_id_ejercicio(self, id_ejercicio):
            lista_E_asiento = self.session.query(E_asiento).filter_by(id_ejercicio=id_ejercicio).all()
            self.session.close()
            return lista_E_asiento

      def get_asiento_plan_cuenta(self, id_asiento):

            sql = text('select p.descripcion, p.id_cuenta from asiento a inner join cliente c on c.id_cliente= a.id_cliente inner join plan_cuentas p on p.id_cliente = c.id_cliente where a.id_asiento = ' + str(id_asiento))
            result = self.session.execute(sql)
            try:
                self.session.close()
                return result
            except :
                self.session.close()
                return False



