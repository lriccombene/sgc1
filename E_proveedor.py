import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric, update
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_proveedor(base):
      __tablename__="proveedor"
      id_proveedor = Column(Integer, primary_key=True, autoincrement=True)
      nombre = Column(String)
      razon_social = Column(String)
      cuit_cuil =  Column(String)
      condicion_ante_iva =  Column(String)
      ref =  Column(String)
      id_cliente = Column(String)
      session=""

      def __init__(self):
            obj_conexion =  configuracion()
            engine=create_engine(obj_conexion.config())
            Session= sessionmaker(bind=engine)
            self.session=Session()

      @classmethod
      def guardar(cls, obj_proveedor ):

            obj_E_proveedor = cls()
            obj_E_proveedor.nombre = obj_proveedor.nombre
            obj_E_proveedor.razon_social = obj_proveedor.razon_social
            obj_E_proveedor.cuit_cuil = obj_proveedor.cuit_cuil
            obj_E_proveedor.condicion_ante_iva = obj_proveedor.condicion_ante_iva
            obj_E_proveedor.ref = obj_proveedor.ref
            obj_E_proveedor.id_cliente = obj_proveedor.id_cliente
            obj_E_proveedor.session.add(obj_E_proveedor)
            try :
                  obj_E_proveedor.session.commit()
                  obj_E_proveedor.session.close()
                  return obj_E_proveedor

            except IntegrityError :
                  obj_E_proveedor.session.rollback()
                  obj_E_proveedor.session.close()
                  return "False"

      def get_proveedor_razon_social(self, razon_social,id_cliente):
            obj_proveedor = self.session.query(E_proveedor).filter_by(razon_social=str(razon_social),id_cliente=id_cliente ).first()
            self.session.close()
            return obj_cliente

      def get_proveedor_cuit_cuil(self, cuit_cuil,id_cliente):
            obj_proveedor = self.session.query(E_proveedor).filter_by(cuit_cuil=str(cuit_cuil),id_cliente = id_cliente).first()
            self.session.close()
            return obj_proveedor

      def buscar_proveedores(self,id_cliente):
            obj_proveedores = self.session.query(E_proveedor).filter_by(id_cliente=id_cliente).all()
            self.session.close()
            return obj_proveedores

      def actualizar(self,obj_proveedor):
            u = update(E_proveedor).where(E_proveedor.id_proveedor == obj_proveedor.id_proveedor).values(nombre=obj_proveedor.nombre, razon_social = obj_proveedor.razon_social,cuit_cuil = obj_proveedor.cuit_cuil, condicion_ante_iva = obj_proveedor.condicion_ante_iva,ref = obj_proveedor.ref)
            self.session.execute(u)
            self.session.commit()
            self.session.close()
