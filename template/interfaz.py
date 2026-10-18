import sys
import tkinter

import arimaa as aa

U_PX = 8
CASILLA_PX = 10 * U_PX
MARGEN_MARCA_TRAMPA_PX = U_PX
BORDE_PX = U_PX
MARGEN_PX = 5 * U_PX

COLOR_BORDE = "#000000"
COLOR_CASILLA_CLARA = "#ececec"
COLOR_CASILLA_OSCURA = "#cccccc"
COLOR_CASILLA_TRAMPA = "#ffb3b3"
COLOR_CASILLA_SEL1 = "#000080"
COLOR_CASILLA_SEL2 = "#800000"
COLOR_MARCA_TRAMPA = "#4d4d4d"
COLOR_GANADOR_FG = "#ffffff"
COLOR_GANADOR_BG = "#a00000"

FUENTE = "Helvetica"
TAM_FUENTE = int(CASILLA_PX * 0.35)

POSICIONES = [aa.Posicion(i, j) for i in range(aa.ALTO) for j in range(aa.ANCHO)]
FIGURAS = {
    aa.ELEFANTE: "e",
    aa.CAMELLO: "m",
    aa.CABALLO: "h",
    aa.PERRO: "d",
    aa.GATO: "c",
    aa.CONEJO: "r",
}

COLORES = {
    aa.DORADO: "g",
    aa.PLATEADO: "s",
}

PIEZAS = [aa.Pieza(f, col) for f in FIGURAS.keys() for col in COLORES.keys()]


class GTablero(tkinter.Canvas):
    def __init__(self, parent):
        self.garimaa = parent
        self.ancho = 2 * BORDE_PX + aa.ANCHO * CASILLA_PX
        self.alto = 2 * BORDE_PX + aa.ALTO * CASILLA_PX
        super().__init__(parent, width=self.ancho, height=self.alto)
        self.cargar_imagenes()
        self.bind("<Button-1>", self.on_click)

    ## Manejo de eventos

    def on_click(self, evt):
        if self.coordenada_en_tablero(evt.x, evt.y):
            pos = self.coordenada_a_posicion(evt.x, evt.y)
            self.garimaa.click_en_posicion(pos)

    ## Conversión entre posiciones y coordenadas

    def posicion_a_coordenada(self, pos):
        x = BORDE_PX + pos.columna * CASILLA_PX
        y = BORDE_PX + (aa.ALTO - pos.fila - 1) * CASILLA_PX
        return x, y

    def posicion_a_bordes_casilla(self, pos):
        (x0, y0) = self.posicion_a_coordenada(pos)
        x1 = x0 + CASILLA_PX
        y1 = y0 + CASILLA_PX
        return x0, y0, x1, y1

    def coordenada_en_tablero(self, x, y):
        return (
            BORDE_PX <= x
            and x <= BORDE_PX + CASILLA_PX * aa.ANCHO
            and BORDE_PX <= y
            and y <= BORDE_PX + CASILLA_PX * aa.ALTO
        )

    def coordenada_a_posicion(self, x, y):
        columna = (x - BORDE_PX) // CASILLA_PX
        fila = aa.ALTO - (y - BORDE_PX) // CASILLA_PX - 1
        return aa.Posicion(fila, columna)

    ## Métodos para dibujar el tablero

    def cargar_imagen(self, pieza):
        fn = "piezas/" + FIGURAS[pieza.figura] + COLORES[pieza.color] + ".png"
        return tkinter.PhotoImage(file=fn)

    def cargar_imagenes(self):
        self.imgs = {}
        for pieza in PIEZAS:
            self.imgs[pieza] = self.cargar_imagen(pieza)

    def color_casilla(self, pos, seleccionadas):
        if len(seleccionadas) >= 1 and pos == seleccionadas[0]:
            return COLOR_CASILLA_SEL1
        elif len(seleccionadas) >= 2 and pos == seleccionadas[1]:
            return COLOR_CASILLA_SEL2
        elif pos in aa.POSICIONES_TRAMPA:
            return COLOR_CASILLA_TRAMPA
        elif (pos.fila + pos.columna) % 2 == 0:
            return COLOR_CASILLA_OSCURA
        else:
            return COLOR_CASILLA_CLARA

    def marcar_trampa(self, pos):
        x0, y0, x1, y1 = self.posicion_a_bordes_casilla(pos)
        color = COLOR_MARCA_TRAMPA
        m = MARGEN_MARCA_TRAMPA_PX
        self.create_line(x0 + m, y0 + m, x1 - m, y1 - m, fill=color, width=m)
        self.create_line(x0 + m, y1 - m, x1 - m, y0 + m, fill=color, width=m)

    def dibujar_celda(self, pos, seleccionadas):
        x0, y0, x1, y1 = self.posicion_a_bordes_casilla(pos)
        color = self.color_casilla(pos, seleccionadas)
        self.create_rectangle(x0, y0, x1, y1, fill=color, outline="")
        if pos in aa.POSICIONES_TRAMPA:
            self.marcar_trampa(pos)

    def dibujar_pieza(self, pos, pieza):
        x0, y0, x1, y1 = self.posicion_a_bordes_casilla(pos)
        x = (x0 + x1) // 2
        y = (y0 + y1) // 2
        self.create_image(x, y, image=self.imgs[pieza])

    def dibujar_tablero(self, tablero, casillas_seleccionadas):
        self.delete("all")
        self.create_rectangle(0, 0, self.ancho, self.alto, fill=COLOR_BORDE)
        for pos in POSICIONES:
            self.dibujar_celda(pos, casillas_seleccionadas)
            c = aa.casilla_en_posicion(tablero, pos)
            if c != aa.VACIA:
                self.dibujar_pieza(pos, c)


