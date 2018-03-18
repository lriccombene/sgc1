

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric, update
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
      debe = Column(Integer)
      haber =  Column(Integer)
      id_asiento =  Column(DateTime)
      session=""

      def __init__(self):
            obj_conexion =  configuracion()
            engine=create_engine(obj_conexion.config())
            Session= sessionmaker(bind=engine)
            self.session=Session()

      @classmethod
      def guardar(cls, obj_cuenta ):

            obj_E_cuenta = cls()
            obj_E_cuenta.id_plan_cuentas = obj_cuenta.id_plan_cuentas
            obj_E_cuenta.debe = obj_cuenta.debe
            obj_E_cuenta.haber = obj_cuenta.haber
            obj_E_cuenta.id_asiento = obj_cuenta.id_asiento
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
            lista_E_cuenta = self.session.query(E_cuenta).filter_by(id_asiento=str(id_asiento)).all()
            self.session.close()
            return lista_E_cuenta

      def actualizar(self,obj_cuenta):
            u = update(E_cuenta).where(E_cuenta.id_cuenta == obj_cuenta.id_cuenta).values(debe=obj_cuenta.debe, haber = obj_cuenta.haber,id_asiento = obj_cuenta.id_asiento)
            self.session.execute(u)
            self.session.commit()
            self.session.close()
