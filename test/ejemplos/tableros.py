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

