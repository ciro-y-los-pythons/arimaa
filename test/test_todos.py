"""
Archivo general de tests (Explota de Exceptions, asique no es muy recomendable ejecutarlo)
Ejecutable con: python3 -m unittest test.todos
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from src.arimaa import *
from test.ejemplos.tableros import *

"""
Las piezas se representan con las siguientes letras:
  E : elefante
  M : camello
  H : caballo
  D : perro
  C : gato
  R : ratón
donde
  mayúscula : dorado
  minúscula : plateado
"""

#### Ejercicio 1


class test_tablero_bien_formado(unittest.TestCase):
    def test_8x8_lleno(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(tablero_bien_formado(t))

    def test_8x8_vacio(self):
        t = tablero_8x8_vacio()
        self.assertTrue(tablero_bien_formado(t))

    def test_8x8_mal_en_fila(self):
        t = tablero_mal_formado_filas_ejemplo()
        self.assertFalse(tablero_bien_formado(t))

    def test_8x8_mal_en_columna(self):
        t = tablero_mal_formado_columnas_ejemplo()
        self.assertFalse(tablero_bien_formado(t))


class test_posicion_en_tablero(unittest.TestCase):
    def test_posicion_valida_minimo(self):
        pos = Posicion(0, 0)
        self.assertTrue(posicion_en_tablero(pos))

    def test_posicion_valida_maximo(self):
        pos = Posicion(7, 7)
        self.assertTrue(posicion_en_tablero(pos))

    def test_posicion_col_pasa_min(self):
        pos = Posicion(1, -1)
        self.assertFalse(posicion_en_tablero(pos))

    def test_posicion_col_pasa_max(self):
        pos = Posicion(1, 8)
        self.assertFalse(posicion_en_tablero(pos))

    def test_posicion_row_pasa_min(self):
        pos = Posicion(-1, 1)
        self.assertFalse(posicion_en_tablero(pos))

    def test_posicion_row_pasa_max(self):
        pos = Posicion(8, 1)
        self.assertFalse(posicion_en_tablero(pos))

    def test_posicion_todo_invalido_min(self):
        pos = Posicion(-1, -1)
        self.assertFalse(posicion_en_tablero(pos))

    def test_posicion_todo_invalido_max(self):
        pos = Posicion(8, 8)
        self.assertFalse(posicion_en_tablero(pos))


class test_movimiento_bien_formado(unittest.TestCase):
    def test_movimiento_ok(self):
        self.assertTrue(
            movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE]))
        )


class test_juego_bien_formado(unittest.TestCase):
    def test_juego_ok(self):
        j = Juego(tablero_8x8_vacio(), DORADO, 0)
        self.assertTrue(juego_bien_formado(j))


#### Ejercicio 2


class test_posicion_vecina_hacia(unittest.TestCase):
    def test_vecina_al_norte(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(0, 0), NORTE), Posicion(1, 0))


class test_son_posiciones_vecinas(unittest.TestCase):
    def test_vecinas(self):
        self.assertTrue(son_posiciones_vecinas(Posicion(0, 0), Posicion(1, 0)))


class test_casilla_en_posicion(unittest.TestCase):
    def test_casilla_en_posicion(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertEqual(casilla_en_posicion(t, Posicion(0, 0)), Pieza(CABALLO, DORADO))


class test_hay_casilla_vacia(unittest.TestCase):
    def test_casilla_vacia(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_casilla_vacia(t, Posicion(2, 1)))

    def test_casilla_no_vacia(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_casilla_vacia(t, Posicion(0, 0)))


class test_hay_pieza_de_color(unittest.TestCase):
    def test_hay_pieza_de_color_ok(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_pieza_de_color(t, Posicion(1, 4), DORADO))


#### Ejercicio 3


class test_hay_casilla_vacia_hacia(unittest.TestCase):
    def test_hay_casilla_vacia_hacia(self):
        t = leer_tablero(
            [
                "-r----rr",  # 7
                "-mrh----",  # 6
                "-r---r--",  # 5
                "d-EH---c",  # 4
                "-M--hD-d",  # 3
                "-R-e----",  # 2
                "---H-R-C",  # 1
                "R-R---RR",  # 0
                # 01234567
            ]
        )
        self.assertTrue(hay_casilla_vacia_hacia(t, Posicion(0, 0), NORTE))


class test_hay_pieza_amiga_vecina(unittest.TestCase):
    def test_hay_pieza_amiga_vecina(self):
        t = leer_tablero(
            [
                "R-hRD-Rr",  # 7
                "M----d--",  # 6
                "-h-rrCR-",  # 5
                "R-rcE---",  # 4
                "--drRR--",  # 3
                "-HD-H--m",  # 2
                "--r-RCc-",  # 1
                "re---r--",  # 0
                # 01234567
            ]
        )
        self.assertTrue(hay_pieza_amiga_vecina(t, Posicion(4, 3)))


class test_hay_pieza_enemiga_mas_debil_hacia(unittest.TestCase):
    def test_hay_pieza_enemiga_mas_debil_hacia(self):
        t = leer_tablero(
            [
                "--Hdm---",  # 7
                "r--HhC--",  # 6
                "e---R-C-",  # 5
                "ME--d---",  # 4
                "h--RDcRr",  # 3
                "R-R-r--r",  # 2
                "-RRcrRD-",  # 1
                "--r---rr",  # 0
                # 01234567
            ]
        )
        self.assertTrue(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(1, 3), OESTE))


class test_hay_pieza_enemiga_mas_fuerte_hacia(unittest.TestCase):
    def test_hay_pieza_enemiga_mas_fuerza_hacia(self):
        t = tablero_8x8_ya_finalizando()
        pos = Posicion(3, 4)
        d = NORTE
        self.assertTrue(hay_pieza(t, pos))
        self.assertTrue(hay_pieza(t, posicion_vecina_hacia(pos, d)))
        self.assertEqual(posicion_vecina_hacia(pos, d), Posicion(4, 4))
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_hacia(t, pos, d))

    def test_no_hay_pieza_enemiga_hacia(self):
        t = tablero_8x8_ya_empezado()
        pos = Posicion(3, 0)
        d = NORTE
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_hacia(t, pos, d))

    def test_hay_pieza_enemiga_de_misma_fuerza_hacia(self):
        t = tablero_8x8_ya_empezado()
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
        t = leer_tablero(
            [
                "R-e--mRr",  # 7
                "------dE",  # 6
                "h--Rr-RR",  # 5
                "c--R-C--",  # 4
                "-rCHDrr-",  # 3
                "----rc--",  # 2
                "h-R-M-R-",  # 1
                "rr-D-dH-",  # 0
                # 01234567
            ]
        )
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(3, 1)))


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


#### Ejercicio 4


class test_puede_realizar_movimiento(unittest.TestCase):
    def test_mover_a_secas_ok(self):
        t = leer_tablero(
            [
                "--eMr---",  # 7
                "--------",  # 6
                "-R----r-",  # 5
                "--------",  # 4
                "--mMd---",  # 3
                "---D----",  # 2
                "--------",  # 1
                "-mD--mDR",  # 0
                # 01234567
            ]
        )
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE])
        self.assertTrue(puede_realizar_movimiento(j, m))


#### Ejercicio 5


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


class test_tableros_coinciden_salvo_en_la_posicion(unittest.TestCase):
    def test_coinciden_salvo_en_una_posicion(self):
        t1 = tablero_8x8_inicial_ejemplo()
        t2 = tablero_8x8_inicial_falta_un_conejo_dorado_en_h2()
        pos = Posicion(1, 7)
        self.assertTrue(tableros_coinciden_salvo_en_la_posicion(t1, t2, pos))

    def test_coinciden_en_todas_las_posiciones(self):
        t1 = tablero_8x8_inicial_ejemplo()
        t2 = tablero_8x8_inicial_ejemplo()
        pos = Posicion(0, 0)  # Indistinto, porque coinciden en todas las pos
        self.assertFalse(tableros_coinciden_salvo_en_la_posicion(t1, t2, pos))


#### Ejercicio 6


class test_realizar_movimiento(unittest.TestCase):
    def test_mover_a_secas(self):
        t0 = leer_tablero(
            [
                "rrrrrrrr",  # 7
                "ccddhh-e",  # 6
                "--------",  # 5
                "---m----",  # 4
                "--------",  # 3
                "--------",  # 2
                "EMHHDDCC",  # 1
                "RRRRRRRR",  # 0
                # 01234567
            ]
        )
        tN = leer_tablero(
            [
                "rrrrrrrr",  # 7
                "ccddhh-e",  # 6
                "---m----",  # 5
                "--------",  # 4
                "--------",  # 3
                "--------",  # 2
                "EMHHDDCC",  # 1
                "RRRRRRRR",  # 0
                # 01234567
            ]
        )
        j0 = Juego(t0, PLATEADO, 0)
        jN = Juego(tN, PLATEADO, 1)
        mN = Movimiento(MOVER_A_SECAS, Posicion(4, 3), [NORTE])
        self.assertTrue(puede_realizar_movimiento(j0, mN))
        self.assertEqual(realizar_movimiento(j0, mN), jN)


#### Ejercicio 7


class test_ganador_del_juego(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
