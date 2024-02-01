import pygame
import random
import winsound
from Obstacles import obstacles

pygame.init()
pygame.display.set_caption("Trex Game")
screen = pygame.display.set_mode((900, 300))
screen.fill((0,0,0))
clock = pygame.time.Clock()
gameover = False

#player variables
xpos = 100
ypos = 200
vy = 0
PHeight = 100
PWidth = 50
PHealth = 100
isOnGround = True

keys = [False, False]

ticker =  0
score = 0
obst = []
for i in range(5):
    obst.append(obstacles())



while gameover == False:
    clock.tick(60)
    ticker += 1
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True

        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_SPACE:
                keys[0] = True
            elif event.key == pygame.K_UP:
                keys[0] = True
            if event.key == pygame.K_DOWN:
                keys[1] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                keys[0] = False
            elif event.key == pygame.K_UP:
                keys[0] = False
            if event.key == pygame.K_DOWN:
                keys[1] = False
                
    if keys[0] == True and isOnGround == True: #only jump when on the ground
        winsound.Beep(600, 50)
        vy = -8
        isOnGround = False
    
        
    if ypos + 100 > 300:
        isOnGround = True
        vy = 0
        ypos = 300 -100
        
    for i in range(len(obst)):
        obst[i].move()
        if ypos + PHeight >= obst[i].ypos and ypos <= obst[i].ypos + obst[i].height and xpos + PWidth >= obst[i].xpos and xpos <= obst[i].xpos + obst[i].width:
            obst[i].xpos = random.randrange(900, 2500)
            PHealth -= 10
            print(PHealth)
    if isOnGround == False:
        vy+=.4#Gravity
        

    if ticker >40:
        score += 1
        ticker = 0
    ypos += vy
    if PHealth <= 0:
        gameover = True
    #render section
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 255), (xpos, ypos, 50, PHeight), 5)
    #Health bar
    pygame.draw.rect(screen, (255, 0, 0), (700, 25, 100, 25))
    pygame.draw.rect(screen, (0, 255, 0), (700, 25, PHealth, 25))
    

    #score
    font = pygame.font.Font(None, 40)
    text = font.render(str(score),1, (255, 48, 55))
    screen.blit(text, (100,25))
    for i in range(len(obst)):
        obst[i].draw(screen)
    pygame.display.flip()
pygame.quit()