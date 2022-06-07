# Degradado ascii y decorador

## ventana_ascii_funciones.py

La función create_window(list) espera una lista de strings y la devuelve con un marco en caracteres ascii:

```python
lista = ["Hola mundo", "Esto es una prueba"]
    create_window(lista)
╔═════════════════▬□x╗
║     Hola mundo     ║
║ Esto es una prueba ║
╚════════════════════╝    
```

## degradado.py

La funcion crea_degradado espera una lista de caracteres con las que creara un degradado en la pantalla y luego las encapsula dentro de un marco usando la funcion create_window()

La función crea_linea(*lista*, *largo_linea*) espera una lista de caracteres y un valor de ancho de linea.

crea_linea elige un caracter inicial aleatorio al comienzo y despues sigue añadiendo teniendo en cuenta que solo puede coger los valores mas cercanos que tenga dentro de la lista:

```python
caracteres = list("█▓▒░ ")
numeros = list("01234")
crea_degradado(caracteres)
crea_degradado(numeros)

╔═════════════════════▬□x╗
║  ░░░▒▓▓▓██████▓█▓▓▓▒▓▒ ║
║  ░░░▒▓▓▓██████▓█▓▓▓▒▓▒ ║
║  ░░░▒▓▓▓██████▓█▓▓▓▒▓▒ ║
║  ░░░▒▓▓▓██████▓█▓▓▓▒▓▒ ║
║  ░░░▒▓▓▓██████▓█▓▓▓▒▓▒ ║
║  ░░░▒▓▓▓██████▓█▓▓▓▒▓▒ ║
║  ░░░▒▓▓▓██████▓█▓▓▓▒▓▒ ║
║  ░░░▒▓▓▓██████▓█▓▓▓▒▓▒ ║
║  ░░░▒▓▓▓██████▓█▓▓▓▒▓▒ ║
║  ░░░▒▓▓▓██████▓█▓▓▓▒▓▒ ║
╚════════════════════════╝
╔═════════════════════▬□x╗
║ 2344434444343432321012 ║
║ 2344434444343432321012 ║
║ 2344434444343432321012 ║
║ 2344434444343432321012 ║
║ 2344434444343432321012 ║
║ 2344434444343432321012 ║
║ 2344434444343432321012 ║
║ 2344434444343432321012 ║
║ 2344434444343432321012 ║
║ 2344434444343432321012 ║
╚════════════════════════╝
```