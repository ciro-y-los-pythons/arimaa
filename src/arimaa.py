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
    """Verifica si el movimiento parte de un origen valido y si la cantidad de pasos coincide con la accion

    PRE: True

    Args:
        m: Movimiento a verificar

    Returns:
        Si la posicion de origen existe en el tablero y la cantidad de pasos coincide con la accion: True, sino False
        {posiciónEnTablero(m.origen)
        ∧ (m.acción = Mover_a_secas → |m.pasos| = 1)
        ∧ (m.acción = Arrastrar → |m.pasos| = 2)
        ∧ (m.acción = Empujar → |m.pasos| = 2)}

    """
    while posicion_en_tablero(m.origen):
        if len(m.pasos) == 1:
            return m.accion == MOVER_A_SECAS
        elif len(m.pasos) == 2:
            return m.accion == ARRASTRAR or m.accion == EMPUJAR

    return False


def juego_bien_formado(j: Juego) -> bool:
    """Verifica que el tablero este bien y los pasos esten dentro del limite.

    PRE: True

    Args:
        j: El estado del juego a revisar.

    Returns:
        Si el tablero y los pasos están dentro de los límites: True, Sino False
        (tableroBienFormado (j.tablero) ∧ 0 ≤ j.pasosConsumidos < Max_pasos)
    """
    es_tablero_valido: bool = tablero_bien_formado(j.tablero)
    son_pasos_validos: bool = 0 <= j.pasos_consumidos and j.pasos_consumidos < MAX_PASOS
    
    es_juego_valido: bool = es_tablero_valido and son_pasos_validos
    return es_juego_valido


#### Ejercicio 2


def posicion_vecina_hacia(pos: Posicion, d: Direccion) -> Posicion:
    """Verifico la posicion a la que quiero mover la pieza

    Args:
        pos (posicion): posicion actual
        d   (Dirección): dirección a la que quiero mover

    Returns:
        Posicion (Posicion): posicion despues de mover a la dirección indicada
    """
    movimiento: Posicion
    if d == SUR:
        movimiento = Posicion(fila=pos.fila - 1, columna=pos.columna)
    elif d == NORTE:
        movimiento = Posicion(fila=pos.fila + 1, columna=pos.columna)
    elif d == ESTE:
        movimiento = Posicion(fila=pos.fila, columna=pos.columna + 1)
    elif d == OESTE:
        movimiento = Posicion(fila=pos.fila, columna=pos.columna - 1)
    return movimiento


def casilla_en_posicion(t: Tablero, p: Posicion) -> Casilla:
    """
    Args:
        t   (Tablero): Tablero del Juego, en él se busca la posición.
        pos (Posición): Posición en la que se busca la casilla.

    Returns:
        bool: si esta vacía la celda en la {pos} dentro del {t}

    Requires:
        tableroBienFormado (t) ∧ posiciónEnTablero (pos)
    """
    casilla = t[p.fila][p.columna]
    return casilla


def hay_figura_de_color(t: Tablero, pos: Posicion, f: Figura, col: Color) -> bool:
    """
    Verfica si hay una {Pieza} de determinada {Figura} y {Color} en cierta {Posicion} del {Tablero}

    Requires:
        True

    Arguments:
        t    (Tablero): Tablero en el que se busca la Pieza
        pos (Posicion): Posición de la Pieza a buscar
        f     (Figura): Figura con que tiene que coincidir
        col    (Color): Color con el que tiene que coincidir

    Returns:
        bool: Si hay una {f} de cierto {col} en la {pos} del {t}
        {posiciónEnTablero(pos) ∧ ¬hayCasillaVacía(t, pos)}
    """
    if not posicion_en_tablero(pos):
        return False
    if hay_casilla_vacia(t, pos):
        return False

    pieza_encontrada: Casilla = casilla_en_posicion(t, pos)
    es_la_misma_figura: bool = pieza_encontrada.figura == f
    es_el_mismo_color: bool = pieza_encontrada.color == col

    return es_la_misma_figura and es_el_mismo_color


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
    """
    Verifica si hay una Pieza de determinado Color en cierta Posicion del Tablero

    Pre:
        tableroBienFormado(t) ∧ posiciónEnTablero(pos)

    Args:
        t: Tablero en el que se busca la Pieza
        pos: Posición de la Pieza a buscar
        col: Color con el que tiene que coincidir

    Returns:
        bool: Si hay una Pieza de cierto {col} en la {pos} del {t}
    """
    figuras: list[Figura] = [ELEFANTE, CAMELLO, CABALLO, PERRO, GATO, CONEJO]
    res: bool = False

    for f in figuras:
        if hay_figura_de_color(t, pos, f, col):
            res = True

    return res


