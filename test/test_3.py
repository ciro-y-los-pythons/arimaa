import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from src.arimaa import *
from test.ejemplos.tableros import *


class test_hay_casilla_vacia_hacia(unittest.TestCase):
    def test_hay_casilla_vacia_hacia(self):
        t = tablero_8x8_empezando()
        pos = Posicion(0, 0)
        self.assertTrue(hay_casilla_vacia_hacia(t, pos, NORTE))
    def test_no_hay_casilla_vacia_hacia(self):
        t = tablero_8x8_empezando()
        pos = Posicion(2, 0)
        self.assertFalse(hay_casilla_vacia_hacia(t, pos, NORTE))


class test_hay_pieza(unittest.TestCase):
    def test_hay_pieza(self):
        t = tablero_8x8_inicial_ejemplo()
        pos = Posicion(0, 0)
        self.assertTrue(hay_pieza(t, pos))
    def test_no_hay_pieza(self):
        t = tablero_8x8_inicial_ejemplo()
        pos = Posicion(2, 2)
        self.assertFalse(hay_pieza(t, pos))


class test_hay_pieza_amiga_vecina(unittest.TestCase):
    def test_hay_pieza_amiga_vecina(self):
        t = tablero_8x8_ya_empezado()
        pos = Posicion(2, 5)
        self.assertTrue(hay_pieza_amiga_vecina(t, pos))
    def test_no_hay_pieza_amiga_vecina(self):
        t = tablero_8x8_ya_empezado()
        pos = Posicion(7, 0)
        self.assertFalse(hay_pieza_amiga_vecina(t, pos))


class test_hay_pieza_enemiga_mas_debil_hacia(unittest.TestCase):
    def test_hay_pieza_enemiga_mas_debil_hacia(self):
        t = tablero_8x8_ya_empezado()
        pos = Posicion(4, 5)
        self.assertTrue(hay_pieza_enemiga_mas_debil_hacia(t, pos, SUR))
    def test_no_hay_pieza_enemiga_mas_debil_hacia(self):
        t = tablero_8x8_ya_empezado()
        pos = Posicion(3, 5)
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, pos, NORTE))
    def test_hay_pieza_enemiga_igual_de_fuerte_hacia(self):
        t = tablero_8x8_ya_empezado()
        pos = Posicion(5, 3)
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, pos, OESTE))


class test_hay_pieza_enemiga_mas_fuerte_hacia(unittest.TestCase):
    def test_hay_pieza_enemiga_mas_fuerza_hacia(self):
        t = tablero_8x8_ya_finalizando()
        pos = Posicion(3, 4)
        d = NORTE
        pos_norte = posicion_vecina_hacia(pos, d)
        self.assertTrue(hay_pieza(t, pos))
        self.assertTrue(hay_pieza(t, pos_norte))
        self.assertEqual(pos_norte, Posicion(4, 4))
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


class test_hay_pieza_enemiga_mas_fuerte_vecina(unittest.TestCase):
    def test_hay_pieza_enemiga_mas_fuerte_vecina(self):
        t = tablero_8x8_ya_finalizando()
        pos = Posicion(3, 4)
        d = NORTE
        pos_norte = posicion_vecina_hacia(pos, d)
        self.assertTrue(hay_pieza(t, pos))
        self.assertTrue(hay_pieza(t, pos_norte))
        self.assertEqual(pos_norte, Posicion(4, 4))
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, pos))
    def test_no_hay_pieza_enemiga_vecina(self):
        t = tablero_8x8_empezando()
        pos = Posicion(3, 0)
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(t, pos))
    def test_hay_pieza_enemiga_vecina_de_misma_fuerza(self):
        t = tablero_8x8_empezando()
        pos = Posicion(3, 3)
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(t, pos))
    def test_hay_pieza_enemiga_vecina_de_menor_fuerza(self):
        t = tablero_8x8_ya_empezado()
        pos = Posicion(1, 4)
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(t, pos))


class test_hay_pieza_congelada(unittest.TestCase):
    def test_hay_pieza_congelada(self):
        t = leer_tablero(
            [
                "--d--H-D",  # 7
                "-hMc--r-",  # 6
                "--r--C-H",  # 5
                "--------",  # 4
                "-CeD----",  # 3
                "---R----",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        self.assertTrue(hay_pieza_congelada(t, Posicion(6, 1)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
