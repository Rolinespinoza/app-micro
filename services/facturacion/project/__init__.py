# services/facturacion/project/__init__.py

from flask import Flask
import os  # nuevo
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS  # nuevo


 # instanciando la db
db = SQLAlchemy()  # nuevo
toolbar = DebugToolbarExtension()  # nuevo
cors = CORS() # nuevo

# nuevo
def create_app(script_info=None):

    #instanciamos la app
    app = Flask(__name__)

    # estableciendo la configuracion 
    app_settings = os.getenv('APP_SETTINGS')   # Nuevo
    app.config.from_object(app_settings)       # Nuevo

    # levantando extensiones 
    db.init_app(app)
    toolbar.init_app(app)
    cors.init_app(app) #nuevo

    # register blueprints
    from project.api.facturacion import facturacion_blueprint
    app.register_blueprint(facturacion_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}
    return app