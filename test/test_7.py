import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from src.arimaa import *
from test.ejemplos.tableros import *


# TEST #46 - Auxiliar
class test_ganador_del_juego(unittest.TestCase):
    def test_ganador_es_dorado(self):
        t = tablero_8x8_ya_empezado()
        j = Juego(t,DORADO,0)
        self.assertEqual(ganador_del_juego(j), DORADO)
    def test_ganador_es_plateado(self):
        t = tablero_8x8_sin_conejos_dorados()
        j = Juego(t,PLATEADO,0)
        self.assertEqual(ganador_del_juego(j),PLATEADO)
    def test_promueve_conejo_dorado_turno_del_oponente(self):
        t = leer_tablero(
            [
                "rr----Rr",  # 7
                "c-----me",  # 6
                "---Ed-R-",  # 5
                "-M---R--",  # 4
                "---R----",  # 3
                "-rrrr---",  # 2
                "-H---DCC",  # 1
                "R-----RR",  # 0
                # 01234567
            ]
        )
        j = Juego(t, PLATEADO, 0)
        self.assertTrue(hay_ganador_determinado(j))
        self.assertEqual(ganador_del_juego(j), DORADO)

# TEST #38 - Auxiliar
class test_es_inicio_de_turno(unittest.TestCase):
    def test_inicio_de_juego(self):
        j = Juego(tablero_8x8_inicial_ejemplo(),DORADO,0)
        col = DORADO
        self.assertTrue(es_inicio_de_turno(j, col))

    def test_inicio_de_juego_no_coincide_color(self):
        j = Juego(tablero_8x8_inicial_ejemplo(),DORADO,0)
        col = PLATEADO
        self.assertFalse(es_inicio_de_turno(j, col))

    def test_ya_hay_pasos_consumidos(self):
        j = Juego(tablero_8x8_mueve_conejo_dorado_h3(),DORADO,1)
        col = DORADO
        self.assertFalse(es_inicio_de_turno(j, col))

    def test_ya_hay_pasos_consumidos_y_no_coincide_color(self):
        j = Juego(tablero_8x8_mueve_conejo_dorado_h3(),DORADO,1)
        col = PLATEADO
        self.assertFalse(es_inicio_de_turno(j, col))

# TEST #39 - Auxiliar
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

# TEST #40 - Auxiliar
class test_hay_conejo_en_fila_inicial_oponente(unittest.TestCase):
    def test_hay_conejo_en_fila_inicial_oponente(self):
        j = Juego(tablero_8x8_ya_empezado(), DORADO, 0)
        col = DORADO
        self.assertTrue(hay_conejo_en_fila_inicial_oponente(j, col))

    def test_no_hay_conejo_en_fila_inicial_oponente(self):
        j = Juego(tablero_8x8_inicial_ejemplo(), DORADO, 0)
        col = DORADO
        self.assertFalse(hay_conejo_en_fila_inicial_oponente(j, col))

# TEST #41 - Auxiliar
class test_hay_conejo_en_tablero(unittest.TestCase):
    def test_hay_conejo_dorado(self):
        j = Juego(tablero_8x8_ya_finalizando(),DORADO,0)
        col = DORADO
        self.assertTrue(hay_conejo_en_tablero(j, col))

    def test_no_hay_conejos(self):
        j = Juego(tablero_8x8_vacio(),DORADO,0)
        col = DORADO
        self.assertFalse(hay_conejo_en_tablero(j, col))

# TEST #42 - Auxiliar
class test_reune_condiciones_de_ganar(unittest.TestCase):
    def test_reune_condiciones_de_ganar(self):
        j = Juego(tablero_8x8_ya_empezado(), DORADO, 0)
        col = DORADO
        self.assertTrue(reune_condiciones_de_ganar(j, col))

    def test_no_reune_condiciones_de_ganar(self):
        j = Juego(tablero_8x8_sin_conejos_dorados(), DORADO, 0)
        col = DORADO
        self.assertFalse(reune_condiciones_de_ganar(j, col))

# TEST #43 - Auxiliar
class test_reune_condiciones_de_ganar_exclusivas(unittest.TestCase):
    def test_reune_condiciones_de_ganar_exclusivas(self):
        j = Juego(tablero_8x8_sin_conejos_dorados(), PLATEADO, 0)
        col = PLATEADO
        self.assertTrue(reune_condiciones_de_ganar_exclusivas(j, col))

    def test_ambos_reunen_condiciones_de_ganar(self):
        j = Juego(tablero_8x8_ya_empezado(), DORADO, 0)
        col = DORADO
        self.assertFalse(reune_condiciones_de_ganar_exclusivas(j, col))

    def test_no_reune_condiciones_de_ganar(self):
        j = Juego(tablero_8x8_sin_conejos_dorados(), DORADO, 0)
        col = DORADO
        self.assertFalse(reune_condiciones_de_ganar_exclusivas(j, col))

# TEST #44 - Auxiliar
class test_es_jugador_ganador(unittest.TestCase):
    def test_gana_en_turno_del_oponente(self):
        t = tablero_8x8_sin_conejos_dorados()
        j = Juego(t,DORADO,0)
        col = PLATEADO
        self.assertTrue(es_jugador_ganador(j,col))
    def test_gana_en_turno_propio_exclusivamente(self):
        t = tablero_8x8_sin_conejos_dorados()
        j = Juego(t,PLATEADO,0)
        col = PLATEADO
        self.assertTrue(es_jugador_ganador(j,col))
    def test_no_gana_en_inicio_turno_propio(self):
        t = tablero_8x8_inicial_ejemplo()
        j = Juego(t,DORADO,0)
        col = DORADO
        self.assertFalse(es_jugador_ganador(j,col))
    def test_no_gana_en_inicio_turno_oponente(self):
        t = tablero_8x8_inicial_ejemplo()
        j = Juego(t,DORADO,0)
        col = PLATEADO
        self.assertFalse(es_jugador_ganador(j,col))

# TEST #45 - Problema
class test_hay_ganador_determinado(unittest.TestCase):
    def test_hay_ganador_dorado(self):
        t = tablero_8x8_ya_empezado()
        j = Juego(t,DORADO,0)
        self.assertTrue(hay_ganador_determinado(j))
    def test_hay_ganador_plateado(self):
        t = tablero_8x8_sin_conejos_dorados()
        j = Juego(t,PLATEADO,0)
        self.assertTrue(hay_ganador_determinado(j))
    def test_no_hay_ganador_determinado(self):
        t = tablero_8x8_inicial_ejemplo()
        j = Juego(t,DORADO,0)
        self.assertFalse(hay_ganador_determinado(j))


if __name__ == "__main__":
    unittest.main(verbosity=2)
