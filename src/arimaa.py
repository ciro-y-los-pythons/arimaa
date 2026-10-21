from template.definiciones import *

#### Funciones ya dadas


def son_posiciones_vecinas(pos1: Posicion, pos2: Posicion) -> bool:  # pragma: no cover
    return (pos1.fila == pos2.fila and abs(pos1.columna - pos2.columna) == 1) or (
        pos1.columna == pos2.columna and abs(pos1.fila - pos2.fila) == 1
    )


def direccion_desde_hasta(
    pos1: Posicion, pos2: Posicion
) -> Direccion:  # pragma: no cover
    assert son_posiciones_vecinas(pos1, pos2)
    if pos1.fila < pos2.fila:
        return NORTE
    elif pos1.fila > pos2.fila:
        return SUR
    elif pos1.columna < pos2.columna:
        return ESTE
    else:
        return OESTE


def pasar_turno(j: Juego) -> Juego:  # pragma: no cover
    return Juego(j.tablero, oponente(j.turno), 0)


#### Ejercicio 1


def tablero_bien_formado(t: Tablero) -> bool:
    """Verifica si el Tablero se encuentra con las medidas correspondientes (8 x 8)

    Args:
        t: Tablero a Verificar.

    Returns:
        Si el Tablero se encuentra con las medidas correspondientes True, Sino False
        (|t| = ALTO ∧ ∀ i:Z.(0 ≤ i < |t| → |t[i]| = ANCHO))
    """
    if len(t) != ALTO:
        return False
    for i in t:
        if len(i) != ANCHO:
            return False
    return True


def posicion_en_tablero(pos: Posicion) -> bool:
    """Verifica si la posición ingresada Existe dentro del Tablero (8 x 8)

    Args:
        pos: Posición a Verificar.

    Returns:
        Si la posición ingresada no excede las medidas del Tablero: True, Sino False
        (0 ≤ pos.fila < Alto ∧ 0 ≤ pos.columna < Ancho)
    """
    es_fila_valida: bool = 0 <= pos.fila and pos.fila < ALTO
    es_columna_valida: bool = 0 <= pos.columna and pos.columna < ANCHO
    es_posicion_valida: bool = es_fila_valida and es_columna_valida
    return es_posicion_valida


def movimiento_bien_formado(m: Movimiento) -> bool:
    raise Exception("No implementado")


def juego_bien_formado(j: Juego) -> bool:
    raise Exception("No implementado")


#### Ejercicio 2


def posicion_vecina_hacia(pos: Posicion, d: Direccion) -> Posicion:
    """Verifico la posicion a la que quiero mover la pieza
    Args:
        pos (posicion): posicion actual
        d   (Dirección): dirección a la que quiero mover
    Return:
        Posicion (Posicion): posicion despues de mover a la dirección indicada """
    movimiento:Posicion
    if d==ESTE:
        movimiento=Posicion(fila = pos.fila-1, columna =pos.columna)
    elif d==OESTE:
        movimiento=Posicion(fila=pos.fila+1, columna=pos.columna)
    elif d==NORTE:
        movimiento=Posicion(fila=pos.fila, columna=pos.columna+1)
    elif d==SUR:
        movimiento=Posicion(fila=pos.fila, columna=pos.columna-1)
    return movimiento    

def casilla_en_posicion(t: Tablero, p: Posicion) -> Casilla:
    """"re
    Args:
        t   (Tablero): Tablero del Juego, en él se busca la posición.
        pos (Posición): Posición en la que se busca la casilla.
    
    Returns:
        bool: si esta vacía la celda en la {pos} dentro del {t}
    requires:
        tableroBienFormado (t) ∧ posiciónEnTablero (pos) 
    """
    casilla=t[p.fila][p.columna]
    return casilla
def hay_casilla_vacia(t: Tablero, pos: Posicion) -> bool:
    """Verifica si la casilla del {t} ubicada en la {pos} está vacía

    Args:
        t   (Tablero): Tablero del Juego, en él se busca la posición.
        pos (Posición): Posición en la que se busca la casilla.

    Returns:
        bool: si esta vacía la celda en la {pos} dentro del {t}
              {posicion_en_tablero(pos) and t[pos.fila][pos.columna] == CasillaVacia}

    Requires:
        bool: {tablero_bien_formado(t) ∧ posicion_en_tablero(pos)}
    """
    if not tablero_bien_formado(t):
        no_cumple_requiere = Exception("Requiere: tablero_bien_formado(t)")
        raise no_cumple_requiere
    if not posicion_en_tablero(pos):
        no_cumple_requiere = Exception("Requiere: posicion_en_tablero(pos)")
        raise no_cumple_requiere

    casilla: Casilla = t[pos.fila][pos.columna]
    casilla_esta_vacia: bool = casilla == CasillaVacia.VACIA
    return casilla_esta_vacia


def hay_pieza_de_color(t: Tablero, pos: Posicion, col: Color) -> bool:
    raise Exception("No implementado")


#### Ejercicio 3


def hay_casilla_vacia_hacia(t: Tablero, pos: Posicion, d: Direccion) -> bool:
    raise Exception("No implementado")


def hay_pieza_amiga_vecina(t: Tablero, pos: Posicion) -> bool:
    raise Exception("No implementado")


def hay_pieza_enemiga_mas_debil_hacia(t: Tablero, pos: Posicion, d: Direccion) -> bool:
    raise Exception("No implementado")


def hay_pieza_enemiga_mas_fuerte_vecina(t: Tablero, pos: Posicion) -> bool:
    raise Exception("No implementado")


def hay_pieza_congelada(t: Tablero, pos: Posicion) -> bool:
    raise Exception("No implementado")


#### Ejercicio 4


def puede_realizar_movimiento(j: Juego, m: Movimiento) -> bool:
    raise Exception("No implementado")


#### Ejercicio 5


def activar_trampas(t: Tablero) -> Tablero:
    raise Exception("No implementado")


#### Ejercicio 6


def realizar_movimiento(j: Juego, m: Movimiento) -> Juego:
    raise Exception("No implementado")


#### Ejercicio 7


def hay_ganador_determinado(j: Juego) -> bool:
    raise Exception("No implementado")


def ganador_del_juego(j: Juego) -> Color:
    raise Exception("No implementado")
