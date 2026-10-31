import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from src.arimaa import *
from test.ejemplos.tableros import *


# TEST #37 - Problema
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

    def test_mover_a_secas_con_trampa(self):
        t0 = tablero_8x8_piezas_en_todas_las_trampas_sin_amigas_1()
        tN = tablero_8x8_piezas_en_todas_las_trampas_sin_amigas_mueve_conejo()
        
        j0 = Juego(t0, DORADO, 0)
        jN = Juego(tN, DORADO, 1)
        mN = Movimiento(MOVER_A_SECAS, Posicion(2, 5), [NORTE])
        self.assertTrue(puede_realizar_movimiento(j0, mN))
        self.assertEqual(realizar_movimiento(j0, mN), jN)

    # ARRASTRAR
    def test_arrastrar_correctamente(self):
        t0 = leer_tablero(
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
        tN = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "----E---",  # 5
                "----r---",  # 4
                "--------",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        
        j0 = Juego(t0, DORADO, 0)
        jN = Juego(tN, DORADO, 2)
        mN = Movimiento(ARRASTRAR, Posicion(4, 4), [NORTE,NORTE])
        self.assertTrue(puede_realizar_movimiento(j0, mN))
        self.assertEqual(realizar_movimiento(j0, mN), jN)

    def test_arrastrar_con_trampa(self):
        t0 = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "--------",  # 5
                "----E---",  # 4
                "----r---",  # 3
                "-----c--",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        tN = leer_tablero(
            [
                "--------",  # 7
                "--------",  # 6
                "----E---",  # 5
                "----r---",  # 4
                "--------",  # 3
                "--------",  # 2
                "--------",  # 1
                "--------",  # 0
                # 01234567
            ]
        )
        
        j0 = Juego(t0, DORADO, 0)
        jN = Juego(tN, DORADO, 2)
        mN = Movimiento(ARRASTRAR, Posicion(4, 4), [NORTE,NORTE])
        self.assertTrue(puede_realizar_movimiento(j0, mN))
        self.assertEqual(realizar_movimiento(j0, mN), jN)

    # EMPUJAR
    def test_empujar_correctamente(self):
        t0 = tablero_8x8_ya_empezado()
        tN = tablero_8x8_ya_empezado_camello_dorado_empuja_conejo_plateado()
        
        j0 = Juego(t0, DORADO, 0)
        jN = Juego(tN, DORADO, 2)
        mN = Movimiento(EMPUJAR, Posicion(1, 4), [NORTE,OESTE])
        self.assertTrue(puede_realizar_movimiento(j0, mN))
        self.assertEqual(realizar_movimiento(j0, mN), jN)


    def test_empujar_con_trampa(self):
        t0 = tablero_8x8_gato_plateado_en_trampa()
        tN = tablero_8x8_gato_plateado_en_trampa_quitado_y_perro_plateado_empuja_conejo_dorado_a_trampa()
        
        j0 = Juego(t0, PLATEADO, 0)
        jN = Juego(tN, PLATEADO, 2)
        mN = Movimiento(EMPUJAR, Posicion(6, 6), [SUR,OESTE])
        self.assertTrue(puede_realizar_movimiento(j0, mN))
        self.assertEqual(realizar_movimiento(j0, mN), jN)

    # CAMBIO DE TURNO
    def test_mismo_turno(self):
        t0 = tablero_8x8_empezando()
        tN = tablero_8x8_empezando_mueve_conejo_dorado_a5()
        j0 = Juego(t0, DORADO, 0)
        jN = Juego(tN, DORADO, 1)
        mN = Movimiento(MOVER_A_SECAS, Posicion(3, 0), [NORTE])
    
        self.assertTrue(puede_realizar_movimiento(j0, mN))
        self.assertEqual(realizar_movimiento(j0, mN), jN)
    
    
    def test_cambio_de_turno(self):
        t0 = tablero_8x8_empezando()
        tN = tablero_8x8_empezando_mueve_conejo_dorado_a5()
        j0 = Juego(t0, DORADO, 3)
        jN = Juego(tN, PLATEADO, 0)
        mN = Movimiento(MOVER_A_SECAS, Posicion(3, 0), [NORTE])
    
        self.assertTrue(puede_realizar_movimiento(j0, mN))
        self.assertEqual(realizar_movimiento(j0, mN), jN)


# TEST #28 - Auxiliar
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

# TEST #29 - Auxiliar
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

# TEST #30 - Auxiliar
class test_tablero_post_mover_a_secas(unittest.TestCase):
    def test_mueve_y_no_habia_piezas_en_trampa(self):
        t0 = tablero_8x8_inicial_ejemplo()
        t1 = tablero_8x8_mueve_conejo_dorado_h3()
        pos = Posicion(1,7)
        d = NORTE
        self.assertTrue(tablero_post_mover_a_secas(t0,t1,pos,d))


    def test_mueve_y_habia_piezas_en_trampa(self):
        t0 = tablero_8x8_piezas_en_todas_las_trampas_sin_amigas_1()
        t1 = tablero_8x8_piezas_en_todas_las_trampas_sin_amigas_mueve_conejo()
        pos = Posicion(2,5)
        d = NORTE
        # Mueve y se activan las trampas
        self.assertTrue(tablero_post_mover_a_secas(t0,t1,pos,d))

        # Mueve y no se activan las trampas
        t2 = genera_tablero_quitando_pieza_en_posicion(t0,pos)
        t2 = genera_tablero_poniendo_pieza_en_posicion(t2, t0[pos.fila][pos.columna], posicion_vecina_hacia(pos,NORTE))
        self.assertFalse(tablero_post_mover_a_secas(t0,t2,pos,d))

    def test_mueve_fuera_del_tablero(self):
        t0 = tablero_8x8_ya_empezado()
        t1 = tablero_8x8_ya_empezado_mueve_camello_plateado_a4()
        pos = Posicion(4,0)
        d = OESTE
        self.assertFalse(tablero_post_mover_a_secas(t0,t1,pos,d))

    def test_no_puede_mover_a_secas(self):
        t0 = tablero_8x8_ya_empezado()
        t1 = tablero_8x8_ya_empezado() # Indistinto, corta cuando puede_mover_a_secas(t0,pos,d) == False
        pos = Posicion(3,5)
        d = SUR
        self.assertFalse(tablero_post_mover_a_secas(t0,t1,pos,d))

    def test_pieza_mueve_a_pos_distinta(self):
        t0 = tablero_8x8_ya_empezado()
        t1 = tablero_8x8_ya_empezado_mueve_camello_plateado_a4()
        pos = Posicion(4,0)
        d = ESTE
        self.assertFalse(tablero_post_mover_a_secas(t0,t1,pos,d))

# TEST #31 - Auxiliar
# class test_tablero_post_arrastrar(unittest.TestCase):
#     def test_tablero_post_arrastrar_ok(self):
#         self.assertEqual(tablero_post_arrastrar())

# TEST #32 - Auxiliar
class test_tablero_post_empujar(unittest.TestCase):
    def test_empuja_y_no_habia_piezas_en_trampa(self):
        t0 = tablero_8x8_ya_empezado()
        t1 = tablero_8x8_ya_empezado_camello_dorado_empuja_conejo_plateado()
        pos = Posicion(1,4)
        d = NORTE
        d_empuje = OESTE

        self.assertTrue(tablero_post_empujar(t0,t1,pos,d,d_empuje))


    def test_empuja_y_habia_piezas_en_trampa(self):
        t0 = tablero_8x8_gato_plateado_en_trampa()
        t1 = tablero_8x8_gato_plateado_en_trampa_quitado_y_perro_plateado_empuja_conejo_dorado_a_trampa()
        pos = Posicion(6,6)
        d = SUR
        d_empuje = OESTE

        # Se activan las trampas
        self.assertTrue(tablero_post_empujar(t0,t1,pos,d,d_empuje))

        # No se activan las trampas
        pos_enemiga = posicion_vecina_hacia(pos,d)
        pos_hueco = posicion_vecina_hacia(pos_enemiga,d_empuje)
        t2 = genera_tablero_quitando_pieza_en_posicion(t0,pos_enemiga)
        t2 = genera_tablero_poniendo_pieza_en_posicion(t2,t0[pos_enemiga.fila][pos_enemiga.columna],pos_hueco)
        self.assertFalse(tablero_post_empujar(t0,t2,pos,d,d_empuje))

# TEST #34 - Auxiliar
class test_hay_que_cambiar_de_turno(unittest.TestCase):
    def test_mover_a_secas_inicio(self):
        j = Juego(tablero_8x8_inicial_ejemplo(),DORADO,0)
        m = Movimiento(MOVER_A_SECAS,Posicion(1,1),[NORTE])
        self.assertFalse(hay_que_cambiar_de_turno(j,m))
    def test_camello_empuja_conejo_y_juego_tenia_2_pasos(self):
        j = Juego(tablero_8x8_ya_finalizando(),PLATEADO,2)
        m = Movimiento(EMPUJAR,Posicion(4,4),[SUR,SUR])
        self.assertTrue(hay_que_cambiar_de_turno(j,m))

# TEST #35 - Auxiliar
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

# TEST #36 - Auxiliar
# class test_juego_post_movimiento(unittest.TestCase):
#     def test_juego_post_movimiento_ok(self):
#         self.assertEqual(juego_post_movimiento())


if __name__ == "__main__":
    unittest.main(verbosity=2)
