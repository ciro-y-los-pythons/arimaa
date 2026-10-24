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

if __name__ == "__main__":
    unittest.main(verbosity=2)
