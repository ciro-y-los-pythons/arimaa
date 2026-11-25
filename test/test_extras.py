import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from src.arimaa import *
from test.ejemplos.tableros import *


# TEST #52 - Extra
class test_posiciones_de_las_piezas(unittest.TestCase):
    def test_posiciones_de_las_piezas(self):
        t = tablero_8x8_una_pieza()
        j = Juego(t,DORADO,0)

        res = {"R": [(3,5)]}
        self.assertEqual(posiciones_de_las_piezas(j), res)

# TEST #53 - Extras
class test_todos_los_movimientos_posibles(unittest.TestCase):
    def test_todos_los_movimientos_posibles(self):
        t = tablero_8x8_una_pieza()
        j = Juego(t, DORADO, 0)
        movimientos = todos_los_movimientos_posibles(j)

        res: list[Movimiento] = [
            Movimiento(MOVER_A_SECAS, Posicion(3, 5), [NORTE]),
            Movimiento(MOVER_A_SECAS, Posicion(3, 5), [ESTE]),
            Movimiento(MOVER_A_SECAS, Posicion(3, 5), [OESTE]),
        ]
        self.assertEqual(len(movimientos), len(res))

    def test_tablero_vacio(self):
        j = Juego(tablero_8x8_vacio(), DORADO, 0)
        self.assertEqual(todos_los_movimientos_posibles(j), [])

    def test_sin_pasos_disponibles(self):
        j = Juego(tablero_8x8_inicial_ejemplo(), DORADO, MAX_PASOS)
        self.assertEqual(todos_los_movimientos_posibles(j), [])

    def test_una_pieza_conejo_dorado(self):
        j = Juego(tablero_8x8_una_pieza(), DORADO, 0)
        origen = Posicion(3, 5)
        esperado = [
            Movimiento(MOVER_A_SECAS, origen, [NORTE]),
            Movimiento(MOVER_A_SECAS, origen, [ESTE]),
            Movimiento(MOVER_A_SECAS, origen, [OESTE]),
        ]
        self.assertCountEqual(todos_los_movimientos_posibles(j), esperado)

    def test_inicial_turno_dorado(self):
        j = Juego(tablero_8x8_inicial_ejemplo(), DORADO, 0)
        esperado = []
        for columna in range(ANCHO):
            esperado.append(Movimiento(MOVER_A_SECAS, Posicion(1, columna), [NORTE]))
        self.assertCountEqual(todos_los_movimientos_posibles(j), esperado)

    def test_inicial_turno_plateado(self):
        j = Juego(tablero_8x8_inicial_ejemplo(), PLATEADO, 0)
        esperado = []
        for columna in range(ANCHO):
            esperado.append(Movimiento(MOVER_A_SECAS, Posicion(6, columna), [SUR]))
        self.assertCountEqual(todos_los_movimientos_posibles(j), esperado)

    def test_camello_dorado_arrastra_y_empuja(self):
        j = Juego(tablero_8x8_ya_empezado_camello_dorado_empuja_conejo_plateado(), DORADO, 0)
        res = todos_los_movimientos_posibles(j)
        acciones = []
        for m in res:
            acciones.append(m.accion)
        self.assertIn(ARRASTRAR, acciones)
        self.assertIn(EMPUJAR, acciones)

    def test_con_un_solo_paso_restante_no_hay_movimientos_de_dos_pasos(self):
        j = Juego(tablero_8x8_ya_empezado_camello_dorado_empuja_conejo_plateado(), DORADO, MAX_PASOS - 1)
        res = todos_los_movimientos_posibles(j)
        self.assertTrue(len(res) > 0)
        for m in res:
            self.assertEqual(len(m.pasos), 1)

    def test_cumple_la_especificacion_en_tablero_ya_empezado(self):
        j = Juego(tablero_8x8_ya_empezado(), DORADO, 0)
        res = todos_los_movimientos_posibles(j)
        self.assertTrue(len(res) > 0)
        for i in range(len(res)):
            for k in range(i + 1, len(res)):
                self.assertNotEqual(res[i], res[k])
        for m in res:
            self.assertTrue(movimiento_bien_formado(m))
            self.assertTrue(puede_realizar_movimiento(j, m))


if __name__ == "__main__":
    unittest.main(verbosity=2)
