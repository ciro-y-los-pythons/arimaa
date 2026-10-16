from definiciones import *

#### Algunas funciones ya dadas

def son_posiciones_vecinas(pos1 : Posicion, pos2 : Posicion) -> bool: # pragma: no cover
    return (pos1.fila == pos2.fila and abs(pos1.columna - pos2.columna) == 1) \
        or (pos1.columna == pos2.columna and abs(pos1.fila - pos2.fila) == 1)

def direccion_desde_hasta(pos1 : Posicion, pos2 : Posicion) -> Direccion: # pragma: no cover
    assert son_posiciones_vecinas(pos1, pos2)
    if pos1.fila < pos2.fila:
       return NORTE
    elif pos1.fila > pos2.fila:
       return SUR
    elif pos1.columna < pos2.columna:
       return ESTE
    else:
       return OESTE

def pasar_turno(j : Juego) -> Juego: # pragma: no cover
    return Juego(j.tablero, oponente(j.turno), 0)

#### Ejercicio 1

def tablero_bien_formado(t : Tablero) -> bool:
    raise Exception("No implementado")

def posicion_en_tablero(pos : Posicion) -> bool:
    raise Exception("No implementado")

def movimiento_bien_formado(m : Movimiento) -> bool:
    raise Exception("No implementado")

def juego_bien_formado(j : Juego) -> bool:
    raise Exception("No implementado")

#### Ejercicio 2

def posicion_vecina_hacia(pos : Posicion, d : Direccion) -> Posicion:
    raise Exception("No implementado")

def casilla_en_posicion(t : Tablero, p : Posicion) -> Casilla:
    raise Exception("No implementado")

def hay_casilla_vacia(t : Tablero, pos : Posicion) -> bool:
    raise Exception("No implementado")

def hay_pieza_de_color(t : Tablero, pos : Posicion, col : Color) -> bool:
    raise Exception("No implementado")

#### Ejercicio 3

def hay_casilla_vacia_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    raise Exception("No implementado")

def hay_pieza_amiga_vecina(t : Tablero, pos : Posicion) -> bool:
    raise Exception("No implementado")

def hay_pieza_enemiga_mas_debil_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    raise Exception("No implementado")

def hay_pieza_enemiga_mas_fuerte_vecina(t : Tablero, pos : Posicion) -> bool:
    raise Exception("No implementado")

def hay_pieza_congelada(t : Tablero, pos : Posicion) -> bool:
    raise Exception("No implementado")

#### Ejercicio 4

def puede_realizar_movimiento(j : Juego, m : Movimiento) -> bool:
    raise Exception("No implementado")

#### Ejercicio 5

def activar_trampas(t : Tablero) -> Tablero:
    raise Exception("No implementado")

#### Ejercicio 6

def realizar_movimiento(j : Juego, m : Movimiento) -> Juego:
    raise Exception("No implementado")

#### Ejercicio 7

def hay_ganador_determinado(j : Juego) -> bool:
    raise Exception("No implementado")

def ganador_del_juego(j : Juego) -> Color:
    raise Exception("No implementado")

