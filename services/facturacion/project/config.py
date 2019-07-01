# services/facturacion/project/config.py


import os  # nuevo

class BaseConfig:
   """Configuración base"""
   TESTING = False
   SQLALCHEMY_TRACK_MODIFICATIONS = False  # nuevo
   SECRET_KEY = '1'
   DEBUG_TB_ENABLED = False
   DEBUG_TB_INTERCEPT_REDIRECTS = False


class DevelopmentConfig(BaseConfig):
   """Configuraccion de desarrollo"""
   SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # nuevo
   DEBUG_TB_ENABLED = True #nuevo

class TestingConfig(BaseConfig):
   """Configuración de prueba"""
   TESTING = True
   SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')  # nuevo


class ProductionConfig(BaseConfig):
   """Configuracion de produccion"""
   SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # nuevo