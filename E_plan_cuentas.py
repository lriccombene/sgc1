import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric, update
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_plan_cuentas(base):
      __tablename__="plan_cuentas"
      id_cuenta = Column(Integer, primary_key=True, autoincrement=True)
      codigo = Column(String)
      descripcion =  Column(String)
      id_cliente = Column(Integer)
      session=""

      def __init__(self):
            obj_conexion =  configuracion()
            engine=create_engine(obj_conexion.config())
            Session= sessionmaker(bind=engine)
            self.session=Session()

      @classmethod
      def guardar(cls, obj_cuenta ):

            obj_E_cuenta = cls()
            obj_E_cuenta.codigo = obj_cuenta.codigo
            obj_E_cuenta.descripcion = obj_cuenta.descripcion
            obj_E_cuenta.id_cliente = obj_cuenta.id_cliente
            obj_E_cuenta.session.add(obj_E_cuenta)

            try :
                  obj_E_cuenta.session.commit()
                  obj_E_cuenta.session.close()
                  return obj_E_cuenta

            except IntegrityError :
                  obj_E_proveedor.session.rollback()
                  obj_E_proveedor.session.close()
                  return "False"

      def get_cuenta_id_cuenta(self, id_cuenta):
            obj_cuenta = self.session.query(E_plan_cuentas).filter_by(id_cuenta=str(id_cuenta)).first()
            self.session.close()
            return obj_cuenta

      def get_cuentas_id_cliente(self, id_cliente):
            obj_cuentas = self.session.query(E_plan_cuentas).filter_by(id_cliente=str(id_cliente)).all()
            try :
                  id=obj_cuentas[0].id_cliente
                  self.session.close()
                  return obj_cuentas

            except :
                  self.session.close()
                  return "False"

      def actualizar(self,id_cuenta,codigo,descripcion):
            u = update(E_plan_cuentas).where(E_plan_cuentas.id_cuenta == obj_cuenta.id_cuenta).values(codigo = obj_cuenta.codigo,descripcion = obj_cuenta.descripcion)
            self.session.execute(u)
            self.session.commit()
            self.session.close()
