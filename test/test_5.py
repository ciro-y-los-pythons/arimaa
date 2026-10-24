import unittest


import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] 
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from arimaa import *

from test.ejemplos.tableros import (
    tablero_8x8_inicial_ejemplo,
    tablero_8x8_vacio,
    tablero_mal_formado_columnas_ejemplo,
    tablero_mal_formado_filas_ejemplo,
    tablero_8x8_inicial_falta_un_conejo_dorado_en_h2
)

class test_tableros_coinciden_en_la_posicion(unittest.TestCase):
    def test_coinciden(self):
        t1 = tablero_8x8_inicial_ejemplo()
        t2 = tablero_8x8_inicial_ejemplo()
        pos = Posicion(0,0)
        self.assertTrue(tableros_coinciden_en_la_posicion(t1,t2, pos))
    def test_no_coinciden(self):
        t1 = tablero_8x8_inicial_ejemplo()
        t2 = tablero_8x8_vacio()
        pos = Posicion(0,0)
        self.assertFalse(tableros_coinciden_en_la_posicion(t1,t2, pos))


class test_tableros_coinciden_salvo_en_la_posicion(unittest.TestCase):
    def test_coinciden_salvo_en_una_posicion(self):
        t1 = tablero_8x8_inicial_ejemplo()
        t2 = tablero_8x8_inicial_falta_un_conejo_dorado_en_h2()
        pos = Posicion(1,7)
        self.assertTrue(tableros_coinciden_salvo_en_la_posicion(t1,t2, pos))
    def test_coinciden_en_todas_las_posiciones(self):
        t1 = tablero_8x8_inicial_ejemplo()
        t2 = tablero_8x8_inicial_ejemplo()
        pos = Posicion(0,0) #Indistinto, porque coinciden en todas las pos
        self.assertFalse(tableros_coinciden_salvo_en_la_posicion(t1,t2, pos))

if __name__ == "__main__":
    unittest.main(verbosity=2)
