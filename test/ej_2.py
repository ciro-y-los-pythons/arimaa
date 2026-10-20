import unittest

from src.arimaa import *
from test.ejemplos.tableros import tablero_8x8_inicial_ejemplo

# class test_posicion_vecina_hacia(unittest.TestCase):
#     def test_vecina_al_norte(self):
#         self.assertEqual(posicion_vecina_hacia(Posicion(0, 0), NORTE), Posicion(1, 0))


# class test_son_posiciones_vecinas(unittest.TestCase):
#     def test_vecinas(self):
#         self.assertTrue(son_posiciones_vecinas(Posicion(0, 0), Posicion(1, 0)))


# class test_casilla_en_posicion(unittest.TestCase):
#     def test_casilla_en_posicion(self):
#         t = tablero_8x8_inicial_ejemplo()
#         self.assertEqual(casilla_en_posicion(t, Posicion(0, 0)), Pieza(CABALLO, DORADO))


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


# class test_hay_pieza_de_color(unittest.TestCase):
#     def test_hay_pieza_de_color_ok(self):
#         t = tablero_8x8_inicial_ejemplo()
#         self.assertTrue(hay_pieza_de_color(t, Posicion(1, 4), DORADO))


if __name__ == "__main__":
    unittest.main(verbosity=2)
