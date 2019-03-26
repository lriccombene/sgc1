import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric, update,text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_libro_iva_ventas(base):
    __tablename__="libro_iva_ventas"
    id_libro_iva_ventas = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(DateTime)
    nro_comprobante = Column(String)
    tipo = Column(String)
    id_proveedor = Column(Integer)
    ref = Column(String)
    neto = Column(Numeric)
    neto_10_5 = Column(Numeric)
    neto_21 = Column(Numeric)
    neto_27 = Column(Numeric)
    iva = Column(Numeric)
    monotributo = Column(Numeric)
    impuestos_otros = Column(Numeric)
    no_gravado = Column(Numeric)
    percepcion_ibb = Column(Numeric)
    percepcion_iva = Column(Numeric)
    id_cliente = Column(Integer)
    id_ejercicio = Column(Integer)
    id_ejercicio_detalle = Column(Integer)

    session = ""

    def __init__(self):
        obj_conexion = configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session = Session()

    @classmethod
    def guardar(cls, obj_libro_iva_ventas):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj_E_libro_iva_ventas = cls()
        obj_E_libro_iva_ventas.fecha = obj_libro_iva_ventas.fecha
        obj_E_libro_iva_ventas.nro_comprobante = obj_libro_iva_ventas.nro_comprobante
        obj_E_libro_iva_ventas.tipo = obj_libro_iva_ventas.tipo
        obj_E_libro_iva_ventas.id_proveedor = obj_libro_iva_ventas.id_proveedor
        obj_E_libro_iva_ventas.ref = obj_libro_iva_ventas.ref
        obj_E_libro_iva_ventas.neto_10_5 = obj_libro_iva_ventas.neto_10_5
        obj_E_libro_iva_ventas.neto_21 = obj_libro_iva_ventas.neto_21
        obj_E_libro_iva_ventas.neto_27 = obj_libro_iva_ventas.neto_27
        obj_E_libro_iva_ventas.iva = obj_libro_iva_ventas.iva
        obj_E_libro_iva_ventas.monotributo = obj_libro_iva_ventas.monotributo
        obj_E_libro_iva_ventas.impuestos_otros = obj_libro_iva_ventas.impuestos_otros
        obj_E_libro_iva_ventas.no_gravado = obj_libro_iva_ventas.no_gravado
        obj_E_libro_iva_ventas.percepcion_IBB = obj_libro_iva_ventas.percepcion_IBB
        obj_E_libro_iva_ventas.percepcion_iva = obj_libro_iva_ventas.percepcion_iva
        obj_E_libro_iva_ventas.id_cliente = obj_libro_iva_ventas.id_cliente
        obj_E_libro_iva_ventas.id_ejercicio = obj_libro_iva_ventas.id_ejercicio
        obj_E_libro_iva_ventas.id_ejercicio_detalle = obj_libro_iva_ventas.id_ejercicio_detalle
        obj_E_libro_iva_ventas.session.add(obj_libro_iva_ventas)
        try:
            obj_E_libro_iva_ventas.session.commit()
            obj_E_libro_iva_ventas.session.close()
            return obj_E_libro_iva_ventas
        except IntegrityError:
            obj_E_libro_iva_ventas.session.rollback()
            obj_E_libro_iva_ventas.session.close()
            return "False"

    def get_libro_iva_ventas(self, id_cliente):
        obj_E_libro_iva_compras = self.session.query(E_libro_iva_ventas).filter_by(id_cliente=id_cliente).all()
        self.session.close()
        return obj_E_libro_iva_compras


    def get_libro_iva_ventas_ejericio(self, id_ejercicio, id_ejercicio_detalle):
        obj_E_libro_iva_compras = self.session.query(E_libro_iva_ventas).filter_by(id_ejercicio = id_ejercicio, id_ejercicio_detalle = id_ejercicio_detalle).all()
        self.session.close()
        return obj_E_libro_iva_compras


    def get_grila_libro_iva_ventas(self, id_ejercicio, id_ejercicio_detalle):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        sql = text('SELECT v.id_libro_iva_ventas, v.fecha, v.nro_comprobante , p.nombre,(v.neto_10_5 + v.neto_21 + v.neto_27) neto from libro_iva_ventas v inner join proveedor p on v.id_proveedor= p.id_proveedor WHERE id_ejercicio = ' + str(id_ejercicio) + ' AND id_ejercicio_detalle =' + str(id_ejercicio_detalle))
        result = self.session.execute(sql)
        try:
            return result
        except :
            self.session.close()
            return False