class Status:
    def __init__(self) -> None:
        self.turno = None
        self.pasos_remanentes = None
        self.puede_undo = None
        self.puede_redo = None
        self.puede_pasar = None
        self.ganador = None


class GStatus(tkinter.Frame):
    def __init__(self, parent):
        self.garimaa = parent
        super().__init__(parent)
        self.cargar_imagenes()
        self.boton_undo = tkinter.Button(
            self, text="◀", command=self.undo, font=(FUENTE, TAM_FUENTE)
        )
        self.boton_redo = tkinter.Button(
            self, text="▶", command=self.redo, font=(FUENTE, TAM_FUENTE)
        )
        self.gturno = tkinter.Canvas(self, width=CASILLA_PX + 2, height=CASILLA_PX + 2)
        self.gpasos = tkinter.Label(self, font=(FUENTE, TAM_FUENTE, "bold"))
        self.boton_pasar = tkinter.Button(
            self,
            text="Pasar",
            command=self.pasar_turno,
            font=(FUENTE, TAM_FUENTE, "bold"),
        )
        self.boton_undo.pack(side=tkinter.LEFT, pady=U_PX)
        self.boton_redo.pack(side=tkinter.LEFT, padx=2 * U_PX, pady=U_PX)
        self.gturno.pack(side=tkinter.LEFT, pady=U_PX)
        self.gpasos.pack(side=tkinter.LEFT, pady=U_PX)
        self.boton_pasar.pack(side=tkinter.LEFT, padx=5 * U_PX, pady=U_PX)

    def cargar_imagenes(self):
        self.imgs = {}
        for color in COLORES.keys():
            self.imgs[color] = self.cargar_imagen(color)

    def cargar_imagen(self, color):
        fn = "piezas/" + "turno_" + COLORES[color] + ".png"
        return tkinter.PhotoImage(file=fn)

    def dibujar_status(self, status):
        if status.ganador is None:
            self.dibujar_status_sin_ganador(status)
        else:
            self.dibujar_status_con_ganador(status)

    def dibujar_status_con_ganador(self, status):
        x = CASILLA_PX / 2
        y = CASILLA_PX / 2
        self.gturno.delete("all")
        self.gturno.create_image(x, y, image=self.imgs[status.ganador])
        self.gpasos.config(
            text="GANA", fg=COLOR_GANADOR_FG, bg=COLOR_GANADOR_BG, padx=10, pady=4
        )
        self.habilitar_boton(self.boton_undo, status.puede_undo)
        self.habilitar_boton(self.boton_redo, False)
        self.habilitar_boton(self.boton_pasar, False)

    def dibujar_status_sin_ganador(self, status):
        x = CASILLA_PX / 2
        y = CASILLA_PX / 2
        self.gturno.delete("all")
        self.gturno.create_image(x, y, image=self.imgs[status.turno])
        self.gpasos.config(
            text=str(status.pasos_remanentes),
            fg="black",
            bg=self.cget("bg"),
            padx=1,
            pady=1,
        )
        self.habilitar_boton(self.boton_undo, status.puede_undo)
        self.habilitar_boton(self.boton_redo, status.puede_redo)
        self.habilitar_boton(self.boton_pasar, status.puede_pasar)

    def habilitar_boton(self, boton, flag_habilitado):
        if flag_habilitado:
            boton.config(relief=tkinter.RAISED, bd=2, state=tkinter.NORMAL)
        else:
            boton.config(relief=tkinter.FLAT, bd=0, state=tkinter.DISABLED)

    def undo(self):
        self.garimaa.undo()

    def redo(self):
        self.garimaa.redo()

    def pasar_turno(self):
        self.garimaa.pasar_turno()


