import pygame, sys
from pygame.locals import *

pygame.init()
ventana =  pygame.display.set_mode((700, 500))
pygame.display.set_caption("jUEGUITO")
#Colorcitos
colorfondo=(1,150,70)
colorlineas = (255,128,0)
colorcirculo = (255,255,0)
colorfiguras = (205,0,155)
while True:
    ventana.fill(colorfondo)
    pygame.draw.line(ventana,colorlineas,(60, 90), (200,100), 40)
    pygame.draw.line(ventana,colorlineas,(80, 190), (100, 150), 20)
    pygame.draw.line(ventana,colorlineas,(40, 30), (250, 190), 10)
    #circulos
    pygame.draw.circle(ventana, colorcirculo, (400, 100), 100, 30)
    pygame.draw.circle(ventana, colorcirculo, (590, 250), 50, 20)
    #figuras
    pygame.draw.rect(ventana, colorfiguras, (100, 200, 120, 250))
    pygame.draw.polygon(ventana, colorfiguras, ((400, 400),(500, 400), (550, 500), (490, 500)))
    
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()