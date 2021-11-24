import pygame
from clases import disparo

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenNave = pygame.image.load("C:/Users/Agustín/GitHub/Python/Juego de Meteoritos/resources/image/nave.png")
        self.rect = self.imagenNave.get_rect()
        self.imagenNaveDestruida = pygame.image.load("C:/Users/Agustín/GitHub/Python/Juego de Meteoritos/resources/image/naveExplota.png")
        self.rect.centerx = 240
        self.rect.centery = 690
        self.velocidad = 25
        self.vida = True
        self.listaDisparo = []
        self.sonidoDisparo = pygame.mixer.Sound("C:/Users/Agustín/GitHub/Python/Juego de Meteoritos/resources/sounds/disparos.aiff")

    def mover(self):
        if (self.vida == True):
            if (self.rect.left <= 0):
                self.rect.left = 0
            elif (self.rect.right > 490):
                self.rect.right = 490
    
    def disparar(self, x, y):
        if (self.vida == True):
            misil = disparo.Misil(x, y)
            self.listaDisparo.append(misil)
            self.sonidoDisparo.play()

    def dibujar(self, superficie):
        if self.vida == True:
            superficie.blit(self.imagenNave, self.rect)
        else:
            superficie.blit(self.imagenNaveDestruida, self.rect)