class GArimaa(tkinter.Tk):
    def __init__(self, juego):
        super().__init__()
        self.title("Arimaa")

        self.juego = juego
        self.gtablero = GTablero(self)
        self.gtablero.pack(pady=(MARGEN_PX, 0))
        self.gstatus = GStatus(self)
        self.gstatus.pack()

        # self.seleccionadas es la lista de casillas seleccionadas
        # para hacer un movimiento.
        # Invariante:
        # - Su longitud varía entre 0 y 2.
        # - Sus elementos son casillas que contienen piezas y vecinas entre sí.
        self.seleccionadas = []
        self.historia = [self.juego]
        self.posicion_historia = 0
        self.redibujar()
        self.bind("<Escape>", self.salir)

    def salir(self, evt):
        self.destroy()

    def click_en_posicion(self, pos):
        if not aa.posicion_en_tablero(pos):
            self.seleccionadas = []
            return
        es_vacia = aa.casilla_en_posicion(self.juego.tablero, pos) == aa.VACIA
        if len(self.seleccionadas) == 0:
            if not es_vacia:
                self.seleccionadas.append(pos)
        elif len(self.seleccionadas) == 1:
            ultima = self.seleccionadas[-1]
            son_vecinas = aa.son_posiciones_vecinas(ultima, pos)
            if pos == ultima:
                self.seleccionadas = []
            elif son_vecinas and es_vacia:
                self.tratar_de_mover(self.seleccionadas, pos)
                self.seleccionadas = []
            elif son_vecinas and not es_vacia:
                self.seleccionadas.append(pos)
            elif not es_vacia and pos != ultima:
                self.seleccionadas = [pos]
            else:
                self.seleccionadas = []
        elif len(self.seleccionadas) == 2:
            p0 = self.seleccionadas[0]
            p1 = self.seleccionadas[1]
            son_vecinas = aa.son_posiciones_vecinas(
                p0, pos
            ) or aa.son_posiciones_vecinas(p1, pos)
            if son_vecinas and es_vacia:
                self.tratar_de_mover(self.seleccionadas, pos)
                self.seleccionadas = []
            elif not es_vacia and pos not in self.seleccionadas:
                self.seleccionadas = [pos]
            else:
                self.seleccionadas = []
        self.redibujar()

    def tratar_de_mover(self, posiciones, destino):
        assert len(posiciones) in [1, 2]
        if len(posiciones) == 1:
            d = aa.direccion_desde_hasta(posiciones[0], destino)
            m = aa.Movimiento(aa.MOVER_A_SECAS, posiciones[0], [d])
        elif len(posiciones) == 2:
            if aa.son_posiciones_vecinas(posiciones[0], destino):
                posiciones = [posiciones[1], posiciones[0]]
            col0 = aa.casilla_en_posicion(self.juego.tablero, posiciones[0]).color
            if col0 != self.juego.turno:
                d = aa.direccion_desde_hasta(posiciones[1], destino)
                d_arrastre = aa.direccion_desde_hasta(posiciones[0], posiciones[1])
                m = aa.Movimiento(aa.ARRASTRAR, posiciones[1], [d, d_arrastre])
            else:
                d = aa.direccion_desde_hasta(posiciones[0], posiciones[1])
                d_empuje = aa.direccion_desde_hasta(posiciones[1], destino)
                m = aa.Movimiento(aa.EMPUJAR, posiciones[0], [d, d_empuje])
        if not aa.hay_ganador_determinado(self.juego) and aa.puede_realizar_movimiento(
            self.juego, m
        ):
            self.realizar_movimiento(m)

    def realizar_movimiento(self, m):
        self.juego = aa.realizar_movimiento(self.juego, m)
        self.registrar_historia()

    def pasar_turno(self):
        self.juego = aa.pasar_turno(self.juego)
        self.registrar_historia()

    def registrar_historia(self):
        if self.posicion_historia < len(self.historia) - 1:
            self.historia = self.historia[: self.posicion_historia + 1]
        self.historia.append(self.juego)
        self.posicion_historia += 1
        self.seleccionadas = []
        self.redibujar()

    def undo(self):
        if self.posicion_historia > 0:
            self.posicion_historia -= 1
            self.juego = self.historia[self.posicion_historia]
        self.seleccionadas = []
        self.redibujar()

    def redo(self):
        if self.posicion_historia < len(self.historia) - 1:
            self.posicion_historia += 1
            self.juego = self.historia[self.posicion_historia]
        self.seleccionadas = []
        self.redibujar()

    def redibujar(self):
        self.gtablero.dibujar_tablero(self.juego.tablero, self.seleccionadas)
        status = Status()
        status.turno = self.juego.turno
        status.pasos_remanentes = aa.MAX_PASOS - self.juego.pasos_consumidos
        status.puede_undo = self.posicion_historia > 0
        status.puede_redo = self.posicion_historia < len(self.historia) - 1
        status.puede_pasar = self.juego.pasos_consumidos > 0
        if aa.hay_ganador_determinado(self.juego):
            status.ganador = aa.ganador_del_juego(self.juego)
        else:
            status.ganador = None
        self.gstatus.dibujar_status(status)


