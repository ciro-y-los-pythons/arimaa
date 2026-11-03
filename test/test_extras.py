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
            Movimiento(MOVER_A_SECAS, Posicion(3, 5), [SUR]),
            Movimiento(MOVER_A_SECAS, Posicion(3, 5), [ESTE]),
            Movimiento(MOVER_A_SECAS, Posicion(3, 5), [OESTE]),
        ]
        self.assertEqual(len(movimientos), len(res))


if __name__ == "__main__":
    unittest.main(verbosity=2)