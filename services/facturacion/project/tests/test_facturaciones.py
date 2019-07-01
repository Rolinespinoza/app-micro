# services/facturacion/project/tests/test_facturaciones.py


import json
import unittest

from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    """Tests for the Facturacion Service."""

    def test_facturacion(self):
        """Asegúrese de que la ruta / ping se comporte correctamente."""
        response = self.client.get('/facturacion/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('respuesta exitosa pong', data['mensaje'])
        self.assertIn('exito', data['estado'])


if __name__ == '__main__':
    unittest.main()