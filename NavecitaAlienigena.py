import turtle
import pygame
import random
import math
import sys
import os

#Iniciar juego
pygame.init()

#establece el tamaño de la pantalla
screen_widht = 800
screen_height = 600
screen = pygame.display.set_mode((screen_widht, screen_height))

#Opciones para rutas de recursos
def resource_path(relative_path):
    try:
        base_path = sys._MEiPASS
    except:
        base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

#Cargar imagen de fondo
asset_background = resource_path('gamesaliens/background.png')
background = pygame.image.load(asset_background)

#Cargar icono de ventana
asset_icon = resource_path('gamesaliens/ufo.png')
icon = pygame.image.load(asset_icon)

#Cargar sonido del fondo
asset_sound = resource_path('gamesaliens/audios/background_music.mp3')
background_sound = pygame.mixer.music.load(asset_sound)

#Cargar imegen de jugador
asset_playering = resource_path('gamesaliens/space-invaders.png')
playering = pygame.image.load(asset_playering)

#Cargar imagen de bala 
asset_bulleting = resource_path('gamesaliens/bullet.png')
bulleting = pygame.image.load(asset_bulleting)

#Cargar fuente para texto
asset_over_font =resource_path('gamesaliens/fonts/Ravie.ttf')
over_font = pygame.font.Font(asset_over_font, 60)

#Fuente para texto de puntuacion
asset_puntuacion =resource_path('gamesaliens/fonts/comicbd.ttf')
puntuacion = pygame.font.Font(asset_puntuacion)

#Titulo de ventana
pygame.display.set_caption("Space Invader")

#Establecer icono de ventana
pygame.display.set_icon(icon)

#Reproducir sonido de fondo en loop
pygame.mixer.music.play(-1)

#Crear relog para controñar velocidad de juego
clock = pygame.time.Clock()

#Posicion inicial del jugador 
PlayerX = 370
PlayerY = 470
playerX_change = 0
playerY_change = 0

#lista para almacenar pocisiones de los enemigos 
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemys = 10

#Se inicializa las variables para guardar las pocisiones de los enemigos
for i in range(no_of_enemys):
    enemy1 = resource_path('gamesaliens/enemy1.png')
    enemyimg.append(pygame.image.load(enemy1))
    
    enemy2 = resource_path('gamesaliens/enemy2.png')
    enemyimg.append(pygame.image.load(enemy2))
    
    #se asigna posiciones aleatorias para los enemigos 
    enemyX.append(random.randint(0,739))
    enemyY.append(random.randint(0,150))
    #Se establece la velocidad en los ejes
    enemyX_change.append(5)
    enemyY_change.append(20)
    
    #Se inicializa variables para otorgar posiciones a las balas
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 10
    bullet_state = "ready"
    
    # En algún lugar al principio del script
    pygame.font.init()  # Inicializa el módulo de fuentes de Pygame
    font = pygame.font.Font(None, 36)  # Crea una fuente (puedes ajustar el tamaño según sea necesario)

    #se inicializa la puntuacion en 0
    score = 0
    #funcion para mostrar la puntuacion en la pantalla
    def show_score():
        score_value = font.render("SCORE" + str(score), True, (255, 255, 255))
        screen.blit(score_value, (10, 10))
    #funcion para dibujar al jugador 
    def player(x, y):
        screen.blit(playering, (x,y))
    #funcion para dibujar al enemigo en la pantalla
    def enemy(x,y,i):
        screen.blit(enemyimg[i], (x,y))
    #funcion  para disparar bala
    def fire_bullet(x, y):
        global bullet_state
        
        bullet_state = "fire"
        screen.blit(bulleting, (x + 16, y + 10))
    #funcion para comprar si ha habido una colision entre la bala y el enemigo
    def isCollision(enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
        if distance < 27:
            return True
        else:
            return False
    #funcion para mostrar un texto de game over
    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (255,255,255))
        text_rect = over_text.get_rect(center=(int(screen_widht/2), int(screen_widht/2)))
        screen.blit(over_text, text_rect)
    
    #Bucle principal
    def gameloop():
        #declaramos
        global score
        global PlayerX
        global PlayerY
        global playerX_change
        global bulletX
        global bulletY
        global Collision
        global bullet_state
        
        in_game = True
        while in_game:
            #maneja, renderiza, actualiza y limpia pantalla
            screen.fill((0, 0, 0))
            screen.blit(background,(0,0))
            
            for event in pygame.event.get():          
                if event.type == pygame.QUIT:
                    in_game = False
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    #movimientos del jugador y disparos
                    if event.key == pygame.K_LEFT:
                        playerX_change = -5
                    if event.key == pygame.K_RIGHT:
                        playerX_change = 5
                    if event.key == pygame.K_SPACE:
                        if bullet_state == "ready":
                            bulletX = PlayerX
                            fire_bullet(bulletX,bulletY)     
                    if event.type == pygame.KEYUP:
                        playerX_change = 0

            #Aqui esta actualizando la posicion de jugador 
            PlayerX += playerX_change
                    
            if PlayerX <= 0:
                PlayerX = 0
            elif PlayerX >= 736:
              PlayerX = 736        
            
            #Bucle que se ejecuta para cada enemigo
            for i in range(no_of_enemys):
                if enemyY[i] > 440:
                    for j in range(no_of_enemys):
                        enemyY[j] = 2000
                    game_over_text()
                    
                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = 5
                    enemyY[i] += enemyY_change[i]
                elif enemyX[i] >= 736:
                    enemyX_change[i] = -5
                    enemyY[i] += enemyY_change[i]
                #Colicion de bala y enemigo
                collison = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
                if collison:
                    bulletY = 454
                    bullet_state = "ready"
                    score += 1
                    enemyX[i]= random.randint(0, 736)
                    enemyY[i] = random.randint(0, 150)
                enemy(enemyX[i],enemyY[i],i) 
            if bulletY < 0:
                bulletY = 454
                bullet_state = "ready"
            if bullet_state =="fire":
                fire_bullet(bulletX,bulletY)
                bulletY -= bulletY_change
            
            player(PlayerX, PlayerY)
            show_score()
            
            pygame.display.update()
            
            clock.tick(120)

gameloop()