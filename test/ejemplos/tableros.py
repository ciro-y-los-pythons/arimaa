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
    Tablero Inicial (0 jugadas):
    | h c d m e d c h | 7\n
    | r r r r r r r r | 6\n
    | - - - - - - - - | 5\n
    | - - - - - - - - | 4\n
    | - - - - - - - - | 3\n
    | - - - - - - - - | 2\n
    | R R R R R R R R | 1\n
    | H C D M E D C H | 0\n
      0 1 2 3 4 5 6 7
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
    Tablero Inicial (0 jugadas):
    | h c d m e d c h | 7\n
    | r r r r r r r r | 6\n
    | - - - - - - - - | 5\n
    | - - - - - - - - | 4\n
    | - - - - - - - - | 3\n
    | - - - - - - - R | 2\n
    | R R R R R R R - | 1\n
    | H C D M E D C H | 0\n
      0 1 2 3 4 5 6 7
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
    Tablero Recién Empezando:
    | h c d m e d c h | 7\n
    | r r r - r r - - | 6\n
    | - - - - - - r r | 5\n
    | - - - r - - - - | 4\n
    | R - - R - - - - | 3\n
    | - - - - - - - - | 2\n
    | - R R - R R R R | 1\n
    | H C D M E D C H | 0\n
      0 1 2 3 4 5 6 7
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
    Tablero Ya Empezado:
    | R - e - - m R r | 7\n
    | - - - - - - d E | 6\n
    | h - - R r - R R | 5\n
    | c - - R - C - - | 4\n
    | - r C H D r r - | 3\n
    | - - - - r c - - | 2\n
    | h - R - M - R - | 1\n
    | r r - D - d H - | 0\n
      0 1 2 3 4 5 6 7
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


def tablero_8x8_ya_finalizando_v2():
    """
    Tablero Ya Finalizando (igual al anterior, con un caballo dorado en b6):
    | - - - - - - - h | 7\n
    | - - - - - - - R | 6\n
    | - H - - - - - - | 5\n
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
