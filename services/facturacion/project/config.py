# services/facturacion/project/config.py

class BaseConfig:
   """Configuracion base"""
   TESTING = False
import os  # nuevo




class BaseConfig:
   """Configuración base"""
   TESTING = False
   SQLALCHEMY_TRACK_MODIFICATIONS = False  # nuevo


class DevelopmentConfig(BaseConfig):
   """Configuraccion de desarrollo"""
   SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # nuevo


class TestingConfig(BaseConfig):
   """Configuración de prueba"""
   TESTING = True
   SQLALCHEMY_DATABSE_URI = os.environ.get('DATABASE_TEST_URL')  # nuevo


class ProductionConfig(BaseConfig):
   """Configuracion de produccion"""
   SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # nuevo