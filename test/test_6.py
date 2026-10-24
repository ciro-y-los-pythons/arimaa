import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] 
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from src.arimaa import *

from test.ejemplos.tableros import *

class test_es_tablero_poniendo_pieza(unittest.TestCase):
    def test_se_agrega_pieza(self):
        t0 = tablero_8x8_inicial_falta_un_conejo_dorado_en_h2()
        t1 = tablero_8x8_inicial_ejemplo()
        pos = Posicion(1,7)
        f = CONEJO
        col = DORADO
        self.assertTrue(es_tablero_poniendo_pieza(t0,t1,pos,f,col))
    def test_se_cambia_pieza(self):
        t0 = tablero_8x8_ya_finalizando()
        t1 = tablero_8x8_ya_finalizando_v2()
        pos = Posicion(5,1)
        f = CABALLO
        col = DORADO
        self.assertTrue(es_tablero_poniendo_pieza(t0,t1,pos,f,col))
    def test_no_coinciden_las_piezas(self):
        # Se "agrega" un conejo dorado en t1, pero se quiere verificar por parametro un perro plateado
        t0 = tablero_8x8_inicial_falta_un_conejo_dorado_en_h2()
        t1 = tablero_8x8_inicial_ejemplo()
        pos = Posicion(1,7)
        f = PERRO
        col = PLATEADO
        self.assertFalse(es_tablero_poniendo_pieza(t0,t1,pos,f,col))
    def test_son_tableros_iguales(self):
        t1 = tablero_8x8_inicial_ejemplo()
        t2 = tablero_8x8_inicial_ejemplo()
        pos = Posicion(0,0)
        f = CABALLO
        col = DORADO
        self.assertFalse(es_tablero_poniendo_pieza(t1,t2,pos,f,col))


class test_es_tablero_trasladando_pieza(unittest.TestCase):
    def test_mueve_conejo_dorado_h2_a_h3(self):
        t0 = tablero_8x8_inicial_ejemplo()
        t1 = tablero_8x8_mueve_conejo_dorado_h3()
        pos_origen = Posicion(1,7)
        pos_destino = Posicion(2,7)
        self.assertTrue(es_tablero_trasladando_pieza(t0,t1,pos_origen,pos_destino))
    def test_quita_y_no_mueve(self):
        t0 = tablero_8x8_inicial_ejemplo()
        t1 = tablero_8x8_inicial_falta_un_conejo_dorado_en_h2()
        pos_origen = Posicion(1,7)
        pos_destino = Posicion(2,7)
        self.assertFalse(es_tablero_trasladando_pieza(t0,t1,pos_origen,pos_destino))
    def test_no_hay_pieza_origen(self):
        t0 = tablero_8x8_inicial_falta_un_conejo_dorado_en_h2()
        t1 = tablero_8x8_mueve_conejo_dorado_h3()
        pos_origen = Posicion(1,7)
        pos_destino = Posicion(2,7)
        self.assertFalse(es_tablero_trasladando_pieza(t0,t1,pos_origen,pos_destino))

if __name__ == "__main__":
    unittest.main(verbosity=2)
