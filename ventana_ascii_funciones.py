import random

borde = list("╔╗╚╝")
hor = "═"
ver = "║"

def create_top(width):
    ancho = width-5
    resultado = borde[0]+hor*ancho+"▬"+"□"+"x"+borde[1]
    print(resultado)

def create_line(width, text):
    resultado = ver +text + ver
    return resultado

def create_lines(width, texts):
    for text in texts:
        n_espacios = (width - (len(text) + 2))//2
        resto_espacios = (width - (len(text) + 2))%2
        
        print(f"{ver}{' '*n_espacios}{text}{' '*n_espacios}{' '*resto_espacios}{ver}")
        #print("{}{}{}{}{}{:>12}".format(ver, " "*n_espacios, text, " "*n_espacios, " "*resto_espacios, ver))


def create_bottom(width):
    width -= 2
    resultado = borde[2] + hor*width + borde[3]
    print(resultado)

def create_window(texts):
    width = 0
    for linea in texts:
        if len(linea) > width:
            width = len(linea)
    width += 4
    create_top(width)
    create_lines(width, texts)
    create_bottom(width)

def crea_lista(n_lineas, largo, start, finish):
    resultado = []
    for lineas in range(0, n_lineas):
        linea = ""
        for caracter in range(0, largo):
            car = random.randint(start, finish)
            car = chr(car)
            linea += car
        resultado.append(linea)
    return resultado


if __name__ == "__main__":
    lista = ["Hola mundo", "Esto es una prueba"]
    create_window(lista)




