from enum import Enum
from typing import Final, NamedTuple

ALTO = 8
ANCHO = 8
MAX_PASOS = 4

#### Figura


class Figura(Enum):
    ELEFANTE = "ELEFANTE"
    CAMELLO = "CAMELLO"
    CABALLO = "CABALLO"
    PERRO = "PERRO"
    GATO = "GATO"
    CONEJO = "CONEJO"

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)


ELEFANTE = Figura.ELEFANTE
CAMELLO = Figura.CAMELLO
CABALLO = Figura.CABALLO
PERRO = Figura.PERRO
GATO = Figura.GATO
CONEJO = Figura.CONEJO


def fuerza(f: Figura) -> int:
    if f == CONEJO:
        return 1
    elif f == GATO:
        return 2
    elif f == PERRO:
        return 3
    elif f == CABALLO:
        return 4
    elif f == CAMELLO:
        return 5
    else:
        return 6


#### Color


class Color(Enum):
    DORADO = "DORADO"
    PLATEADO = "PLATEADO"

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)


DORADO = Color.DORADO
PLATEADO = Color.PLATEADO


def oponente(col: Color) -> Color:
    if col == DORADO:
        return PLATEADO
    else:
        return DORADO


#### Casilla


class CasillaVacia(Enum):
    VACIA = "VACIA"

    def __repr__(self):
        return "VACIA"

    @property
    def figura(self) -> Figura:
        raise Exception("La casilla está vacía, no contiene una figura.")

    @property
    def color(self) -> Color:
        raise Exception("La casilla está vacía, no contiene un color.")


class Pieza(NamedTuple):
    figura: Figura
    color: Color


VACIA: Final = CasillaVacia.VACIA

Casilla = CasillaVacia | Pieza

#### Tablero

Tablero = list[list[Casilla]]

#### Acción


class Accion(Enum):
    MOVER_A_SECAS = "MOVER_A_SECAS"
    ARRASTRAR = "ARRASTRAR"
    EMPUJAR = "EMPUJAR"

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)


MOVER_A_SECAS = Accion.MOVER_A_SECAS
ARRASTRAR = Accion.ARRASTRAR
EMPUJAR = Accion.EMPUJAR

#### Posición


class Posicion(NamedTuple):
    fila: int
    columna: int


POSICIONES_TRAMPA = [
    Posicion(2, 2),
    Posicion(2, 5),
    Posicion(5, 2),
    Posicion(5, 5),
]

#### Dirección


class Direccion(Enum):
    NORTE = "NORTE"
    SUR = "SUR"
    ESTE = "ESTE"
    OESTE = "OESTE"

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)


NORTE = Direccion.NORTE
SUR = Direccion.SUR
ESTE = Direccion.ESTE
OESTE = Direccion.OESTE


def opuesta(d: Direccion) -> Direccion:
    if d == NORTE:
        return SUR
    elif d == SUR:
        return NORTE
    elif d == ESTE:
        return OESTE
    else:
        return ESTE


#### Movimiento


class Movimiento(NamedTuple):
    accion: Accion
    origen: Posicion
    pasos: list[Direccion]


#### Juego


class Juego(NamedTuple):
    tablero: Tablero
    turno: Color
    pasos_consumidos: int


#### Para escribir piezas y tableros como strings

LETRA_A_FIGURA: dict[str, Figura] = {
    "E": ELEFANTE,
    "M": CAMELLO,
    "H": CABALLO,
    "D": PERRO,
    "C": GATO,
    "R": CONEJO,
}

FIGURA_A_LETRA: dict[Figura, str] = {}
for letra, figura in LETRA_A_FIGURA.items():
    FIGURA_A_LETRA[figura] = letra


def leer_casilla(letra: str) -> Casilla:
    if letra == "-":
        return VACIA
    color = DORADO if letra == letra.upper() else PLATEADO
    figura = LETRA_A_FIGURA[letra.upper()]
    return Pieza(figura, color)


# Ejemplo:
#
#  leer_tablero([
#     'hcdmedch',
#     'rrrrrrrr',
#     '--------',
#     '--------',
#     '--------',
#     '--------',
#     'RRRRRRRR',
#     'HCDMEDCH',
#   ])
#
# Devuelve el correspondiente tablero.
def leer_tablero(lineas: list[str]) -> Tablero:
    tablero = []
    for linea in lineas:
        fila = []
        for letra in linea:
            fila.append(leer_casilla(letra))
        tablero.append(fila)
    return tablero[::-1]


def mostrar_casilla(casilla: Casilla) -> str:
    if casilla == VACIA:
        return "-"
    elif casilla.color == DORADO:
        return FIGURA_A_LETRA[casilla.figura]
    else:
        return FIGURA_A_LETRA[casilla.figura].lower()


# mostrar_tablero es la función inversa de leer_tablero
def mostrar_tablero(t: Tablero) -> list[str]:
    lineas = []
    for ii in range(ALTO):
        i = ALTO - 1 - ii
        linea = []
        for j in range(ANCHO):
            linea.append(mostrar_casilla(t[i][j]))
        lineas.append("".join(linea))
    return lineas


def leer_tablero_de_archivo(nombre_archivo: str):
    with open(nombre_archivo) as f:
        lineas = f.readlines()
    lineas = [linea.strip(" \t\r\n") for linea in lineas]
    return leer_tablero(lineas)


def mostrar_tablero_en_pantalla(t: Tablero) -> None:
    lineas = mostrar_tablero(t)
    for linea in lineas:
        print(linea)
