import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric, update,text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_libro_iva_compras(base):
      __tablename__="libro_iva_compras"
      id_libro_iva_compras = Column(Integer, primary_key=True, autoincrement=True)
      fecha = Column(DateTime)
      nro_comprobante = Column(String)
      tipo =  Column(String)
      id_proveedor =  Column(Integer)
      ref =  Column(String)
      neto_10_5 = Column(Numeric)
      neto_21 = Column(Numeric)
      neto_27 = Column(Numeric)
      iva = Column(Numeric)
      monotributo = Column(Numeric)
      impuestos_otros = Column(Numeric)
      no_grabado = Column(Numeric)
      percepcion_ibb = Column(Numeric)
      percepcion_iva = Column(Numeric)
      id_cliente = Column(Integer)
      id_ejercicio = Column(Integer)
      id_ejercicio_detalle = Column(Integer)
      neto = Column(Numeric)
      session=""

      def __init__(self):
            obj_conexion = configuracion()
            engine=create_engine(obj_conexion.config())
            Session= sessionmaker(bind=engine)
            self.session = Session()

      @classmethod
      def guardar(cls, obj_libro_iva_compras ):

            obj_E_libro_iva_compras = cls()
            obj_E_libro_iva_compras.fecha = obj_libro_iva_compras.fecha
            obj_E_libro_iva_compras.nro_comprobante = obj_libro_iva_compras.nro_comprobante
            obj_E_libro_iva_compras.tipo = obj_libro_iva_compras.tipo
            obj_E_libro_iva_compras.id_proveedor = obj_libro_iva_compras.id_proveedor
            obj_E_libro_iva_compras.ref = obj_libro_iva_compras.ref
            obj_E_libro_iva_compras.neto_10_5 = obj_libro_iva_compras.neto_10_5
            obj_E_libro_iva_compras.neto_21 = obj_libro_iva_compras.neto_21
            obj_E_libro_iva_compras.neto_27 = obj_libro_iva_compras.neto_27
            obj_E_libro_iva_compras.iva = obj_libro_iva_compras.iva
            obj_E_libro_iva_compras.monotributo = obj_libro_iva_compras.monotributo
            obj_E_libro_iva_compras.impuestos_otros = obj_libro_iva_compras.impuestos_otros
            obj_E_libro_iva_compras.no_grabado = obj_libro_iva_compras.no_grabado
            obj_E_libro_iva_compras.percepcion_ibb = obj_libro_iva_compras.percepcion_ibb
            obj_E_libro_iva_compras.percepcion_iva = obj_libro_iva_compras.monotributo
            obj_E_libro_iva_compras.id_cliente = obj_libro_iva_compras.id_cliente
            obj_E_libro_iva_compras.id_ejercicio = obj_libro_iva_compras.id_ejercicio
            obj_E_libro_iva_compras.id_ejercicio_detalle = obj_libro_iva_compras.id_ejercicio_detalle

            obj_E_libro_iva_compras.session.add(obj_libro_iva_compras)
            try:
                obj_E_libro_iva_compras.session.commit()
                obj_E_libro_iva_compras.session.close()
                return obj_E_libro_iva_compras
            except IntegrityError:
                obj_E_libro_iva_compras.session.rollback()
                obj_E_libro_iva_compras.session.close()
                return "False"

      def get_libro_iva_compras(self, id_cliente):
            obj_E_libro_iva_compras = self.session.query(E_libro_iva_compras).filter_by(id_cliente=id_cliente).all()
            self.session.close()
            return obj_E_libro_iva_compras

      def get_grilla_libro_iva_compras(self, id_ejercicio, id_ejercicio_detalle):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            sql = text('SELECT v.id_libro_iva_compras, v.fecha, v.nro_comprobante , p.nombre,v.neto from libro_iva_compras v inner join proveedor p on v.id_proveedor= p.id_proveedor WHERE id_ejercicio = ' + str(id_ejercicio) + ' AND id_ejercicio_detalle =' + str(id_ejercicio_detalle))
            result = self.session.execute(sql)
            try:
                  return result
            except :
                  self.session.close()
                  return False


      def get_reporte_libro_iva_compras(self, id_ejercicio):
            # pyqtRemoveInputHook()
            # import pdb; pdb.set_trace()
            cadena ='SELECT v.id_libro_iva_compras,v.fecha,v.nro_comprobante,v.tipo,v.ref,v.neto_10_5,v.neto_21,v.neto_27,' \
                    'v.iva,v.monotributo,v.impuestos_otros,v.no_grabado,v.percepcion_ibb ,v.percepcion_iva, p.nombre ' \
                    'from libro_iva_compras v ' \
                    'inner join proveedor p  on v.id_proveedor= p.id_proveedor ' \
                    'WHERE id_ejercicio = ' + str(id_ejercicio) + ' order by v.id_libro_iva_compras'
            sql = text(cadena)
            result = self.session.execute(sql)
            try:
                  return result
            except:
                  self.session.close()
                  return False
