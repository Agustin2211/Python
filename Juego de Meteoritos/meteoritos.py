import pygame, sys
from pygame import image
from pygame.locals import *
from clases import jugador
from clases import asteroide
from random import randint
from time import time

#VARIABLES
ANCHO = 480
ALTO = 700
PLAYING = True
listaAsteroide = []
puntuacion = 0

#FUNCION PRINCIPAL
def cargarAsteroides(x, y):
    meteoro = asteroide.Asteroide(x, y)
    listaAsteroide.append(meteoro)

def gameOver():
    global PLAYING
    PLAYING = False
    for meteoritos in listaAsteroide:
        listaAsteroide.remove(meteoritos)

def meteoritos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    fondo = pygame.image.load("C:/Users/Agustín/GitHub/Python/Juego de Meteoritos/resources/image/fondo.png")
    pygame.display.set_caption("Meteoritos")
    nave = jugador.Nave()
    contador = 0

    #SONIDOS
    pygame.mixer.music.load("C:/Users/Agustín/GitHub/Python/Juego de Meteoritos/resources/sounds/fondo.wav")
    pygame.mixer.music.play(3)
    sonidoColision = pygame.mixer.Sound("C:/Users/Agustín/GitHub/Python/Juego de Meteoritos/resources/sounds/colision.aiff")

    #FUENTE DEL MARCADOR
    fuenteMarcador = pygame.font.SysFont("Arial", 20)
    colorFuente = (255,255,255)

    #CICLO DEL JUEGO
    while True:

        ventana.blit(fondo, (0,0))
        nave.dibujar(ventana)
        tiempo = time()
        global puntuacion
        textoMarcador = fuenteMarcador.render("Puntuacion: " + str(puntuacion), 0, colorFuente)
        ventana.blit(textoMarcador, (0, 0))
        if (tiempo - contador > 1):
            contador = tiempo
            posX = randint(2,478)
            cargarAsteroides(posX, 0)

        if len(listaAsteroide) > 0:
            for i in listaAsteroide:
                if PLAYING == True:
                    i.dibujar(ventana)
                    i.recorrido()
                    if(i.rect.top > ALTO):
                        listaAsteroide.remove(i)
                    else:
                        if(i.rect.colliderect(nave.rect)):
                            listaAsteroide.remove(i)
                            sonidoColision.play()
                            nave.vida = False
                            gameOver()

        if len(nave.listaDisparo) > 0:
            for i in nave.listaDisparo:
                i.dibujar(ventana)
                i.recorrido()
                if i.rect.top < -10:
                    nave.listaDisparo.remove(i)
                else:
                    for meteoritos in listaAsteroide:
                        if(i.rect.colliderect(meteoritos)):
                            listaAsteroide.remove(meteoritos)
                            puntuacion = puntuacion + 1
                            nave.listaDisparo.remove(i)

        nave.mover()

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if PLAYING == True:
                    if evento.key == K_LEFT:
                        nave.rect.left = nave.rect.left - nave.velocidad
                    elif evento.key == K_RIGHT:
                        nave.rect.right = nave.rect.right + nave.velocidad
                    elif evento.key == K_SPACE:
                        x,y = nave.rect.center
                        nave.disparar(x,y)

        if PLAYING == False:
            fuenteGameOver = pygame.font.SysFont("Arial", 40)
            textoGameOver = fuenteGameOver.render("Game Over", 0, colorFuente)
            ventana.blit(textoGameOver, (140, 140))
            pygame.mixer.music.fadeout(3000)

        pygame.display.update()

meteoritos()