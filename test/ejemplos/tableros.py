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


def tablero_8x8_empezando():
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


def tablero_8x8_ya_finalizando():
    """
    Tablero Ya Finalizando:
    | - - - - - - - h | 7\n
    | - - - - - - - R | 6\n
    | - R - - - - - - | 5\n
    | - - - - c - - - | 4\n
    | - - - - R - - - | 3\n
    | - - - - - - - - | 2\n
    | - - - - - - - - | 1\n
    | r - - - - - - - | 0\n
      0 1 2 3 4 5 6 7
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
