import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from src.arimaa import *
from test.ejemplos.tableros import *


# TEST #27 - Problema
class test_activar_trampas(unittest.TestCase):
    def test_activar_trampas_ok(self):
        t0 = leer_tablero(
            [
                "-eRD--rd",  # 7
                "--------",  # 6
                "H-r--E--",  # 5
                "-H--r-Cr",  # 4
                "R-------",  # 3
                "R-H--m--",  # 2
                "R-------",  # 1
                "c-D---R-",  # 0
                # 01234567
            ]
        )
        t1 = leer_tablero(
            [
                "-eRD--rd",  # 7
                "--------",  # 6
                "H-------",  # 5
                "-H--r-Cr",  # 4
                "R-------",  # 3
                "R-------",  # 2
                "R-------",  # 1
                "c-D---R-",  # 0
                # 01234567
            ]
        )
        t2 = activar_trampas(t0)
        self.assertNotEqual(t0, t1)
        self.assertEqual(t2, t1)
        self.assertTrue(tablero_bien_formado(t2))
        self.assertTrue(es_tablero_despues_de_activar_todas_las_trampas(t0,t2))

    def test_no_hay_piezas_en_trampa(self):
        t0 = tablero_8x8_inicial_ejemplo()
        t1 = tablero_8x8_inicial_ejemplo()
        t2 = activar_trampas(t0)
        self.assertEqual(t0,t1)
        self.assertEqual(t2,t1)
        self.assertTrue(tablero_bien_formado(t2))
        self.assertTrue(es_tablero_despues_de_activar_todas_las_trampas(t0,t2))

    def test_todas_tienen_amiga_vecina(self):
        t0 = tablero_8x8_piezas_en_todas_las_trampas_pero_con_amigas()
        t1 = tablero_8x8_piezas_en_todas_las_trampas_pero_con_amigas()
        t2 = activar_trampas(t0)
        self.assertEqual(t0,t1)
        self.assertEqual(t2,t1)
        self.assertTrue(tablero_bien_formado(t2))
        self.assertTrue(es_tablero_despues_de_activar_todas_las_trampas(t0,t2))

    def test_piezas_en_todas_las_trampas_sin_amigas(self):
        t0 = tablero_8x8_piezas_en_todas_las_trampas_sin_amigas_1()
        t1 = tablero_8x8_piezas_en_todas_las_trampas_sin_amigas_2()
        t2 = activar_trampas(t0)
        self.assertNotEqual(t0,t1)
        self.assertEqual(t2,t1)
        self.assertTrue(tablero_bien_formado(t2))
        self.assertTrue(es_tablero_despues_de_activar_todas_las_trampas(t0,t2))

    def test_una_sola_pieza_en_trampa(self):
        t0 = tablero_8x8_gato_plateado_en_trampa()
        t1 = tablero_8x8_gato_plateado_en_trampa_quitado()
        t2 = activar_trampas(t0)
        self.assertNotEqual(t0,t1)
        self.assertEqual(t2,t1)
        self.assertTrue(tablero_bien_formado(t2))
        self.assertTrue(es_tablero_despues_de_activar_todas_las_trampas(t0,t2))

# TEST #23 - Auxiliar
class test_tableros_coinciden_en_la_posicion(unittest.TestCase):
    def test_coinciden(self):
        t1 = tablero_8x8_inicial_ejemplo()
        t2 = tablero_8x8_inicial_ejemplo()
        pos = Posicion(0, 0)
        self.assertTrue(tableros_coinciden_en_la_posicion(t1, t2, pos))
    def test_no_coinciden(self):
        t1 = tablero_8x8_inicial_ejemplo()
        t2 = tablero_8x8_vacio()
        pos = Posicion(0, 0)
        self.assertFalse(tableros_coinciden_en_la_posicion(t1, t2, pos))

# TEST #24 - Auxiliar
class test_tableros_coinciden_salvo_en_la_posicion(unittest.TestCase):
    def test_coinciden_salvo_en_una_posicion(self):
        t1 = tablero_8x8_inicial_ejemplo()
        t2 = tablero_8x8_inicial_falta_un_conejo_dorado_en_h2()
        pos = Posicion(1,7)
        self.assertTrue(tableros_coinciden_salvo_en_la_posicion(t1,t2, pos))
    def test_coinciden_en_todas_las_posiciones(self):
        t1 = tablero_8x8_inicial_ejemplo()
        t2 = tablero_8x8_inicial_ejemplo()
        pos = Posicion(0, 0) # Indistinto, porque coinciden en todas las pos
        self.assertFalse(tableros_coinciden_salvo_en_la_posicion(t1, t2, pos))