TABLERO_INICIAL_POR_DEFECTO = [
    "rrrrrrrr",  # 7
    "ccddhhme",  # 6
    "--------",  # 5
    "--------",  # 4
    "--------",  # 3
    "--------",  # 2
    "EMHHDDCC",  # 1
    "RRRRRRRR",  # 0
    # 01234567
]


def mostrar_opciones():
    sys.stderr.write(f"Opciones:\n")
    sys.stderr.write(
        f"    tablero.txt : Carga el tablero desde el archivo especificado.\n"
    )
    sys.stderr.write(f"    -d          : Empieza el dorado.\n")
    sys.stderr.write(f"    -p          : Empieza el plateado.\n")
    sys.stderr.write(f"    -0          : Empieza con 0 pasos consumidos.\n")
    sys.stderr.write(f"    -1          : Empieza con un paso consumido.\n")
    sys.stderr.write(f"    -2          : Empieza con dos pasos consumidos.\n")
    sys.stderr.write(f"    -3          : Empieza con tres pasos consumidos.\n")


if __name__ == "__main__":
    mostrar_opciones()
    tablero = aa.leer_tablero(TABLERO_INICIAL_POR_DEFECTO)
    turno = aa.DORADO
    pasos_consumidos = 0
    for arg in sys.argv[1:]:
        if arg == "-d":
            turno = aa.DORADO
        elif arg == "-p":
            turno = aa.PLATEADO
        elif arg == "-0":
            pasos_consumidos = 0
        elif arg == "-1":
            pasos_consumidos = 1
        elif arg == "-2":
            pasos_consumidos = 2
        elif arg == "-3":
            pasos_consumidos = 3
        else:
            tablero = aa.leer_tablero_de_archivo(arg)
    juego = aa.Juego(tablero, turno, pasos_consumidos)
    g = GArimaa(juego)
    g.mainloop()
