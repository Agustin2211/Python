import pygame,sys
from pygame.locals import *

pygame.init()

#CREO LA PRIMERA VENTANA DEL JUEGO
ventana = pygame.display.set_mode((800, 600))

#LE COLOCO UN NOMBRE A LA VENTANA
pygame.display.set_caption("Menu Principal")

#COLORES
colorFondo = (1,150,70)
colorLinea = (0,0,255)
colorCirculo = (0,255,255)
colorFiguras = (255,69,0)

#BUCLE PRINCIPAL
while True:
    ventana.fill(colorFondo)

    #DIBUJAR UNA LINEA (EN DONDE, QUE COLOR, PRIMERA POSICION, SEGUNDA POSICION, GROSOR)
    pygame.draw.line(ventana, colorLinea, (10,30), (150,100), 70)
    pygame.draw.line(ventana, colorFondo, (20,30), (150,100), 70)
    pygame.draw.line(ventana, colorCirculo, (30,30), (150,100), 70)
    pygame.draw.line(ventana, colorFiguras, (40,30), (150,100), 70)

    #DIBUJAR UN CIRCULO(EN DONDE, QUE COLOR, POSICION, RADIO, ANCHO)
    pygame.draw.circle(ventana, colorCirculo, (400,450), 77, 40)

    #DIBUJAR RECTANGULO (EN DONDE, QUE COLOR, (DONDE, HASTA))
    pygame.draw.rect(ventana, colorFiguras, (500, 500, 250, 250))

    #DIBUJAR UN POLIGONO (EN DONDE, QUE COLOR, PRIMERA POSICION, SEGUNDA POSICION, HASTA PRIMERA POSICION, HASTA SEGUNDA POSICION)
    pygame.draw.polygon(ventana, colorCirculo, ((400, 400), (500, 500), (600, 600), (700, 700)))

    for evento in pygame.event.get():

        #EL USUARIO QUIERE SALIR DEL JUEGO
        if(evento.type == QUIT):
            pygame.quit()
            sys.exit()
        
        #SE ACTUALIZA LA VENTANA
        pygame.display.update()