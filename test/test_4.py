import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from src.arimaa import *
from test.ejemplos.tableros import *

class test_direccion_de_movimiento_habilitada(unittest.TestCase):
    def test_conejo_dorado_puede_mover_al_norte(self):
        t = tablero_8x8_inicial_ejemplo()
        pos = Posicion(1,3)
        d = NORTE
        self.assertTrue(direccion_de_movimiento_habilitada(t,pos,d))

    def test_conejo_plateado_puede_mover_al_sur(self):
        t = tablero_8x8_inicial_ejemplo()
        pos = Posicion(6,3)
        d = SUR
        self.assertTrue(direccion_de_movimiento_habilitada(t,pos,d))
    
    def test_conejo_dorado_no_puede_mover_al_sur(self):
        t = tablero_8x8_inicial_ejemplo()
        pos = Posicion(1,3)
        d = SUR
        self.assertFalse(direccion_de_movimiento_habilitada(t,pos,d))

    def test_conejo_plateado_no_puede_mover_al_norte(self):
        t = tablero_8x8_inicial_ejemplo()
        pos = Posicion(6,3)
        d = NORTE
        self.assertFalse(direccion_de_movimiento_habilitada(t,pos,d))

    def test_no_es_conejo_y_puede_mover(self):
        t = tablero_8x8_ya_finalizando_v2()
        pos = Posicion(5,1)
        d = NORTE
        self.assertTrue(direccion_de_movimiento_habilitada(t,pos,d))
    
    def test_no_existe_pieza_en_posicion(self):
        t = tablero_8x8_inicial_ejemplo()
        pos = Posicion(4,5)
        d = NORTE
        self.assertFalse(direccion_de_movimiento_habilitada(t,pos,d))


class test_puede_mover_a_secas(unittest.TestCase):
    def test_casilla_esta_vacia(self):
        t = tablero_8x8_inicial_ejemplo()
        pos = Posicion(1,4)
        d = NORTE
        self.assertTrue(puede_mover_a_secas(t,pos,d))

    def test_casilla_no_esta_vacia(self):
        t = tablero_8x8_inicial_ejemplo()
        pos = Posicion(0,0)
        d = NORTE
        self.assertFalse(puede_mover_a_secas(t,pos,d))


if __name__ == "__main__":
    unittest.main(verbosity=2)
