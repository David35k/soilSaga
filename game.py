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
ORANGE = (255, 165, 0)
ORANGE2 = (240, 165, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

currentCard = 0


class Tiles:
    def __init__(self, tileWidth, tileHeight, rows, columns):
        self.tileWidth = tileWidth
        self.tileHeight = tileHeight
        self.rows = rows
        self.columns = columns
        self.tileArr = []

    def createTiles(self):
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

                self.tileArr.append([i, j, True, color])  # y, x, canPlant, color

    def draw(self):
        for tile in self.tileArr:
            pygame.draw.rect(
                screen,
                tile[3],
                [
                    self.tileWidth * tile[1],
                    self.tileHeight * tile[0],
                    self.tileWidth,
                    self.tileHeight,
                ],
            )

tiles = Tiles(100, 100, 5, 10)
tiles.createTiles()


class Plant:
    def __init__(self):
        self.x = tile[1] * 100 + 25
        self.y = tile[0] * 100 + 25
        self.width = 50
        self.height = 50

    def draw(self):
        pygame.draw.rect(screen, ORANGE, [self.x, self.y, self.width, self.height])

class CornPlant(Plant):
    def __init__(self, damage, fireRate):
        super().__init__()
        self.damage = damage
        self.fireRate = fireRate
        
    def shoot(self):
        pass

class Card:
    def __init__(self, order, cost, canPick, plantName):
        self.width = 100
        self.height = 100
        self.order = order
        self.cost = cost
        self.canPick = canPick
        self.posx = self.width * self.order + 10
        self.posy = HEIGHT - self.height - 25
        self.picked = False
        self.plantName = plantName

    def place(self, tile):
        print(self.plantName)

        if currentCard.plantName == "corn":
            plants.append(CornPlant(50, 45))

    def draw(self):
        color = ORANGE

        if (
            pygame.mouse.get_pos()[0] >= self.posx
            and pygame.mouse.get_pos()[0] <= self.posx + self.width
            and pygame.mouse.get_pos()[1] >= self.posy
            and pygame.mouse.get_pos()[1] <= self.posy + self.height
        ):
            color = BLUE

        pygame.draw.rect(screen, color, [self.posx, self.posy, self.width, self.height])


class CardBar:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(
            screen, WHITE, [0, HEIGHT - self.height, self.width, self.height]
        )


cardBar = CardBar(WIDTH, 150)

cornCard = Card(0, 100, True, "corn")
susCard = Card(1.1, 200, True, "sus")

cards = [cornCard, susCard]
plants = []

while carryOn:
    # get check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # check if clicking a card
            for card in cards:
                if (
                    pygame.mouse.get_pos()[0] >= card.posx
                    and pygame.mouse.get_pos()[0] <= card.posx + card.width
                    and pygame.mouse.get_pos()[1] >= card.posy
                    and pygame.mouse.get_pos()[1] <= card.posy + card.height
                    and card.canPick
                ):
                    currentCard = card
                    card.picked = True

        if event.type == pygame.MOUSEBUTTONUP:
            # put the selected card back
            if currentCard:
                currentCard.picked = False
                currentCard.posx = currentCard.width * currentCard.order + 10
                currentCard.posy = HEIGHT - currentCard.height - 25

                # if hovering over a vacant tile place the plant
                for tile in tiles.tileArr:
                    if (
                        pygame.mouse.get_pos()[0] >= tiles.tileWidth * tile[1]
                        and pygame.mouse.get_pos()[0] <= tiles.tileWidth * tile[1] + tiles.tileWidth
                        and pygame.mouse.get_pos()[1] >= tiles.tileWidth * tile[0]
                        and pygame.mouse.get_pos()[1] <= tiles.tileWidth * tile[0] + tiles.tileHeight
                        and tile[2]
                    ):
                        currentCard.place(tile)

                currentCard = 0

    # update positions
    if currentCard:
        if currentCard.picked:
            currentCard.posx = pygame.mouse.get_pos()[0] - 0.5 * currentCard.width
            currentCard.posy = pygame.mouse.get_pos()[1] - 0.5 * currentCard.height

    # clear screen
    pygame.draw.rect(screen, (0, 0, 0), [0, 0, WIDTH, HEIGHT])

    # draw stuff
    tiles.draw()
    cardBar.draw()

    for card in cards:
        card.draw()

    for plant in plants:
        plant.draw()

    # update screen
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
