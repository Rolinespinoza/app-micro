# services/orders/project/__init__.py

from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/users/ping', methods=['GET'])
def ping_pong():
   return jsonify({
       'status':'success',
       'message': 'respuesta exitosa'
   })