#### Ejercicio 3


def hay_casilla_vacia_hacia(t: Tablero, pos: Posicion, d: Direccion) -> bool:
    """Verifica si hay una casilla vacia en la direccion a la que se quiere mover
    requiere:
        tableroBienFormado (t) ∧ posiciónEnTablero (pos)
    Args:
        t (tablero): ablero del Juego, en él se busca la posición.
        pos (Posición): Posición en la que se busca la casilla.
        d   (Dirección): direccion a la que se quiere hacer el movimiento
    Returns:
        Bool: retorna True si"""
    posicion_vecina: Posicion = posicion_vecina_hacia(pos, d)
    verificar: bool = hay_casilla_vacia(t, posicion_vecina)
    return verificar


def hay_pieza(t: Tablero, pos: Posicion) -> bool:
    """
    Verfica si hay una {Pieza} en cierta {Posicion} del {Tablero}

    Requires:
        True

    Arguments:
        t    (Tablero): Tablero en el que se busca la Pieza
        pos (Posicion): Posición de la Pieza a buscar

    Returns:
        ∃ f: Figura. ∃ col: Color. {hay_figura_de_color(t, pos, f, col)}
    """
    casilla_encontrada: Casilla = casilla_en_posicion(t, pos)
    es_una_pieza: bool = casilla_encontrada != VACIA
    return es_una_pieza


def hay_pieza_amiga_vecina(t: Tablero, pos: Posicion) -> bool:
    """Verifica si hay una pieza amiga vecina

    Requires:
        Casilla_en_posicion(t, pos)
        ∧ posicion_vecina_hacia(pos, direccion)
        ∧ posicion_en_tablero(vecina)
        ∧ hay_pieza_de_color(t, vecina, color)

    Arguments:
        t    (Tablero): Tablero en el que se verifica si hay pieza amiga vecina
        pos  (Posicion): Posición de la p_propia

    Returns:
        Bool: res = True ↔ ∃ d: Direccion.(posicion_en_tablero(posicion_vecina_hacia(pos, d))
                ∧ hay_pieza_de_color(t, posicion_vecina_hacia(pos, d), casilla_en_posicion(t, pos).color)
            )
    """
    color: Color = casilla_en_posicion(t, pos).color
    hay_amiga: bool = False
    direcciones: list[Direccion] = [NORTE, SUR, ESTE, OESTE]

    for direccion in direcciones:
        vecina: Posicion = posicion_vecina_hacia(pos, direccion)
        if posicion_en_tablero(vecina):
            if hay_pieza_de_color(t, vecina, color):
                hay_amiga = True

    return hay_amiga


def hay_pieza_enemiga_mas_debil_hacia(t: Tablero, pos: Posicion, d: Direccion) -> bool:
    raise Exception("No implementado")


