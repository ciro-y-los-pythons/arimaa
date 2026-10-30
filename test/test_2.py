import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from src.arimaa import *
from test.ejemplos.tableros import tablero_8x8_inicial_ejemplo


class test_posicion_vecina_hacia(unittest.TestCase):
    def test_sur(self):
        pos = Posicion(fila=5, columna=3)
        res = posicion_vecina_hacia(pos, SUR)
        self.assertEqual(res, Posicion(fila=4, columna=3))
    def test_norte(self):
        pos = Posicion(fila=5, columna=3)
        res = posicion_vecina_hacia(pos, NORTE)
        self.assertEqual(res, Posicion(fila=6, columna=3))
    def test_este(self):
        pos = Posicion(fila=5, columna=3)
        res = posicion_vecina_hacia(pos, ESTE)
        self.assertEqual(res, Posicion(fila=5, columna=4))
    def test_oeste(self):
        pos = Posicion(fila=5, columna=3)
        res = posicion_vecina_hacia(pos, OESTE)
        self.assertEqual(res, Posicion(fila=5, columna=2))


class test_son_posiciones_vecinas(unittest.TestCase):
    def test_vecinas_misma_fila(self):
        self.assertTrue(son_posiciones_vecinas(Posicion(0, 0), Posicion(0, 1)))
    def test_vecinas_misma_columna(self):
        self.assertTrue(son_posiciones_vecinas(Posicion(0, 0), Posicion(1, 0)))
    def test_misma_fila_no_vecinas(self):
        self.assertFalse(son_posiciones_vecinas(Posicion(0, 0), Posicion(0, 2)))
    def test_misma_columna_no_vecinas(self):
        self.assertFalse(son_posiciones_vecinas(Posicion(0, 0), Posicion(2, 0)))
    def test_diagonal_no_vecinas(self):
        self.assertFalse(son_posiciones_vecinas(Posicion(0, 0), Posicion(1, 1)))
    def test_misma_posicion_no_vecinas(self):
        self.assertFalse(son_posiciones_vecinas(Posicion(0, 0), Posicion(0, 0)))


class test_casilla_en_posicion(unittest.TestCase):
    def test_casilla_en_posicion(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertEqual(casilla_en_posicion(t, Posicion(0, 0)), Pieza(CABALLO, DORADO))


class test_hay_casilla_vacia(unittest.TestCase):
    """
    Requiere: {tablero_bien_formado(t) ∧ posicion_en_tablero(pos)}
    Por lo tanto no se evalúa cuando la posición no es válida ni el tablero esta mal formado.
    """
    def test_casilla_vacia(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_casilla_vacia(t, Posicion(2, 1)))
    def test_casilla_no_vacia(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_casilla_vacia(t, Posicion(0, 0)))


class test_hay_figura_de_color(unittest.TestCase):
    def test_posicion_invalida(self):
        t = tablero_8x8_inicial_ejemplo()
        pos = Posicion(8, 8)
        f = CABALLO
        col = DORADO
        self.assertFalse(hay_figura_de_color(t, pos, f, col))
    def test_casilla_vacia(self):
        t = tablero_8x8_inicial_ejemplo()
        pos = Posicion(2, 2)
        f = CABALLO
        col = DORADO
        self.assertFalse(hay_figura_de_color(t, pos, f, col))
    def test_diferente_color(self):
        t = tablero_8x8_inicial_ejemplo()
        pos = Posicion(7, 0)
        f = CABALLO
        col = DORADO
        self.assertFalse(hay_figura_de_color(t, pos, f, col))
    def test_diferente_figura(self):
        t = tablero_8x8_inicial_ejemplo()
        pos = Posicion(0, 0)
        f = GATO
        col = DORADO
        self.assertFalse(hay_figura_de_color(t, pos, f, col))
    def test_diferente_pieza(self):
        t = tablero_8x8_inicial_ejemplo()
        pos = Posicion(7, 1)
        f = CABALLO
        col = DORADO
        self.assertFalse(hay_figura_de_color(t, pos, f, col))
    def test_misma_pieza(self):
        t = tablero_8x8_inicial_ejemplo()
        pos = Posicion(0, 0)
        f = CABALLO
        col = DORADO
        self.assertTrue(hay_figura_de_color(t, pos, f, col))


class test_hay_pieza_de_color(unittest.TestCase):
    def test_hay_pieza_de_color_ok(self):
        t = tablero_8x8_inicial_ejemplo()
        pos = Posicion(1, 4)
        self.assertTrue(hay_pieza_de_color(t, pos, DORADO))
    def test_no_hay_pieza_del_color(self):
        t = tablero_8x8_inicial_ejemplo()
        pos = Posicion(5, 1)
        self.assertFalse(hay_pieza_de_color(t, pos, PLATEADO))


if __name__ == "__main__":
    unittest.main(verbosity=2)
