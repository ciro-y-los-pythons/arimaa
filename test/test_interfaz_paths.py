from pathlib import Path

import template.interfaz as interfaz


def test_rutas_de_imagenes_son_absolutas_y_compatibles_con_la_plantilla():
    assert interfaz.PIEZAS_DIR == Path(interfaz.__file__).resolve().parent / "piezas"
    assert interfaz.ruta_imagen_turno(interfaz.aa.DORADO) == interfaz.PIEZAS_DIR / "turno_g.png"
    assert interfaz.ruta_imagen_pieza(interfaz.aa.Pieza(interfaz.aa.ELEFANTE, interfaz.aa.DORADO)) == interfaz.PIEZAS_DIR / "eg.png"