def hay_pieza_enemiga_mas_fuerte_hacia(t: Tablero, pos: Posicion, d: Direccion) -> bool:
    """
    Verifica si hay una pieza_enemiga más fuerte hacia cierta dirección

    Requires:
        True

    Arguments:
        t    (Tablero): Tablero en el que se verifica si ∃ la p_enemiga
        pos (Posicion): Posición de la p_propia
        d  (Dirección): Dirección en la que se busca la p_enemiga

    Returns:
        ∃ f: Figura. ∃ col: Color. ∃ pos_enemiga: Posición. ∃ f_enemiga: Figura. (
            hay_figura_de_color (t, pos, f, col)
            ∧ es_posición_vecina_hacia (pos, d, pos_enemiga)
            ∧ hay_figura_de_color (t, pos_enemiga, f_enemiga, oponente(col))
            ∧ fuerza(f) < fuerza(f_enemiga)
        )
    """
    # Verificar ∃ pieza_propia
    casilla_propia_esta_vacia: bool = hay_casilla_vacia(t, pos)
    if casilla_propia_esta_vacia:
        return False
    p_propia: Casilla = casilla_en_posicion(t, pos)

    # Verificar ∃ pieza_vecina
    posicion_vecina: Posicion = posicion_vecina_hacia(pos, d)
    if not posicion_en_tablero(posicion_vecina):
        return False
    if hay_casilla_vacia_hacia(t, pos, d):
        return False
    p_vecina: Casilla = casilla_en_posicion(t, posicion_vecina)

    # Verifica si es pieza enemiga
    color_enemigo: Color = oponente(p_propia.color)
    es_p_enemiga: bool = p_vecina.color == color_enemigo
    if not es_p_enemiga:
        return False

    es_p_enemiga_mas_fuerte: bool = fuerza(p_propia.figura) < fuerza(p_vecina.figura)
    return es_p_enemiga_mas_fuerte


def hay_pieza_enemiga_mas_fuerte_vecina(t: Tablero, pos: Posicion) -> bool:
    """
    Verifica si hay una pieza_enemiga más fuerte alrededor de cierta Posición

    Requires:
        tablero_bien_formado(t)
        ∧ posicion_en_tablero(pos)
        ∧ hay_pieza(t, pos)

    Arguments:
        t    (in Tablero): Tablero en el que se verifica si ∃ la p_enemiga
        pos (in Posicion): Posición de la p_propia

    Returns:
        Bool: { res = True ←→ hay_pieza_enemiga_mas_fuerte_vecina(t, pos) }
            V { ∃ d: Dirección. hay_pieza_enemiga_mas_fuerte_hacia(t, pos, d) }
    """
    if not tablero_bien_formado(t):
        exception_t = Exception("Requiere: Tablero bien formado")
        raise exception_t
    if not posicion_en_tablero(pos):
        exception_pos = Exception("Requiere: posición Existente en el Tablero")
        raise exception_pos
    if not hay_pieza(t, pos):
        exception_p = Exception("Requiere: ∃ pieza en la Posición del Tablero")
        raise exception_p

    direcciones: list[Direccion] = [NORTE, SUR, ESTE, OESTE]
    for d in direcciones:
        if hay_pieza_enemiga_mas_fuerte_hacia(t, pos, d):
            return True
    return False


def hay_pieza_congelada(t: Tablero, pos: Posicion) -> bool:
    raise Exception("No implementado")


#### Ejercicio 4

def puede_realizar_movimiento(j: Juego, m: Movimiento) -> bool:
    raise Exception("No implementado")


def direccion_de_movimiento_habilitada(t: Tablero, pos: Posicion, d: Direccion) -> bool:
    """Verifica si en la Posicion pos hay una figura y si es CONEJO, que mueva hacia "adelante" con respecto a su color
    PRE:
        True

    Args:
        t (Tablero): Tablero donde deberia estar la figura
        pos (Posicion): Posicion del tablero a verificar
        d (Direccion): Direccion donde se quiere mover la pieza

    Returns:
        Si la figura existe en la pos y es CONEJO:
            - Si es DORADO y d es NORTE True, sino False
            - Si es PLATEADO y d es SUR True, sino False
        Si la figura existe en la pos y no es CONEJO: True, sino False
        Existe f: Figura. Existe col: Color. (hayFiguraDeColor (t, pos, f, col)
        ∧ ((f = Conejo ∧ col = Dorado ) → d != Sur )
        ∧ ((f = Conejo ∧ col = Plateado ) → d != Norte )
    """
    pieza: Pieza = t[pos.fila][pos.columna]

    es_direccion_habilitada: bool = False
    
    if pieza == VACIA:
        return False

    f: Figura = pieza.figura
    col: Color = pieza.color

    if hay_figura_de_color(t,pos,f,col):
        es_direccion_habilitada = True
        
        if f == CONEJO and col == DORADO:
            es_direccion_habilitada = d != SUR
        elif f == CONEJO and col == PLATEADO:
            es_direccion_habilitada = d != NORTE

    return es_direccion_habilitada


