import unittest

from src.arimaa import *
from test.ejemplos.tableros import (
    tablero_8x8_inicial_ejemplo,
    tablero_8x8_vacio,
    tablero_mal_formado_columnas_ejemplo,
    tablero_mal_formado_filas_ejemplo,
)

"""
Archivo de tests separado para focalizarse en el Ejercicio_1
Ejecutable con: python3 -m unittest test.ej_1
"""


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


class test_posicion_en_tablero(unittest.TestCase):
    def test_posicion_valida_minimo(self):
        pos = Posicion(0, 0)
        self.assertTrue(posicion_en_tablero(pos))

    def test_posicion_valida_maximo(self):
        pos = Posicion(7, 7)
        self.assertTrue(posicion_en_tablero(pos))

    def test_posicion_col_pasa_min(self):
        pos = Posicion(1, -1)
        self.assertFalse(posicion_en_tablero(pos))

    def test_posicion_col_pasa_max(self):
        pos = Posicion(1, 8)
        self.assertFalse(posicion_en_tablero(pos))

    def test_posicion_row_pasa_min(self):
        pos = Posicion(-1, 1)
        self.assertFalse(posicion_en_tablero(pos))

    def test_posicion_row_pasa_max(self):
        pos = Posicion(8, 1)
        self.assertFalse(posicion_en_tablero(pos))

    def test_posicion_todo_invalido_min(self):
        pos = Posicion(-1, -1)
        self.assertFalse(posicion_en_tablero(pos))

    def test_posicion_todo_invalido_max(self):
        pos = Posicion(8, 8)
        self.assertFalse(posicion_en_tablero(pos))


if __name__ == "__main__":
    unittest.main(verbosity=2)
