import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from src.arimaa import *
from test.ejemplos.tableros import *


# TEST #17 - Auxiliar
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

# TEST #18 - Auxiliar
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

# TEST #19 - Auxiliar
class test_puede_arrastrar(unittest.TestCase):
    def test_puede_arrastrar_ok(self):
        t = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "--------",  # 5
                "----E---",  # 4
                "----r---",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        pos = Posicion(4,4)
        d = NORTE
        d_arrastre = NORTE
        self.assertTrue(puede_arrastrar(t,pos,d,d_arrastre))
    def test_casilla_destino_ocupada(self):
        t = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "----c---",  # 5
                "----E---",  # 4
                "----r---",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        pos = Posicion(4,4)
        d = NORTE
        d_arrastre = NORTE
        self.assertFalse(puede_arrastrar(t,pos,d,d_arrastre))
    def test_pieza_es_amiga_no_enemiga(self):
        t = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "--------",  # 5
                "----E---",  # 4
                "----R---",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        pos = Posicion(4,4)
        d = NORTE
        d_arrastre = NORTE
        self.assertFalse(puede_arrastrar(t,pos,d,d_arrastre))
    def test_enemigo_es_mas_fuerte_o_igual(self):
        t = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "--------",  # 5
                "----D---",  # 4
                "----m---",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        pos = Posicion(4,4)
        d = NORTE
        d_arrastre = NORTE
        self.assertFalse(puede_arrastrar(t,pos,d,d_arrastre))
    def test_no_hay_pieza_en_direccion_de_arrastre(self):
        t = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "--------",  # 5
                "----E---",  # 4
                "--------",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        pos = Posicion(4,4)
        d = NORTE
        d_arrastre = NORTE
        self.assertFalse(puede_arrastrar(t,pos,d,d_arrastre))

# TEST #20 - Auxiliar
class test_puede_empujar(unittest.TestCase):
    def test_puede_empujar_ok(self):
        t = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "----r---",  # 5
                "----E---",  # 4
                "--------",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        pos = Posicion(4,4)
        d = NORTE
        d_empuje = ESTE
        self.assertTrue(puede_empujar(t,pos,d,d_empuje))
    def test_casilla_destino_ocupada(self):
        t = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "----rc--",  # 5
                "----E---",  # 4
                "--------",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        pos = Posicion(4,4)
        d = NORTE
        d_empuje = ESTE
        self.assertFalse(puede_empujar(t,pos,d,d_empuje))
    def test_pieza_es_amiga(self):
        t = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "----R---",  # 5
                "----E---",  # 4
                "--------",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        pos = Posicion(4,4)
        d = NORTE
        d_empuje = ESTE
        self.assertFalse(puede_empujar(t,pos,d,d_empuje))
    def test_enemigo_mas_fuerte_o_igual(self):
        t = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "----m---",  # 5
                "----D---",  # 4
                "--------",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        pos = Posicion(4,4)
        d = NORTE
        d_empuje = ESTE
        self.assertFalse(puede_empujar(t,pos,d,d_empuje))
    def test_no_hay_pieza_para_empujar(self):
        t = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "--------",  # 5
                "----E---",  # 4
                "--------",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        pos = Posicion(4,4)
        d = NORTE
        d_empuje = ESTE
        self.assertFalse(puede_empujar(t,pos,d,d_empuje))

# TEST #21 - Auxiliar
class test_puede_realizar_accion(unittest.TestCase):
    """
    Requiere: {tablero_bien_formado(t) ∧ movimiento_bien_formado(m)}
    Por lo tanto no se evalúa cuando el tablero o el movimiento están mal formados.
    """
    def test_puede_mover_a_secas(self):
        t = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "--------",  # 5
                "----E---",  # 4
                "--------",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        m = Movimiento(MOVER_A_SECAS,Posicion(4,4),[NORTE])
        self.assertTrue(puede_realizar_accion(t,m))
    def test_no_puede_mover_a_secas(self):
        t = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "----c---",  # 5
                "----E---",  # 4
                "--------",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        m = Movimiento(MOVER_A_SECAS,Posicion(4,4),[NORTE])
        self.assertFalse(puede_realizar_accion(t,m))
    def test_puede_arrastrar(self):
        t = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "--------",  # 5
                "----E---",  # 4
                "----r---",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        m = Movimiento(ARRASTRAR,Posicion(4,4),[NORTE,NORTE])
        self.assertTrue(puede_realizar_accion(t,m))
    def test_puede_empujar(self):
        t = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "----r---",  # 5
                "----E---",  # 4
                "--------",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        m = Movimiento(EMPUJAR,Posicion(4,4),[NORTE,ESTE])
        self.assertTrue(puede_realizar_accion(t,m))
    def test_no_puede_empujar(self):
        t = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "----rc--",  # 5
                "----E---",  # 4
                "--------",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        m = Movimiento(EMPUJAR,Posicion(4,4),[NORTE,ESTE])
        self.assertFalse(puede_realizar_accion(t,m))

# TEST #22 - Problema
class test_puede_realizar_movimiento(unittest.TestCase):
    """
    Requiere: {juego_bien_formado(j) ∧ movimiento_bien_formado(m)}
    Por lo tanto no se evalúa cuando el juego o el movimiento están mal formados.
    """
    def test_movimiento_todo_ok(self):
        t = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "--------",  # 5
                "----E---",  # 4
                "--------",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        j = Juego(t,DORADO,0)
        m = Movimiento(MOVER_A_SECAS,Posicion(4,4),[NORTE])
        self.assertTrue(puede_realizar_movimiento(j,m))
    def test_pieza_no_es_del_color_del_turno(self):
        t = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "--------",  # 5
                "----E---",  # 4
                "--------",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        j = Juego(t,PLATEADO,0)
        m = Movimiento(MOVER_A_SECAS,Posicion(4,4),[NORTE])
        self.assertFalse(puede_realizar_movimiento(j,m))
    def test_pieza_congelada(self):
        t = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "--------",  # 5
                "----d---",  # 4
                "----R---",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        j = Juego(t,DORADO,0)
        m = Movimiento(MOVER_A_SECAS,Posicion(4,3),[SUR])
        self.assertFalse(puede_realizar_movimiento(j,m))
    def test_direccion_no_habilitada(self):
        t = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "--------",  # 5
                "----R---",  # 4
                "--------",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        j = Juego(t,DORADO,0)
        m = Movimiento(MOVER_A_SECAS,Posicion(4,4),[SUR])
        self.assertFalse(puede_realizar_movimiento(j,m))
    def test_supera_limite_de_pasos(self):
        t = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "--------",  # 5
                "----E---",  # 4
                "----r---",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        j = Juego(t,DORADO,3)
        m = Movimiento(ARRASTRAR,Posicion(4,4),[NORTE,NORTE])
        self.assertFalse(puede_realizar_movimiento(j,m))
    def test_accion_no_valida(self):
        t = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "----H---",  # 5
                "----E---",  # 4
                "--------",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        j = Juego(t,DORADO,0)
        m = Movimiento(MOVER_A_SECAS,Posicion(4,4),[NORTE])
        self.assertFalse(puede_realizar_movimiento(j,m))


if __name__ == "__main__":
    unittest.main(verbosity=2)
