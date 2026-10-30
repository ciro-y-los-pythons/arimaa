"""
Archivo general de tests (Explota de Exceptions, no es muy recomendable ejecutarlo)
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
# test_cases: 24/24
# date_checked: 30/10, 09:50


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
    def test_movimiento_no_esta_en_tablero(self):
        self.assertFalse(
            movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(9, -1), [NORTE]))
        )
    def test_movimiento_mover_a_secas_con_un_paso(self):
        self.assertTrue(
            movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE]))
        )
    def test_movimiento_mover_a_secas_con_dos_pasos(self):
        self.assertFalse(
            movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(2, 3), [NORTE,SUR]))
        )
    def test_movimiento_empujar_con_dos_pasos(self):
        self.assertTrue(
            movimiento_bien_formado(Movimiento(EMPUJAR, Posicion(0, 1), [NORTE,ESTE]))
        )
    def test_movimiento_empujar_con_un_paso(self):
        self.assertFalse(
            movimiento_bien_formado(Movimiento(EMPUJAR, Posicion(0, 1), [NORTE]))
        )
    def test_movimiento_arrastrar_con_dos_pasos(self):
        self.assertTrue(
            movimiento_bien_formado(Movimiento(ARRASTRAR, Posicion(0, 1), [NORTE,ESTE]))
        )
    def test_movimiento_arrastrar_con_un_paso(self):
        self.assertFalse(
            movimiento_bien_formado(Movimiento(ARRASTRAR, Posicion(0, 1), [NORTE]))
        )


class test_juego_bien_formado(unittest.TestCase):
    def test_juego_valido_minimo(self):
        j = Juego(tablero_8x8_vacio(), DORADO, 0)
        self.assertTrue(juego_bien_formado(j))
    def test_juego_valido_maximo(self):
        j = Juego(tablero_8x8_vacio(), DORADO, 3)
        self.assertTrue(juego_bien_formado(j))
    def test_juego_invalido_pasos_negativos(self):
        j = Juego(tablero_8x8_vacio(), DORADO, -1)
        self.assertFalse(juego_bien_formado(j))
    def test_juego_invalido_pasos_excedidos(self):
        j = Juego(tablero_8x8_vacio(), DORADO, 4)
        self.assertFalse(juego_bien_formado(j))
    def test_juego_invalido_tablero_mal(self):
        j = Juego(tablero_mal_formado_filas_ejemplo(), DORADO, 0)
        self.assertFalse(juego_bien_formado(j))


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
        t0 = tablero_8x8_camello_plateado_en_trampa()
        t1 = tablero_8x8_camello_plateado_en_trampa_quitado()
        t2 = activar_trampas(t0)
        self.assertNotEqual(t0,t1)
        self.assertEqual(t2,t1)
        self.assertTrue(tablero_bien_formado(t2))
        self.assertTrue(es_tablero_despues_de_activar_todas_las_trampas(t0,t2))


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
        t0 = tablero_8x8_camello_plateado_en_trampa()
        t1 = tablero_8x8_camello_plateado_en_trampa_quitado()
        pos_trampa = Posicion(2,5)
        self.assertTrue(es_tablero_despues_de_activar_trampa(t0,t1, pos_trampa))

    def test_no_hay_amiga_y_no_Se_quita_pieza(self):
        t0 = tablero_8x8_camello_plateado_en_trampa()
        t1 = tablero_8x8_camello_plateado_en_trampa()
        pos_trampa = Posicion(2,5)
        self.assertFalse(es_tablero_despues_de_activar_trampa(t0,t1, pos_trampa))


class test_es_tablero_despues_de_activar_todas_las_trampas(unittest.TestCase):
    def test_no_hay_piezas_en_trampa_tableros_correctos(self):
        t0 = tablero_8x8_camello_plateado_en_trampa_quitado()
        t1 = tablero_8x8_camello_plateado_en_trampa_quitado()
        self.assertTrue(es_tablero_despues_de_activar_todas_las_trampas(t0,t1))

    def test_no_hay_piezas_en_trampa_tableros_incorrectos(self):
        t0 = tablero_8x8_camello_plateado_en_trampa_quitado()
        t1 = tablero_8x8_camello_plateado_en_trampa()
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
        t0 = tablero_8x8_camello_plateado_en_trampa()
        t1 = tablero_8x8_camello_plateado_en_trampa_quitado()
        self.assertTrue(es_tablero_despues_de_activar_todas_las_trampas(t0,t1))

    def test_una_sola_pieza_en_trampa_y_no_se_activa(self):
        t0 = tablero_8x8_camello_plateado_en_trampa()
        t1 = tablero_8x8_camello_plateado_en_trampa()
        self.assertFalse(es_tablero_despues_de_activar_todas_las_trampas(t0,t1))

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


class test_hay_que_cambiar_de_turno(unittest.TestCase):
    def test_mover_a_secas_inicio(self):
        j = Juego(tablero_8x8_inicial_ejemplo(),DORADO,0)
        m = Movimiento(MOVER_A_SECAS,Posicion(1,1),[NORTE])
        self.assertFalse(hay_que_cambiar_de_turno(j,m))
    def test_camello_empuja_conejo_y_juego_tenia_2_pasos(self):
        j = Juego(tablero_8x8_ya_finalizando(),PLATEADO,2)
        m = Movimiento(EMPUJAR,Posicion(4,4),[SUR,SUR])
        self.assertTrue(hay_que_cambiar_de_turno(j,m))


class test_juego_con_turno_posiblemente_avanzado(unittest.TestCase):
    def test_cambia_de_turno_todo_ok(self):
        j0 = Juego(tablero_8x8_ya_empezado(),DORADO,3)
        j1 = Juego(tablero_8x8_ya_empezado_mueve_camello_plateado_a4(),PLATEADO,0)
        m = Movimiento(MOVER_A_SECAS,Posicion(4,0),[SUR])
        self.assertTrue(juego_con_turno_posiblemente_avanzado(j0,j1,m))
    def test_no_cambia_de_turno_todo_ok(self):
        j0 = Juego(tablero_8x8_ya_empezado(),PLATEADO,2)
        j1 = Juego(tablero_8x8_ya_empezado_mueve_camello_plateado_a4(),PLATEADO,3)
        m = Movimiento(MOVER_A_SECAS,Posicion(4,0),[SUR])
        self.assertTrue(juego_con_turno_posiblemente_avanzado(j0,j1,m))
    def test_cambia_de_turno_pero_no_de_jugador(self):
        j0 = Juego(tablero_8x8_ya_empezado(),DORADO,3)
        j1 = Juego(tablero_8x8_ya_empezado_mueve_camello_plateado_a4(),DORADO,0)
        m = Movimiento(MOVER_A_SECAS,Posicion(4,0),[SUR])
        self.assertFalse(juego_con_turno_posiblemente_avanzado(j0,j1,m))
    def test_cambia_de_turno_pero_no_reinicia_pasos(self):
        j0 = Juego(tablero_8x8_ya_empezado(),DORADO,3)
        j1 = Juego(tablero_8x8_ya_empezado_mueve_camello_plateado_a4(),PLATEADO,4)
        m = Movimiento(MOVER_A_SECAS,Posicion(4,0),[SUR])
        self.assertFalse(juego_con_turno_posiblemente_avanzado(j0,j1,m))


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


if __name__ == "__main__":
    unittest.main(verbosity=2)
