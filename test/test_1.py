import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from src.arimaa import *
from test.ejemplos.tableros import *

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


class test_movimiento_bien_formado(unittest.TestCase):
    def test_movimiento_no_esta_en_tablero(self):
        self.assertFalse(
            movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(9, -1), [NORTE]))
        )
    def test_movimiento_mover_a_secas_con_un_paso(self):
        self.assertTrue(
            movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE]))
        )
    def test_movimiento_mover_a_secas_con_dos_pasos(self):
        self.assertFalse(
            movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(2, 3), [NORTE,SUR]))
        )
    def test_movimiento_empujar_con_dos_pasos(self):
        self.assertTrue(
            movimiento_bien_formado(Movimiento(EMPUJAR, Posicion(0, 1), [NORTE,ESTE]))
        )
    def test_movimiento_empujar_con_un_paso(self):
        self.assertFalse(
            movimiento_bien_formado(Movimiento(EMPUJAR, Posicion(0, 1), [NORTE]))
        )
    def test_movimiento_arrastrar_con_dos_pasos(self):
        self.assertTrue(
            movimiento_bien_formado(Movimiento(ARRASTRAR, Posicion(0, 1), [NORTE,ESTE]))
        )
    def test_movimiento_arrastrar_con_un_paso(self):
        self.assertFalse(
            movimiento_bien_formado(Movimiento(ARRASTRAR, Posicion(0, 1), [NORTE]))
        )

class test_juego_bien_formado(unittest.TestCase):
    def test_juego_valido_minimo(self):
        j = Juego(tablero_8x8_vacio(), DORADO, 0)
        self.assertTrue(juego_bien_formado(j))
    def test_juego_valido_maximo(self):
        j = Juego(tablero_8x8_vacio(), DORADO, 3)
        self.assertTrue(juego_bien_formado(j))
    def test_juego_invalido_pasos_negativos(self):
        j = Juego(tablero_8x8_vacio(), DORADO, -1)
        self.assertFalse(juego_bien_formado(j))
    def test_juego_invalido_pasos_excedidos(self):
        j = Juego(tablero_8x8_vacio(), DORADO, 4)
        self.assertFalse(juego_bien_formado(j))
    def test_juego_invalido_tablero_mal(self):
        j = Juego(tablero_mal_formado_filas_ejemplo(), DORADO, 0)
        self.assertFalse(juego_bien_formado(j))

if __name__ == "__main__":
    unittest.main(verbosity=2)