def puede_mover_a_secas(t: Tablero, pos: Posicion, d: Direccion) -> bool:
    """Verifica si la casilla donde se quiere mover la pieza esta vacia
    PRE:
        True

    Args:
        t (Tablero): Tablero a evaluar
        pos (Posicion): Posicion origen de la pieza
        d (Direccion): Direccion hacia donde se quiere mover la pieza

    Returns:
        Si la casilla contigua indicada esta vacia devuelve True, sino False.
    """
    return hay_casilla_vacia_hacia(t,pos,d)

#### Ejercicio 5


def activar_trampas(t: Tablero) -> Tablero:
    raise Exception("No implementado")


def tableros_coinciden_en_la_posicion(t1: Tablero, t2: Tablero, pos: Posicion) -> bool:  # Auxiliar
    """Verifica si ambos tableros tienen la misma pieza o casilla vacia en una posicion especifica (pasada por parametro)
    PRE:
        True

    Args:
        t1 (Tablero): Tablero a comparar
        t2 (Tablero): Tablero a comparar
        pos (Posicion): Posicion a evaluar

    Returns:
        Si las posiciones tienen el mismo valor devuelve True, sino False.
    """
    return t1[pos.fila][pos.columna] == t2[pos.fila][pos.columna]


def tableros_coinciden_salvo_en_la_posicion(t1: Tablero, t2: Tablero, pos: Posicion) -> bool:  # Auxiliar
    """Verifica si ambos tableros tienen los mismos valores en todas las posiciones salvo pos (pasada por parametro)
    PRE:
        True

    Args:
        t1 (Tablero): Tablero a comparar
        t2 (Tablero): Tablero a comparar
        pos (Posicion): Posicion a evaluar

    Returns:
        Si los tableros tienen el mismo valor en todas las posiciones menos la indicada devuelve True, sino False.
    """
    if tableros_coinciden_en_la_posicion(t1, t2, pos):
        return False

    numero_de_posiciones_coincidentes: int = 0
    for fila in range(0, 8):
        for columna in range(0, 8):
            if tableros_coinciden_en_la_posicion(t1, t2, Posicion(fila, columna)):
                numero_de_posiciones_coincidentes += 1

    return numero_de_posiciones_coincidentes == 63

def es_tablero_sacando_pieza(t0: Tablero, t1: Tablero, pos: Posicion) -> bool: # Auxiliar
    """Verifica si t1 es el mismo tablero que t0 pero con una pieza removida en pos
    PRE:
        True

    Args:
        t0 (Tablero): Tablero "inicial"
        t1 (Tablero): Posible tablero con una pieza removida
        pos (Posicion): Posicion a evaluar

    Returns:
        Si los tableros tienen el mismo valor en todas las posiciones y pos es una casilla vacia devuelve True, sino False.
    """
    return tableros_coinciden_salvo_en_la_posicion(t0, t1, pos) and hay_casilla_vacia(t1, pos)


#### Ejercicio 6


def realizar_movimiento(j: Juego, m: Movimiento) -> Juego:
    raise Exception("No implementado")


