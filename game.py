import pygame, random

pygame.init()

WIDTH, HEIGHT = 1000, 700
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Soil Saga")

clock = pygame.time.Clock()

carryOn = True

# Colors
COLOR1 = (125, 125, 125)
COLOR2 = (100, 100, 100)
ORANGE= ()


class Tiles:
    def __init__(self, tileWidth, tileHeight, rows, columns):
        self.tileWidth = tileWidth
        self.tileHeight = tileHeight
        self.rows = rows
        self.columns = columns

    def draw(self):
        color = 0
        for i in range(self.rows):
            if i % 2 == 0:
                color = COLOR1
            else:
                color = COLOR2

            for j in range(self.columns):
                if color == COLOR1:
                    color = COLOR2
                else:
                    color = COLOR1

                pygame.draw.rect(
                    screen, color, [self.tileWidth * j, self.tileHeight * i, self.tileWidth, self.tileHeight]
                )

class Plant:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pass



class Card:
    def __init__(self):
        pass


tiles = Tiles(100, 100, 5, 9)

while carryOn:
    # 1. get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    # 2. draw stuff
    tiles.draw()

    # 3. update screen
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