# TEST #25 - Auxiliar
class test_es_tablero_sacando_pieza(unittest.TestCase):
    def test_es_tablero_sacando_una_pieza_en_pos(self):
        t0 = tablero_8x8_inicial_ejemplo()
        t1 = tablero_8x8_inicial_falta_un_conejo_dorado_en_h2()
        pos = Posicion(1,7)
        self.assertTrue(es_tablero_sacando_pieza(t0,t1, pos))
    def test_es_tablero_distinto_valor_pero_no_vacia(self):
        t0 = tablero_8x8_ya_finalizando()
        t1 = tablero_8x8_ya_finalizando_v2()
        pos = Posicion(5,1)
        self.assertFalse(es_tablero_sacando_pieza(t0,t1, pos))
    def test_es_tablero_ambos_iguales(self):
        t0 = tablero_8x8_inicial_ejemplo()
        t1 = tablero_8x8_inicial_ejemplo()
        pos = Posicion(0,0) # Cualquier pos evaluada da False porque son iguales
        self.assertFalse(es_tablero_sacando_pieza(t0,t1, pos))
    def test_quitando_todas_las_piezas(self):
        t0 = tablero_8x8_inicial_ejemplo()
        t1 = tablero_8x8_vacio()
        pos = Posicion(0,0) # Cualquier pos evaluada da False porque son iguales
        self.assertFalse(tableros_coinciden_salvo_en_la_posicion(t0,t1, pos))

# TEST #26A - Auxiliar
class test_es_tablero_despues_de_activar_trampa(unittest.TestCase):
    def test_hay_amiga_y_tableros_iguales(self):
        t0 = tablero_8x8_ya_empezado()
        t1 = tablero_8x8_ya_empezado()
        pos_trampa = Posicion(2,5)
        self.assertTrue(es_tablero_despues_de_activar_trampa(t0,t1, pos_trampa))

    def test_hay_amiga_y_tableros_distintos(self):
        t0 = tablero_8x8_ya_empezado()
        t1 = tablero_8x8_ya_empezado_mueve_camello_plateado_a4()
        pos_trampa = Posicion(2,5)
        self.assertFalse(es_tablero_despues_de_activar_trampa(t0,t1, pos_trampa))

    def test_no_hay_amiga_y_se_quita_pieza(self):
        t0 = tablero_8x8_gato_plateado_en_trampa()
        t1 = tablero_8x8_gato_plateado_en_trampa_quitado()
        pos_trampa = Posicion(2,5)
        self.assertTrue(es_tablero_despues_de_activar_trampa(t0,t1, pos_trampa))

    def test_no_hay_amiga_y_no_Se_quita_pieza(self):
        t0 = tablero_8x8_gato_plateado_en_trampa()
        t1 = tablero_8x8_gato_plateado_en_trampa()
        pos_trampa = Posicion(2,5)
        self.assertFalse(es_tablero_despues_de_activar_trampa(t0,t1, pos_trampa))

# TEST #26B - Auxiliar
class test_es_tablero_despues_de_activar_todas_las_trampas(unittest.TestCase):
    def test_no_hay_piezas_en_trampa_tableros_correctos(self):
        t0 = tablero_8x8_gato_plateado_en_trampa_quitado()
        t1 = tablero_8x8_gato_plateado_en_trampa_quitado()
        self.assertTrue(es_tablero_despues_de_activar_todas_las_trampas(t0,t1))

    def test_no_hay_piezas_en_trampa_tableros_incorrectos(self):
        t0 = tablero_8x8_gato_plateado_en_trampa_quitado()
        t1 = tablero_8x8_gato_plateado_en_trampa()
        self.assertFalse(es_tablero_despues_de_activar_todas_las_trampas(t0,t1))

    def test_todas_tienen_amiga_vecina_y_tableros_iguales(self):
        t0 = tablero_8x8_piezas_en_todas_las_trampas_pero_con_amigas()
        t1 = tablero_8x8_piezas_en_todas_las_trampas_pero_con_amigas()
        self.assertTrue(es_tablero_despues_de_activar_todas_las_trampas(t0,t1))

    def test_piezas_en_todas_las_trampas_sin_amigas_y_activa_todas_las_trampas(self):
        t0 = tablero_8x8_piezas_en_todas_las_trampas_sin_amigas_1()
        t1 = tablero_8x8_piezas_en_todas_las_trampas_sin_amigas_2()
        self.assertTrue(es_tablero_despues_de_activar_todas_las_trampas(t0,t1))

    def test_piezas_en_todas_las_trampas_sin_amigas_y_no_activa_trampas(self):
        t0 = tablero_8x8_piezas_en_todas_las_trampas_sin_amigas_1()
        t1 = tablero_8x8_piezas_en_todas_las_trampas_sin_amigas_1()
        self.assertFalse(es_tablero_despues_de_activar_todas_las_trampas(t0,t1))

    def test_una_sola_pieza_en_trampa_y_se_activa(self):
        t0 = tablero_8x8_gato_plateado_en_trampa()
        t1 = tablero_8x8_gato_plateado_en_trampa_quitado()
        self.assertTrue(es_tablero_despues_de_activar_todas_las_trampas(t0,t1))

    def test_una_sola_pieza_en_trampa_y_no_se_activa(self):
        t0 = tablero_8x8_gato_plateado_en_trampa()
        t1 = tablero_8x8_gato_plateado_en_trampa()
        self.assertFalse(es_tablero_despues_de_activar_todas_las_trampas(t0,t1))


if __name__ == "__main__":
    unittest.main(verbosity=2)
