import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from src.arimaa import *
from test.ejemplos.tableros import *


class test_posicion_en_fila_inicial(unittest.TestCase):
    def test_dorado_en_posicion_en_fila_inicial(self):
        pos = Posicion(0, 0)
        col = DORADO
        self.assertTrue(posicion_en_fila_inicial(pos, col))

    def test_plateado_en_posicion_en_fila_inicial(self):
        pos = Posicion(7, 0)
        col = PLATEADO
        self.assertTrue(posicion_en_fila_inicial(pos, col))

    def test_dorado_fuera_de_posicion_en_fila_inicial(self):
        pos = Posicion(3, 0)
        col = DORADO
        self.assertFalse(posicion_en_fila_inicial(pos, col))

    def test_plateado_fuera_de_posicion_en_fila_inicial(self):
        pos = Posicion(5, 0)
        col = PLATEADO
        self.assertFalse(posicion_en_fila_inicial(pos, col))

    def test_dorado_en_posicion_en_fila_inicial_enemiga(self):
        pos = Posicion(7, 0)
        col = DORADO
        self.assertFalse(posicion_en_fila_inicial(pos, col))

    def test_plateado_en_posicion_en_fila_inicial_enemiga(self):
        pos = Posicion(0, 0)
        col = PLATEADO
        self.assertFalse(posicion_en_fila_inicial(pos, col))


class test_es_inicio_de_turno(unittest.TestCase):
    def test_inicio_de_juego(self):
        j = Juego(tablero_8x8_inicial_ejemplo(),DORADO,0)
        col = DORADO
        self.assertTrue(es_inicio_de_turno(j, col))

    def test_inicio_de_juego_no_coincide_color(self):
        j = Juego(tablero_8x8_inicial_ejemplo(),DORADO,0)
        col = PLATEADO
        self.assertFalse(es_inicio_de_turno(j, col))

    def test_ya_hay_pasos_consumidos(self):
        j = Juego(tablero_8x8_mueve_conejo_dorado_h3(),DORADO,1)
        col = DORADO
        self.assertFalse(es_inicio_de_turno(j, col))

    def test_ya_hay_pasos_consumidos_y_no_coincide_color(self):
        j = Juego(tablero_8x8_mueve_conejo_dorado_h3(),DORADO,1)
        col = PLATEADO
        self.assertFalse(es_inicio_de_turno(j, col))


class test_hay_conejo_en_tablero(unittest.TestCase):
    def test_hay_conejo_dorado(self):
        j = Juego(tablero_8x8_ya_finalizando(),DORADO,0)
        col = DORADO
        self.assertTrue(hay_conejo_en_tablero(j, col))

    def test_no_hay_conejos(self):
        j = Juego(tablero_8x8_vacio(),DORADO,0)
        col = DORADO
        self.assertFalse(hay_conejo_en_tablero(j, col))


if __name__ == "__main__":
    unittest.main(verbosity=2)
