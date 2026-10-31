## Comandos útiles

1. Para hacer chequeo de tipos del código:

```Shell
python -m mypy arimaa.py
```

2. Para correr los casos de test:

```Shell
python -m unittest test.tests.py
```

3. Para evaluar el cubrimiento del código por los casos de test:

```Shell
python -m coverage run --include arimaa.py --branch -m unittest test.tests.py
```

```Shell
python -m coverage json
```

```Shell
python cubrimiento.py
```

4. Para correr la interfaz gráfica:

```Shell
python interfaz.py
```

Para cargar el tablero desde el archivo especificado, se le puede pasar
como parámetro un nombre de archivo (p.ej. "tablero.txt").

Además, se aceptan las siguientes opciones:
-d Empieza el dorado.
-p Empieza el plateado.
-0 Empieza con 0 pasos consumidos.
-1 Empieza con un paso consumido.
-2 Empieza con dos pasos consumidos.
-3 Empieza con tres pasos consumidos.

Por ejemplo:

```Shell
python interfaz.py tablero.txt -p -1
```

Inicia el juego desde el tablero dado, donde comienzan las plateadas
que ya consumieron 1 paso (y por lo tanto le quedan tres pasos).

Nota: la interfaz gráfica sólo funcionará correctamente una vez que toda la
funcionalidad del TP se encuentre implementada. De lo contrario, pueden
experimentar comportamientos difíciles de predecir.

5. Formato de los archivos de tablero:

Los archivos de tablero deben ser de 8 líneas y 8 columnas.

Cada celda puede ser "-" (vacía) o una pieza.
Las letras mayúsculas representan piezas doradas y las minúsculas piezas plateadas:
E/e : Elephant (elefante)
M/m : Camel (camello)
H/h : Horse (caballo)
D/d : Dog (perro)
C/c : Cat (gato)
R/r : Rabit (conejo)

Por ejemplo:

```
rrrrrrrr
ccddhhme
--------
--------
--------
--------
EMHHDDCC
RRRRRRRR
```
