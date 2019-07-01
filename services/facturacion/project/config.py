# services/facturacion/project/config.py

class BaseConfig:
   """Configuracion base"""
   TESTING = False


class DevelopmentConfig(BaseConfig):
   """Configuraccion de desarrollo"""
   pass


class TestingConfig(BaseConfig):
   """Configuración de prueba"""
   pass


class ProductionConfig(BaseConfig):
   """Configuracion de produccion"""
   pass