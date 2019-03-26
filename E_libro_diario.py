import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric, update
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_libro_diario(base):
      __tablename__="libro_diario"
      id_libro_diario = Column(Integer, primary_key=True, autoincrement=True)
      id_cliente = Column(Integer)
      id_asiento = Column(Integer)
      id_cuentas =  Column(Integer)
      id_ejercicio = Column(Integer)
      session=""

      def __init__(self):
            obj_conexion =  configuracion()
            engine=create_engine(obj_conexion.config())
            Session= sessionmaker(bind=engine)
            self.session=Session()

      @classmethod
      def guardar(cls, obj_libro_diario ):

            obj_E_libro_diario = cls()
            obj_E_libro_diario.id_cliente = obj_libro_diario.id_cliente
            obj_E_libro_diario.id_asiento = obj_libro_diario.id_asiento
            obj_E_libro_diario.id_cuentas = obj_libro_diario.id_cuentas
            obj_E_libro_diario.id_ejercicio = obj_libro_diario.id_ejercicio
            obj_E_libro_diario.session.add(obj_E_libro_diario)
            try :
                obj_E_libro_diario.session.commit()
                obj_E_libro_diario.session.close()
                return obj_E_libro_diario

            except IntegrityError :
                obj_E_libro_diario.session.rollback()
                obj_E_libro_diario.session.close()
                return "False"

      def get_libro_diario_id_asiento(self, id_libro_diario):
            obj_E_libro_diario = self.session.query(E_libro_diario).filter_by(id_libro_diario=str(id_libro_diario)).first()
            self.session.close()
            return obj_E_libro_diario

      def actualizar(self,obj_ibro_diario):
            u = update(E_libro_diario).where(E_libro_diario.id_libro_diarioa == obj_ibro_diario.id_libro_diario).values(id_asiento=obj_ibro_diario.id_asiento, id_cuentas = obj_ibro_diario.id_cuentas,id_ejercicio = obj_ibro_diario.id_ejercicio)
            self.session.execute(u)
            self.session.commit()
            self.session.close()
