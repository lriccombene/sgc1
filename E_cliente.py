import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric, update
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_cliente(base):
      __tablename__="cliente"
      id_cliente = Column(Integer, primary_key=True, autoincrement=True)
      nombre = Column(String)
      apellido = Column(String)
      razon_social = Column(String)
      cuit_cuil =  Column(String)
      condicion_ante_iva =  Column(String)
      inicio_actividad =  Column(DateTime)
      descripcion_actividad = Column(String)
      direccion = Column(String)
      telefono = Column(String)
      celular = Column(String)
      email = Column(String)
      nombre_contacto = Column(String)
      IBB = Column(String)
      matricula = Column(String)
      session=""

      # def __init__(self,id_party,create_date,write_uid,write_date,nombre,apellido,tipo,num_doc,estado_civil,num_cliente):
      def __init__(self):
            obj_conexion =  configuracion()
            engine=create_engine(obj_conexion.config())
            Session= sessionmaker(bind=engine)
            self.session=Session()

      @classmethod
      def guardar(cls, obj_cliente ):

            obj_E_cliente = cls()
            obj_E_cliente.nombre = obj_cliente.nombre
            obj_E_cliente.apellido = obj_cliente.apellido
            obj_E_cliente.razon_social = obj_cliente.razon_social
            obj_E_cliente.inicio_actividad = obj_cliente.inicio_actividad
            obj_E_cliente.cuit_cuil = obj_cliente.cuit_cuil
            obj_E_cliente.condicion_ante_iva = obj_cliente.condicion_ante_iva
            obj_E_cliente.descripcion_actividad = obj_cliente.descripcion_actividad
            obj_E_cliente.direccion = obj_cliente.direccion
            obj_E_cliente.telefono = obj_cliente.telefono
            obj_E_cliente.celular= obj_cliente.celular
            obj_E_cliente.email = obj_cliente.email
            obj_E_cliente.nombre_contacto = obj_cliente.nombre_contacto
            obj_E_cliente.IBB = obj_cliente.IBB
            obj_E_cliente.matricula = obj_cliente.matricula
            obj_E_cliente.session.add(obj_E_cliente)

            try :
                  obj_E_cliente.session.commit()
                  obj_cliente_result = obj_E_cliente.session.query(E_cliente).filter_by(cuit_cuil=str(obj_cliente.cuit_cuil)).first()
                  obj_E_cliente.session.close()
                  return obj_cliente_result.id_cliente

            except IntegrityError :
                  obj_E_cliente.session.rollback()
                  obj_E_cliente.session.close()
                  return "False"

      def get_cliente_razon_social(self, razon_social):
            obj_cliente = self.session.query(E_cliente).filter_by(razon_social=str(razon_social)).first()
            self.session.close()
            try:
                a = obj_cliente.id_cliente
                return obj_cliente
            except:
                return false

      def get_cliente_cuit_cuil(self, cuit_cuil):
            obj_cliente = self.session.query(E_cliente).filter_by(cuit_cuil=str(cuit_cuil)).first()
            self.session.close()
            try:
                a = obj_cliente.id_cliente
                return obj_cliente
            except:
                return False

      def get_clientes(self):
            lista_clientes = self.session.query(E_cliente).all()
            self.session.close()
            return lista_clientes


      def buscar_party_party_id(self,id_cliente):
            obj_cliente = self.session.query(E_cliente).filter_by(id_cliente=id_cliente).first()
            self.session.close()
            return obj_cliente


      def actualizar(self,obj_cliente,id_cliente):
            u = update(E_cliente).where(E_cliente.id_cliente == id_cliente).values(nombre=obj_cliente.nombre, razon_social = obj_cliente.razon_social,cuit_cuil = obj_cliente.cuit_cuil, condicion_ante_iva = obj_cliente.condicion_ante_iva,descripcion_actividad = obj_cliente.descripcion_actividad,direccion = obj_cliente.direccion,telefono = obj_cliente.telefono,celular = obj_cliente.celular,email = obj_cliente.email,nombre_contacto = obj_cliente.nombre_contacto,IBB = obj_cliente.IBB,matricula = obj_cliente.matricula)
            self.session.execute(u)
            self.session.commit()
            self.session.close()

      def eliminar(self,id_cliente):
          obj_cuenta = self.session.query(E_cliente).filter_by(id_cliente=str(id_cliente)).first()
          self.session.delete(obj_cuenta)
          self.session.commit()
          return True