def es_tablero_poniendo_pieza(t0: Tablero, t1: Tablero, pos: Posicion, f: Figura, col: Color) -> bool:
    """Verifica si t1 es el tablero resultante de agregar (o cambiar) una pieza en la Posicion pos, de Figura f y Color col 
    PRE:
        True

    Args:
        t0 (Tablero): Tablero "inicial"
        t1 (Tablero): Posible tablero con una pieza removida
        pos (Posicion): Posicion a evaluar
        f (Figura): Figura de la pieza en tablero t1
        col (Color): Color de la pieza en tablero t1

    Returns:
        Si los tableros tienen el mismo valor en todas las posiciones y en t1[pos.fila][pos.columna] hay una pieza con Figura f y Color col True, sino False.
    """
    return tableros_coinciden_salvo_en_la_posicion(t0, t1, pos) and hay_figura_de_color(t1, pos, f, col)


def es_tablero_trasladando_pieza(t0: Tablero, t1: Tablero, pos_origen: Posicion, pos_destino: Posicion) -> bool: # Auxiliar
    """Verifica si t1 es el tablero resultante de mover a partir de t0 una pieza desde la pos_origen hacia pos_destino 
    PRE:
        True

    Args:
        t0 (Tablero): Tablero "inicial", estado anterior
        t1 (Tablero): Tablero "sucesor", estado posterior
        pos_origen (Posicion): Posicion desde donde parte la pieza
        pos_destino (Posicion): Posicion donde la pieza deberia haber ido

    Returns:
        Si en pos_origen hay una pieza, t0 es un estado previo y t1 es un estado posterior: True, sino False
        Existe f: Figura. Existe col: Color. Existe t_intermedio: Tablero. (
        hayFiguraDeColor (t0, pos_origen , f , col)
        ∧ esTableroSacandoPieza (t0 , t_intermedio , pos_origen )
        ∧ esTableroPoniendoPieza (t_intermedio , t1 , pos_destino , f , col)

    """
    pieza_origen: Pieza = t0[pos_origen.fila][pos_origen.columna]
    
    if pieza_origen == VACIA:
        return False

    f: Figura = pieza_origen.figura
    col: Color = pieza_origen.color

    t_intermedio: Tablero = genera_tablero_quitando_pieza_en_posicion(t0,pos_origen)

    return es_tablero_sacando_pieza(t0,t_intermedio,pos_origen) and es_tablero_poniendo_pieza(t_intermedio,t1,pos_destino,f,col)

def genera_tablero_quitando_pieza_en_posicion(t: Tablero, pos: Posicion) -> Tablero: # Auxiliar
    """Genera a partir de un tablero t, otro tablero valido sin la pieza indicada en pos
    PRE:
        True

    Args:
        t (Tablero): Tablero "inicial", estado anterior
        pos (Posicion): Posicion donde se quiere ubicar una casilla vacia

    Returns:
        Una copia de t con todas las posiciones iguales, salvo pos, cuya pieza (o vacia) es reemplazada por VACIA
    """
    t_nuevo: Tablero = []
    for fila in t:
        t_nuevo.append(fila.copy())
    
    t_nuevo[pos.fila][pos.columna] = VACIA

    return t_nuevo


def hay_que_cambiar_de_turno(j: Juego, m: Movimiento) -> bool: # Auxiliar
    """Contabiliza los pasos que se hicieron en un turno y verifica si se llego a la cantidad maxima
    PRE:
        True

    Args:
        j (Juego): Juego actual, contiene la cantidad de pasos ya consumidos
        m (Movimiento): Movimiento que se produce, suma la cantidad de pasos correspondiente

    Returns:
        Si la suma de pasos ya consumidos y la cantidad de pasos del moviemiento supera la maxima permitida por turno: True, sino False
    """
    pasos_totales: int = j.pasos_consumidos + len(m.pasos)

    return pasos_totales == MAX_PASOS


