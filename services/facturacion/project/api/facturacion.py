# services/facturacion/project/api/facturacion.py

from flask import Blueprint, jsonify, request, render_template, redirect
from project.api.models import Articulo, Factura, Detalle, Cliente
from project import db
from sqlalchemy import exc

facturacion_blueprint = Blueprint('facturacion', __name__, template_folder='./templates')


@facturacion_blueprint.route('/facturacion/ping', methods=['GET'])
def ping_pong():
   return jsonify({
       'estado':'exito',
       'mensaje': 'respuesta exitosa pong'
   })

@facturacion_blueprint.route('/articulos', methods=['GET'])
def get_all_articulos():
    """Obtener la lista de articulos de bd"""
    response_object = {
       'estado': 'exitoso',
       'data': {
          'articulos': [articulo.to_json()for articulo in Articulo.query.all()]
        }
    }
    return jsonify(response_object), 200


@facturacion_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        db.session.add(Articulo(nombre=nombre, precio=precio, stock=stock ))
        db.session.commit()
    articulos = Articulo.query.all()
    return render_template('index.html', articulos=articulos)


@facturacion_blueprint.route('/facturas', methods=['GET', 'POST'])
def registrar_factura():
    if request.method == 'POST':
        estado = request.form['estado']
        db.session.add(Factura(estado=estado))
        db.session.commit()
    facturas = Factura.query.all()
    clientes = Cliente.query.all()
    return render_template('factura.html', facturas=facturas, clientes=clientes)


@facturacion_blueprint.route('/clientes', methods=['GET', 'POST'])
def registrar_cliente():
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        telefono = request.form['telefono']
        email = request.form['email']
        db.session.add(Cliente(nombres=nombres, apellidos=apellidos, telefono=telefono, email=email))
        db.session.commit()
    clientes = Cliente.query.all()
    return render_template('cliente.html', clientes=clientes)


@facturacion_blueprint.route('/delete/articulo/<idarticulos>', methods=['POST', 'GET'])
def delete_articulo(idarticulos):
    articulo = Articulo.query.filter_by(idarticulos=int(idarticulos)).first()
    db.session.delete(articulo)
    db.session.commit()
    return redirect("/")

@facturacion_blueprint.route('/delete/factura/<idarticulos>', methods=['POST', 'GET'])
def delete_factura(idarticulos):
    articulo = Articulo.query.filter_by(idarticulos=int(idarticulos)).first()
    db.session.delete(articulo)
    db.session.commit()
    return redirect("/facturas")

@facturacion_blueprint.route('/delete/detalle/<idarticulos>', methods=['POST', 'GET'])
def delete_detalle(idarticulos):
    articulo = Articulo.query.filter_by(idarticulos=int(idarticulos)).first()
    db.session.delete(articulo)
    db.session.commit()
    return redirect("/detalles")

@facturacion_blueprint.route('/delete/cliente/<idarticulos>', methods=['POST', 'GET'])
def delete_cliente(idarticulos):
    articulo = Articulo.query.filter_by(idarticulos=int(idarticulos)).first()
    db.session.delete(articulo)
    db.session.commit()
    return redirect("/clientes")