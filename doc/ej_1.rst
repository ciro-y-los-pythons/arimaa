py:function:: tablero_bien_formado(t: Tablero) -> bool

   Verifica si el Tablero se encuentra con las medidas correspondientes (8 x 8).

   :param t: Tablero a verificar.
   :type t: Tablero
   :returns: True si el tablero cumple con las medidas correspondientes, False en caso contrario.
             (:math:`|t| = \text{ALTO} \land \forall i : \mathbb{Z}. (0 \le i < |t| \to |t[i]| = \text{ANCHO})`)
   :rtype: bool
