import random
from ventana_ascii_funciones import create_window

caracteres = list("█▓▒░")
numeros = list("01234")
chess = list("♞♝♜♛♚♙♘♗♖♕♔♥🙾🙿")
dots = list("⋯⋰⋱∴∷")
set0 = list("∰≭∱∳∻∾≾⊛")

def crea_linea(lista, largo_linea):
    resultado = ""
    start = random.randint(0,len(lista)-1)
    resultado += lista[start]
    
    for caracteres in range(0, largo_linea+1):
        ultimo = resultado[len(resultado)-1]
        val = elige_numero(ultimo, lista)
        resultado += lista[val]
    return resultado

def elige_numero(val, lista):
    if val == lista[0]:
        return random.randint(0,1)

    if val != lista[0] and val != lista[len(lista)-1]:
        indice = lista.index(val)
        resultado = random.randint(indice-1, indice+1)
        return resultado

    if val == lista[len(lista)-1]:
        return random.randint(len(lista)-2,len(lista)-1)
    
def crea_degradado(lista):
    linea = crea_linea(lista, 15)
    contenido = []
    for i in range(0,10):
        contenido.append(linea)
    create_window(contenido)

crea_degradado(numeros)
crea_degradado(caracteres)
crea_degradado(dots)
crea_degradado(set0)
