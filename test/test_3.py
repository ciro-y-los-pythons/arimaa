import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from src.arimaa import *
from test.ejemplos.tableros import *


class test_hay_pieza(unittest.TestCase):
    def test_hay_pieza(self):
        t = tablero_8x8_inicial_ejemplo()
        pos = Posicion(0, 0)
        self.assertTrue(hay_pieza(t, pos))

    def test_no_hay_pieza(self):
        t = tablero_8x8_inicial_ejemplo()
        pos = Posicion(2, 2)
        self.assertFalse(hay_pieza(t, pos))


class test_hay_pieza_enemiga_mas_fuerte_hacia(unittest.TestCase):
    def test_hay_pieza_enemiga_mas_fuerza_hacia(self):
        t = tablero_8x8_ya_finalizando()
        pos = Posicion(3, 4)
        d = NORTE
        self.assertTrue(hay_pieza(t, pos))
        self.assertTrue(hay_pieza(t, posicion_vecina_hacia(pos, d)))
        self.assertEqual(posicion_vecina_hacia(pos, d), Posicion(4, 4))
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_hacia(t, pos, d))

    def test_no_hay_pieza_enemiga_hacia(self):
        t = tablero_8x8_empezando()
        pos = Posicion(3, 0)
        d = NORTE
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_hacia(t, pos, d))

    def test_hay_pieza_enemiga_de_misma_fuerza_hacia(self):
        t = tablero_8x8_empezando()
        pos = Posicion(3, 3)
        d = NORTE
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_hacia(t, pos, d))

    def test_exception_no_hay_pieza_propia(self):
        t = tablero_8x8_ya_finalizando()
        pos = Posicion(1, 1)
        d = NORTE
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_hacia(t, pos, d))


if __name__ == "__main__":
    unittest.main(verbosity=2)
