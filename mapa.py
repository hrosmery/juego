import os
from panelControl import cargarPanel

#Variables para crear un juego
WITH_MAPA = 25
HEIHT_MAPA = 20

espacio_vacio = "   "   
espacio_lleno = "[ ]"

# Configuracion de personaje
coordenada_personaje = [8,10]
personaje = "🡹"
movimientos = 0

# Objetos
Lista_objetos = [ [5,8],[10,7],[8,5],[7,4] ]
ico_objeto = "❤"

def cargar_mapa(movimiento_personaje):
    global movimientos, personaje, coordenada_personaje, Lista_objetos

    # Limpiar pantalla
    os.system('cls')

    # Movimiento del personaje
    if movimiento_personaje == 'w':
        personaje = " ▲ " 
        coordenada_personaje[0] -= 1
    elif movimiento_personaje == 's':
        personaje = " ▼ "
        coordenada_personaje[0] += 1
    elif movimiento_personaje == 'a':
        personaje = " ◀ "
        coordenada_personaje[1] -= 1
    elif movimiento_personaje == 'd':
        personaje = " ▶ "
        coordenada_personaje[1] += 1

    # Contador de movimientos
    movimientos += 1

    cargarPanel(coordenada_personaje, personaje, movimientos)

    # Cargar mapa
    print("+"  + "-"*75 + "+")
    for fila in range(HEIHT_MAPA):
        print("|", end="")
        for columna in range(WITH_MAPA):

            estado = 0

            # Dibujar al personaje
            if(coordenada_personaje[0] == fila and coordenada_personaje[1] == columna):
                #si piso el objeto se elimina
                if [fila, columna] in Lista_objetos:
                    Lista_objetos.remove([fila, columna])
                print(f"{personaje}", end="")
                continue #salto a la siguiente casilla

            #dinuja un objeto si existe en la casilla
            if [fila, columna] in Lista_objetos:
                print(f" {ico_objeto} ", end="")
            else:
                print(espacio_vacio, end="")

        print("|")
    print("+"  + "-"*75 + "+")