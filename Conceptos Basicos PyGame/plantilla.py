import pygame,sys
from pygame.locals import *

pygame.init()

#CREO LA PRIMERA VENTANA DEL JUEGO
ventana = pygame.display.set_mode((800, 600))
#LE COLOCO UN NOMBRE A LA VENTANA
pygame.display.set_caption("Menu Principal")

colorFondo = (1,150,70)

#BUCLE PRINCIPAL

while True:
    ventana.fill(colorFondo)
    for evento in pygame.event.get():

        #EL USUARIO QUIERE SALIR DEL JUEGO

        if(evento.type == QUIT):
            pygame.quit()
            sys.exit()
        
        #SE ACTUALIZA LA VENTANA
        pygame.display.update()