# modulos
import os
import readchar 
from mapa import cargar_mapa

estado_juego =  True

cargar_mapa("inicio")
    
def juego1():
    global estado_juego
    tecla = readchar.readchar()

    if tecla == 'w':
        cargar_mapa(tecla)
    if tecla == 'a':
        cargar_mapa(tecla)
    elif tecla == 's':
        cargar_mapa(tecla)
    elif tecla == 'd':
        cargar_mapa(tecla)
    elif tecla == "q":
        estado_juego = False
        print("Fin")

while estado_juego==True:
    juego1()