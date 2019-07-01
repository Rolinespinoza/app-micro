# services/facturacion/project/__init__.py

from flask import Flask, jsonify

#instanciamos la app
app = Flask(__name__)

# establelciendo configuracion 
app.config.from_object('project.config.DevelopmentConfig') # nuevo 

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
