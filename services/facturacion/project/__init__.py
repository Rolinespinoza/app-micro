# services/facturacion/project/__init__.py

from flask import Flask, jsonify
import os  # nuevo
from flask_sqlalchemy import SQLAlchemy  # nuevo
from datetime import datetime # nuevo
from dateutil import parser as datetime_parser # nuevo

#instanciamos la app
app = Flask(__name__)

# estableciendo la configuracion 
app_settings = os.getenv('APP_SETTINGS')   # Nuevo
app.config.from_object(app_settings)       # Nuevo

# instanciando la db
db = SQLAlchemy(app)  # nuevo

# Modelo de la base de datos 
class Cliente(db.Model):  # nuevo
    __tablename__ = 'clientes'
    idclientes = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombres = db.Column(db.String(128), nullable=False)
    apellidos = db.Column(db.String(128), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(128), nullable=False)
    estado = db.Column(db.Boolean(), default=True, nullable=False)
    facturas = db.relationship('Factura', backref='cliente', lazy='dynamic', cascade='all, delete-orphan')

    def __init__(self, nombres, apellidos, telefono, email):
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email


class Factura(db.Model):  # nuevo
    __tablename__ = 'facturas'
    idfacturas = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha = db.Column(db.DateTime, default=datetime.now)
    estado = db.Column(db.Boolean(), default=True, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.idclientes'), index=True)
    detalles = db.relationship('Detalle', backref='factura', lazy='dynamic', cascade='all, delete-orphan')

    def __init__(self, fecha, estado):
        self.fecha = fecha
        self.estado = estado


class Detalle(db.Model):  # nuevo
    __tablename__ = 'detalles'
    iddetalles = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cantidad = db.Column(db.Integer, nullable=False)
    costo = db.Column(db.Integer, nullable=False)
    articulo_id = db.Column(db.Integer, db.ForeignKey('articulos.idarticulos'), index=True)
    factura_id = db.Column(db.Integer, db.ForeignKey('facturas.idfacturas'), index=True)

    def __init__(self, cantidad, costo):
        self.cantidad = cantidad
        self.costo = costo


class Articulo(db.Model):  # nuevo
    __tablename__ = 'articulos'
    idarticulos = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(128), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.Boolean(), default=True, nullable=False)
    detalles = db.relationship('Detalle', backref='articulo', lazy='dynamic', cascade='all, delete-orphan')

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
# Rutas de navegación 
@app.route("/")
def hello():
    return "Hello World!"

@app.route('/facturacion/ping', methods=['GET'])
def ping_pong():
   return jsonify({
       'estado':'exito',
       'mensaje': 'respuesta exitosa pong'
   })

@app.route("/hola")
def saludo():
    return "Hola mundo!"
