import pygame, sys
from pygame import image
from pygame.locals import *
from clases import jugador

#VARIABLES
ANCHO = 480
ALTO = 700
PLAYING = True

#FUNCION PRINCIPAL
def meteoritos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    fondo = pygame.image.load("C:/Users/Agustín/GitHub/Python/Juego de Meteoritos/resources/image/fondo.png")
    pygame.display.set_caption("Meteoritos")
    nave = jugador.Nave()

    #CICLO DEL JUEGO
    while True:

        ventana.blit(fondo, (0,0))
        nave.dibujar(ventana)
        nave.mover()

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == K_LEFT:
                    nave.rect.left = nave.rect.left - nave.velocidad
                elif evento.key == K_RIGHT:
                    nave.rect.right = nave.rect.right + nave.velocidad
                elif evento.key == K_SPACE:
                    nave.disparar()

        pygame.display.update()


meteoritos()