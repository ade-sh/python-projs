import pygame
pygame.init()
pygame.display.set_caption("hello game")
window=pygame.display.set_mode((500,400))
bg_color=(0,0,230)
while True:
    window.fill(bg_color)
    pygame.draw.circle(window,(0,255,0),(100,99),22,3)
    pygame.draw.rect(window,(55,80,100),(100,50,70,300))
    pygame.draw.rect(window,(255,0,0),(0,0,50,30))
    
    pygame.display.update()
