import pygame, random
pygame.init()

WIDTH, HEIGHT = 1000, 700
size = (WIDTH, HEIGHT) 
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Soil Saga")

clock = pygame.time.Clock()

carryOn = True




while carryOn:
    
    # 1. get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    # 2. draw stuff
    


pygame.quit()