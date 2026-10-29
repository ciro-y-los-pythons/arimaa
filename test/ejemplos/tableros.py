from src.arimaa import leer_tablero


def tablero_8x8_vacio():
    return leer_tablero(
        [
            "--------",  # 7
            "--------",  # 6
            "--------",  # 5
            "--------",  # 4
            "--------",  # 3
            "--------",  # 2
            "--------",  # 1
            "--------",  # 0
            # 01234567
        ]
    )


def tablero_8x8_inicial_ejemplo():
    """
    ```
    Tablero Inicial (0 jugadas):
    | h c d m e d c h | 7
    | r r r r r r r r | 6
    | - - - - - - - - | 5
    | - - - - - - - - | 4
    | - - - - - - - - | 3
    | - - - - - - - - | 2
    | R R R R R R R R | 1
    | H C D M E D C H | 0
      0 1 2 3 4 5 6 7
    ```
    """
    return leer_tablero(
        [
            "hcdmedch",  # 7
            "rrrrrrrr",  # 6
            "--------",  # 5
            "--------",  # 4
            "--------",  # 3
            "--------",  # 2
            "RRRRRRRR",  # 1
            "HCDMEDCH",  # 0
            # 01234567
        ]
    )


def tablero_8x8_mueve_conejo_dorado_h3():
    """
    ```
    Tablero Inicial (1 jugada):
    | h c d m e d c h | 7
    | r r r r r r r r | 6
    | - - - - - - - - | 5
    | - - - - - - - - | 4
    | - - - - - - - - | 3
    | - - - - - - - R | 2
    | R R R R R R R - | 1
    | H C D M E D C H | 0
      0 1 2 3 4 5 6 7
    ```
    """
    return leer_tablero(
        [
            "hcdmedch",  # 7
            "rrrrrrrr",  # 6
            "--------",  # 5
            "--------",  # 4
            "--------",  # 3
            "-------R",  # 2
            "RRRRRRR-",  # 1
            "HCDMEDCH",  # 0
            # 01234567
        ]
    )


def tablero_8x8_empezando():
    """
    ```
    Tablero Recién Empezando:
    | h c d m e d c h | 7
    | r r r - r r - - | 6
    | - - - - - - r r | 5
    | - - - r - - - - | 4
    | R - - R - - - - | 3
    | - - - - - - - - | 2
    | - R R - R R R R | 1
    | H C D M E D C H | 0
      0 1 2 3 4 5 6 7
    ```
    """
    return leer_tablero(
        [
            "hcdmedch",  # 7
            "rrr-rr--",  # 6
            "------rr",  # 5
            "---r----",  # 4
            "R--R----",  # 3
            "--------",  # 2
            "-RR-RRRR",  # 1
            "HCDMEDCH",  # 0
            # 01234567
        ]
    )


