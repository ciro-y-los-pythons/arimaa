import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from src.arimaa import *
from test.ejemplos.tableros import tablero_8x8_inicial_ejemplo


class test_hay_pieza(unittest.TestCase):
    def test_hay_pieza(self):
        t = tablero_8x8_inicial_ejemplo()
        pos = Posicion(0, 0)
        self.assertTrue(hay_pieza(t, pos))

    def test_no_hay_pieza(self):
        t = tablero_8x8_inicial_ejemplo()
        pos = Posicion(2, 2)
        self.assertFalse(hay_pieza(t, pos))


if __name__ == "__main__":
    unittest.main(verbosity=2)
