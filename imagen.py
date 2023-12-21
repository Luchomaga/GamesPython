import pygame, sys
from pygame.locals import *

pygame.init()
ventana =  pygame.display.set_mode((700, 500))
pygame.display.set_caption("jUEGUITO")
#Colorcitos
colorfondo=(1,150,70)
#Carga imagen
imagen = pygame.image.load("imagenes/erizo.jpg")
#posicion de la imagen
posX, posY = (10,40)
while True:
    ventana.fill(colorfondo)
    ventana.blit(imagen, (posX, posY))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