def tablero_8x8_ya_empezado():
    """
    ```
    Tablero Ya Empezado:
    | R - e - - m R r | 7
    | - - - - - - d E | 6
    | h - - R r - R R | 5
    | c - - R - C - - | 4
    | - r C H D r r - | 3
    | - - - - r c - - | 2
    | h - R - M - R - | 1
    | r r - D - d H - | 0
      0 1 2 3 4 5 6 7
    ```
    """
    return leer_tablero(
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

def tablero_8x8_ya_empezado_mueve_camello_plateado_a4():
    """
    ```
    Tablero Ya Empezado:
    | R - e - - m R r | 7
    | - - - - - - d E | 6
    | h - - R r - R R | 5
    | - - - R - C - - | 4
    | c r C H D r r - | 3
    | - - - - r c - - | 2
    | h - R - M - R - | 1
    | r r - D - d H - | 0
      0 1 2 3 4 5 6 7
    ```
    """
    return leer_tablero(
        [
            "R-e--mRr",  # 7
            "------dE",  # 6
            "h--Rr-RR",  # 5
            "---R-C--",  # 4
            "crCHDrr-",  # 3
            "----rc--",  # 2
            "h-R-M-R-",  # 1
            "rr-D-dH-",  # 0
            # 01234567
        ]
    )



def tablero_8x8_ya_finalizando():
    """
    ```
    Tablero Ya Finalizando:
    | - - - - - - - h | 7
    | - - - - - - - R | 6
    | - R - - - - - - | 5
    | - - - - c - - - | 4
    | - - - - R - - - | 3
    | - - - - - - - - | 2
    | - - - - - - - - | 1
    | r - - - - - - - | 0
      0 1 2 3 4 5 6 7
    ```
    """
    return leer_tablero(
        [
            "-------h",  # 7
            "-------R",  # 6
            "-R------",  # 5
            "----c---",  # 4
            "----R---",  # 3
            "--------",  # 2
            "r-------",  # 1
            "--------",  # 0
            # 01234567
        ]
    )


def tablero_8x8_ya_finalizando_v2():
    """
    ```
    Tablero Ya Finalizando (igual al anterior, con un caballo dorado en b6):
    | - - - - - - - h | 7
    | - - - - - - - R | 6
    | - H - - - - - - | 5
    | - - - - c - - - | 4
    | - - - - R - - - | 3
    | - - - - - - - - | 2
    | - - - - - - - - | 1
    | r - - - - - - - | 0
      0 1 2 3 4 5 6 7
    ```
    """
    return leer_tablero(
        [
            "-------h",  # 7
            "-------R",  # 6
            "-H------",  # 5
            "----c---",  # 4
            "----R---",  # 3
            "--------",  # 2
            "r-------",  # 1
            "--------",  # 0
            # 01234567
        ]
    )


def tablero_mal_formado_filas_ejemplo():
    return leer_tablero(
        [
            "hcdmedch",  # 7
            "rrrrrrrr",  # 6
            "--------",  # 5
            "-----",  # 4
            "--------",  # 3
            "--------",  # 2
            "RRRRRRRR",  # 1
            "HCDMEDCH",  # 0
            # 01234567
        ]
    )


def tablero_mal_formado_columnas_ejemplo():
    return leer_tablero(
        [
            "rrrrrrrr",  # 6
            "--------",  # 5
            "--------",  # 4
            "--------",  # 3
            "--------",  # 2
            "RRRRRRRR",  # 1
            "HCDMEDCH",  # 0
            # 01234567
        ]
    )


def tablero_8x8_inicial_falta_un_conejo_dorado_en_h2():
    return leer_tablero(
        [
            "hcdmedch",  # 7
            "rrrrrrrr",  # 6
            "--------",  # 5
            "--------",  # 4
            "--------",  # 3
            "--------",  # 2
            "RRRRRRR-",  # 1
            "HCDMEDCH",  # 0
            # 01234567
        ]
    )


def tablero_8x8_sin_conejos_dorados():
    """
    ```
    Tablero Sin Conejos :
    | - - - - - - - h | 7
    | - - - - - - - - | 6
    | - H - - - - - - | 5
    | - - - - c - - - | 4
    | - - - - - - - - | 3
    | - - - - - - - - | 2
    | - - - - - - - - | 1
    | r - - - - - - - | 0
      0 1 2 3 4 5 6 7
    ```
    """
    return leer_tablero(
        [
            "-------h",  # 7
            "--------",  # 6
            "-H------",  # 5
            "----c---",  # 4
            "--------",  # 3
            "--------",  # 2
            "r-------",  # 1
            "--------",  # 0
            # 01234567
        ]
    )


def tablero_8x8_camello_plateado_en_trampa():
    """
    ```
    Camello en (2,5) casilla trampa,
    debe ser quitado del tablero:
    | R - e - - m R r | 7
    | - - - - - - d E | 6
    | h - - R r - R R | 5
    | c - - R - C - - | 4
    | - r C H D - - - | 3
    | - - - - - c - - | 2
    | h - R - M - R - | 1
    | r r - D - d H - | 0
      0 1 2 3 4 5 6 7
    (basado en tablero_8x8_ya_empezado)
    ```
    """
    return leer_tablero(
        [
            "R-e--mRr",  # 7
            "------dE",  # 6
            "h--Rr-RR",  # 5
            "c--R-C--",  # 4
            "-rCHD---",  # 3
            "-----c--",  # 2
            "h-R-M-R-",  # 1
            "rr-D-dH-",  # 0
            # 01234567
        ]
    )

def tablero_8x8_camello_plateado_en_trampa_quitado():
    """
    ```
    Camello en (2,5) casilla trampa,
    ya fue quitado del tablero:
    | R - e - - m R r | 7
    | - - - - - - d E | 6
    | h - - R r - R R | 5
    | c - - R - C - - | 4
    | - r C H D - - - | 3
    | - - - - - - - - | 2
    | h - R - M - R - | 1
    | r r - D - d H - | 0
      0 1 2 3 4 5 6 7
    (basado en tablero_8x8_ya_empezado)
    ```
    """
    return leer_tablero(
        [
            "R-e--mRr",  # 7
            "------dE",  # 6
            "h--Rr-RR",  # 5
            "c--R-C--",  # 4
            "-rCHD---",  # 3
            "--------",  # 2
            "h-R-M-R-",  # 1
            "rr-D-dH-",  # 0
            # 01234567
        ]
    )

def tablero_8x8_piezas_en_todas_las_trampas_pero_con_amigas():
    """
    ```
    | h c d m e d c h | 7
    | r - - r r - - r | 6
    | - r r - - r r - | 5
    | - - - - - - - - | 4
    | - - - - - - - - | 3
    | - R R - - R R - | 2
    | R - - R R - - R | 1
    | H C D M E D C H | 0
      0 1 2 3 4 5 6 7
    
    Las cuatro trampas ((2,2), (2,5), (5,2), (5,5)) tienen piezas, pero hay piezas amigas al lado de cada una.
    ```
    """
    return leer_tablero(
        [
            "hcdmedch",  # 7
            "r--rr--r",  # 6
            "-rr--rr-",  # 5
            "--------",  # 4
            "--------",  # 3
            "-RR--RR-",  # 2
            "R--RR--R",  # 1
            "HCDMEDCH",  # 0
            # 01234567
        ]
    )

def tablero_8x8_piezas_en_todas_las_trampas_sin_amigas_1():
    """
    ```
    | h c d m e d c h | 7
    | r - - r r - - r | 6
    | - - r - - r - - | 5
    | - - - - - - - - | 4
    | - - - - - - - - | 3
    | - - R - - R - - | 2
    | R - - R R - - R | 1
    | H C D M E D C H | 0
      0 1 2 3 4 5 6 7
    
    Las cuatro trampas ((2,2), (2,5), (5,2), (5,5)) tienen piezas, no hay amigas contiguas
    Es una situacion hipotetica un poco ridicula, pero sirve para el test de activar todas las trampas
    ```
    """
    return leer_tablero(
        [
            "hcdmedch",  # 7
            "r--rr--r",  # 6
            "--r--r--",  # 5
            "--------",  # 4
            "--------",  # 3
            "--R--R--",  # 2
            "R--RR--R",  # 1
            "HCDMEDCH",  # 0
            # 01234567
        ]
    )

def tablero_8x8_piezas_en_todas_las_trampas_sin_amigas_2():
    """
    ```
    | h c d m e d c h | 7
    | r - - r r - - r | 6
    | - - - - - - - - | 5
    | - - - - - - - - | 4
    | - - - - - - - - | 3
    | - - - - - - - - | 2
    | R - - R R - - R | 1
    | H C D M E D C H | 0
      0 1 2 3 4 5 6 7
    
    Estado posterior a tablero_8x8_piezas_en_todas_las_trampas_sin_amigas_1
    ```
    """
    return leer_tablero(
        [
            "hcdmedch",  # 7
            "r--rr--r",  # 6
            "--------",  # 5
            "--------",  # 4
            "--------",  # 3
            "--------",  # 2
            "R--RR--R",  # 1
            "HCDMEDCH",  # 0
            # 01234567
        ]
    )
