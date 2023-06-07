import pygame, random

pygame.init()

# setting up the display
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
PURPLE = (255, 0, 255)
GREEN = (0, 255, 0)

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


class Bullet:
    def __init__(self, plant, speed, damage):
        self.plant = plant
        self.speed = speed
        self.damage = damage
        self.x = plant.x

    def move(self):
        # update position
        self.x += self.speed

        # if it goes off the screen delete it
        if self.x >= WIDTH:
            plant.bulletArr.remove(self)
            del self
        else:
            # if collides with enemy deal damage
            if self.x >= bruh.x:
                bruh.health -= self.damage
                plant.bulletArr.remove(self)
                del self

    def draw(self):
        pygame.draw.rect(screen, PURPLE, [self.x, plant.y + 12.5, 25, 25])


class Plant:
    def __init__(self, health):
        self.x = tile[1] * 100 + 25
        self.y = tile[0] * 100 + 25
        self.width = 50
        self.height = 50
        self.health = health

    def draw(self):
        pygame.draw.rect(screen, ORANGE, [self.x, self.y, self.width, self.height])


class CornPlant(Plant):
    def __init__(self):
        super().__init__(50)
        self.damage = 10
        self.fireRate = 60  # lower means faster shooting
        self.shootTimer = 0
        self.bulletArr = []

    # TODO: make it so that it only attacks if there is an enemy in its lane
    def attack(self):
        # if the timer is less than what it should be dont fire, otherwise do
        if self.shootTimer < self.fireRate:
            pass
        elif self.shootTimer >= self.fireRate:
            # add a new bullet to the bullet array
            self.bulletArr.append(Bullet(self, 5, self.damage))
            self.shootTimer = 0

        self.shootTimer += 1


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

    def place(self):
        print("planted: " + self.plantName)

        if currentCard.plantName == "corn":
            plants.append(CornPlant())

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


class Enemy:
    def __init__(self, row, speed, damage, health, dead):
        self.row = row
        self.x = WIDTH
        self.y = self.row * 100 + 25
        self.speed = speed
        self.damage = damage
        self.health = health
        self.dead = dead

    def move(self):
        self.x -= self.speed

    def checkDeath(self):
        print(self.health)
        if self.health <= 0:
            self.dead = True

    def draw(self):
        pygame.draw.rect(screen, GREEN, [self.x, self.y, 50, 50])


class ZombieBasic(Enemy):
    def __init__(self):
        super().__init__(3, 1, 20, 50, False)


# create all of the different types of cards
cornCard = Card(0, 100, True, "corn")
susCard = Card(1.1, 200, True, "sus")

cards = [cornCard, susCard]
plants = []

bruh = ZombieBasic()

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
                        and pygame.mouse.get_pos()[0]
                        <= tiles.tileWidth * tile[1] + tiles.tileWidth
                        and pygame.mouse.get_pos()[1] >= tiles.tileWidth * tile[0]
                        and pygame.mouse.get_pos()[1]
                        <= tiles.tileWidth * tile[0] + tiles.tileHeight
                        and tile[2]
                    ):
                        currentCard.place()
                        tile[2] = False  # cant plant there anymore

                currentCard = 0

    # update positions of cards
    if currentCard:
        if currentCard.picked:
            currentCard.posx = pygame.mouse.get_pos()[0] - 0.5 * currentCard.width
            currentCard.posy = pygame.mouse.get_pos()[1] - 0.5 * currentCard.height

    # plants attack
    for plant in plants:
        plant.attack()

        # bullet move
        if plant.bulletArr:
            for bullet in plant.bulletArr:
                bullet.move()


    # check if enemy dead
    bruh.checkDeath()
    if bruh.dead:
        del bruh
    else:
        # enemies move
        bruh.move()

    # clear screen
    pygame.draw.rect(screen, (0, 0, 0), [0, 0, WIDTH, HEIGHT])

    # draw tiles

    # tiles.draw()
    bruh.draw()
    pygame.draw.rect(screen, WHITE, [0, HEIGHT - 150, WIDTH, 150])

    # draw the cards
    for card in cards:
        card.draw()

    # draw the plants and their bullets (if they have any)
    for plant in plants:
        if plant.bulletArr:
            for bullet in plant.bulletArr:
                bullet.draw()

        plant.draw()

    # update screen
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
