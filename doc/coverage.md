# Coverage

## Última Actualización

+ Realizada: 30/10, 21:36
+ Ultimo commit: `REFACTOR #07 - tests del ejercicio_6`
+ Resultado:

```Shell
=== Análisis de Coverage ===

➡️  Porcentaje global de líneas cubiertas (1956/2045): 95.65%
➡️  Porcentaje global de ramas cubiertas (137/184): 74.46%
```

## ¿Como se genera el Coverage?

1. Ejecutar los tests con coverage:

```Shell
PYTHONPATH=src python3 -m coverage run --branch -m unittest discover -s test
```

2. Generar el archivo JSON:

```Shell
python3 -m coverage json
```

3. Ejecutar tu script de cubrimiento

```Shell
python3 template/cubrimiento.py
```

## Archivo del Coverage

[./template/cubrimiento.py](./template/cubrimiento.py)

## ¿Por qué se ignoran ciertos archivos del Coverage?

NO es recomendable trackear ni subir el archivo `.coverage` ni el `coverage.json` al Repo.

Estos archivos se consideran artefactos de compilación o de pruebas locales (build/test artifacts) por las siguientes razones:

1. Son generados automáticamente: Deben ser el resultado de ejecutar tus tests en tu máquina o en un servidor de integración continua (como GitHub Actions). Subirlos al repositorio no aporta valor real al código fuente.

2. Pueden generar conflictos (merge conflicts): Como cambian constantemente cada vez que ejecutas los tests (incluso si la lógica del código no cambia, cambian las marcas de tiempo, líneas recorridas o porcentajes), si trabajas en equipo o desde distintas PCs vas a tener conflictos innecesarios en Git.

3. Dependen del entorno: Las rutas absolutas o los archivos ejecutados pueden variar de una computadora a otra, haciendo que los reportes locales no sean universales.
