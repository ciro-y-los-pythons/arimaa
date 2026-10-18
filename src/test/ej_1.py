import unittest

from src.arimaa import *
from src.test.ejemplos.tableros import (
    tablero_8x8_inicial_ejemplo,
    tablero_8x8_vacio,
    tablero_mal_formado_columnas_ejemplo,
    tablero_mal_formado_filas_ejemplo,
)

"""
Archivo de tests separado para focalizarse en el Ejercicio_1
Ejecutable con: python3 -m unittest src.test.ej_1
"""


# Cantidad de Casos de test: 4
class test_tablero_bien_formado(unittest.TestCase):
    def test_8x8_lleno(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(tablero_bien_formado(t))

    def test_8x8_vacio(self):
        t = tablero_8x8_vacio()
        self.assertTrue(tablero_bien_formado(t))

    def test_8x8_mal_en_fila(self):
        t = tablero_mal_formado_filas_ejemplo()
        self.assertFalse(tablero_bien_formado(t))

    def test_8x8_mal_en_columna(self):
        t = tablero_mal_formado_columnas_ejemplo()
        self.assertFalse(tablero_bien_formado(t))


if __name__ == "__main__":
    unittest.main(verbosity=2)