def juego_con_turno_posiblemente_avanzado(j0: Juego, j1: Juego, m: Movimiento) -> bool:
    """Verifica si un juego (j1) cambio de turno o no
    PRE:
        True

    Args:
        j0 (Juego): Estado del juego previo
        j1 (Juego): Estado del juego posterior
        m (Movimiento): Movimiento realizado, suma la cantidad de pasos correspondiente (si el turno cambia debe ser 0, sino suma la cantidad de pasos)

    Returns:
        Si j0 ya consumio sus pasos, j1 debe ser un nuevo turno y tener 0 pasos consumidos y,
        Si j0 no consumio sus pasos, j1 debe ser del mismo turno y tener la misma cantidad de pasos consumidos que su estado previo + actual jugado
        Caso contrario, devuelve False
        (hayQueCambiarDeTurno (j0, m) → (j1 . turno = oponente (j0.turno) ∧ j1.pasosConsumidos = 0))
        ∧ (¬hayQueCambiarDeTurno (j0, m) → (j1.turno = j0.turno ∧ j1.pasosConsumidos = j0.pasosConsumidos + |m.pasos|))

    """
    if hay_que_cambiar_de_turno(j0,m):
        es_avanzado: bool = j1.turno == oponente(j0.turno) and j1.pasos_consumidos == 0
    else:
        es_avanzado: bool = j1.turno == j0.turno and j1.pasos_consumidos == (j0.pasos_consumidos + len(m.pasos))

    return es_avanzado

#### Ejercicio 7

def posicion_en_fila_inicial(pos: Posicion, col: Color) -> bool:
    """
    Verifica si una p_propia se encuentra en su posición inicial

    Requires:
        True

    Arguments:
        pos (in Posicion): Posición de la p_propia
        col    (in Color): Color de la p_propia

    Returns:
        Bool: Si la pieza de cierto Color se encuentra en su fila inicial
            { (col = Dorado → pos. fila == 0) ∧ (col = Plateado → pos. fila == 7) }
    """
    p_dorada_en_inicial: bool = col == DORADO and pos.fila == 0
    p_plateada_en_inicial: bool = col == PLATEADO and pos.fila == 7

    return p_dorada_en_inicial or p_plateada_en_inicial


def hay_conejo_en_fila_inicial_oponente(j: Juego, col: Color)-> bool:
    """
    Verifica si hay un Conejo en la fila inicial del oponente

    PRE:
        True

    Args:
        j (Juego): Juego a evaluar
        col (Color): Color del conejo del cual se evalúa su posición

    Returns:
        bool: Si hay un Conejo en la fila inicial del oponente
    """
    fila_inicial_oponente: int = 0 if oponente(col) == DORADO else 7

    for columna in range(0,8):
        if hay_figura_de_color(j.tablero, Posicion(fila_inicial_oponente,columna), CONEJO, col):
            return True

    return False


def es_inicio_de_turno(j: Juego, col: Color) -> bool:
    """Verifica si un juego (j) es el primero de un turno
    PRE:
        True

    Args:
        j (Juego): Juego a evaluar
        col (Color): Color del turno

    Returns:
        Si el turno del juego coincide con el color pasado por parametro y todavia no se consumieron pasos: True, sino False
    """
    return j.turno == col and j.pasos_consumidos == 0


def hay_conejo_en_tablero(j: Juego, col: Color) -> bool:
    """Verifica si hay al menos un conejo en el tablero

    PRE:
        es_juego_valido(j)

    Args:
        j (Juego): Juego a evaluar
        col (Color): Color del conejo del cual se evalua su existencia

    Returns:
        Si en alguna posicion valida del tablero hay un conejo: True, sino False
        Existe pos: Posición. hayFiguraDeColor (j.tablero, pos, Conejo, col)
    """
    for fila in range(0,8):
        for columna in range(0,8):
            if hay_figura_de_color(j.tablero,Posicion(fila,columna),CONEJO,col):
                return True

    return False


def hay_ganador_determinado(j: Juego) -> bool:
    raise Exception("No implementado")


def ganador_del_juego(j: Juego) -> Color:
    raise Exception("No implementado")
