import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
windowWidth=640
windowHeight=480
surface=pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption('Pygame shapes!')
greenx=10
greeny=0

while True:
    #surface.fill((0,0,0))
    #pygame.draw.rect(surface,(255,0,00),(random.randint(0,windowWidth),random.randint(0,windowHeight),10,10))
    pygame.draw.rect(surface,(0,0,255),(greenx,greeny,10,10))
    greenx-=0.4
    greeny+=1
    for event in GAME_EVENTS.get():
        if event.type==GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
