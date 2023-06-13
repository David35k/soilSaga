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
    def __init__(self, plant, speed, damage, row):
        self.plant = plant
        self.speed = speed
        self.damage = damage
        self.x = plant.x
        self.destroy = False
        self.row = row

    def move(self):
        # update position
        self.x += self.speed

        # if it goes off the screen delete it
        if self.x >= WIDTH:
            plant.bulletArr.remove(self)
            self.destroy = True

        # if collides with enemy deal damage
        for enemy in enemyArr:
            if self.x >= enemy.x and self.x <= enemy.x + 50 and self.row == enemy.row:
                enemy.health -= self.damage
                self.destroy = True

    def draw(self):
        pygame.draw.rect(screen, PURPLE, [self.x, plant.y + 12.5, 25, 25])


class Plant:
    def __init__(self, health, type):
        self.x = tile[1] * 100 + 25
        self.y = tile[0] * 100 + 25
        self.width = 50
        self.height = 50
        self.health = health
        self.type = type

    def draw(self):
        pygame.draw.rect(screen, ORANGE, [self.x, self.y, self.width, self.height])


class MoneyTreePlant(Plant):
    def __init__(self):
        super().__init__(30, "passive")
        self.rate = 500
        self.timer = 0

    def passive(self):
        if self.timer < self.rate:
            pass
        elif self.timer >= self.rate:
            global MONEY
            MONEY = MONEY + 25
            self.timer = 0

        self.timer += 1


class CornPlant(Plant):
    def __init__(self):
        super().__init__(50, "shoot")
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
            self.bulletArr.append(Bullet(self, 5, self.damage, (self.y - 25) / 100))
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
        print(
            "planted: "
            + self.plantName
            + ", row: "
            + str(tile[0])
            + ", column: "
            + str(tile[1])
        )

        if currentCard.plantName == "moneyTree":
            plants.append(MoneyTreePlant())
        elif currentCard.plantName == "corn":
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
        if self.health <= 0:
            self.dead = True

    def draw(self):
        pygame.draw.rect(screen, GREEN, [self.x, self.y, 50, 50])


class ZombieBasic(Enemy):
    def __init__(self, row):
        super().__init__(row, 1, 20, 50, False)


class Wave:
    def __init__(self, enemies, length):
        # each array inside has [type of enemy, time to spawn (frames since start of wave)]
        self.enemies = enemies
        self.length = length  # length of wave in frames

    def spawnEnemies(self):
        for enemy in self.enemies:
            # check if it is time to spawn
            if enemy[1] <= 0:
                if enemy[0] == "zombieBasic":
                    enemyArr.append(ZombieBasic(random.randint(0, 4)))
                    self.enemies.remove(enemy)
            else:
                enemy[1] -= 1


currentCard = 0

# MONEY!!!
MONEY = 1000

# Fonts
moneyFont = pygame.font.SysFont(None, 50)

# create all of the different types of cards
moneyCard = Card(0, 50, True, "moneyTree")
cornCard = Card(1.1, 100, True, "corn")


cards = [moneyCard, cornCard]
plants = []

testWave = Wave([["zombieBasic", 120], ["zombieBasic", 500], ["zombieBasic", 300]], 600)
susWave = Wave(
    [
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
        ["zombieBasic", random.randint(0, 500)],
    ],
    500,
)

enemyArr = []

# for i in range(1):
#     enemyArr.append(ZombieBasic(random.randint(0, 4)))

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
                        and MONEY >= currentCard.cost
                    ):
                        currentCard.place()
                        MONEY -= currentCard.cost
                        tile[2] = False  # cant plant there anymore

                currentCard = 0

    # update positions of cards
    if currentCard:
        if currentCard.picked:
            currentCard.posx = pygame.mouse.get_pos()[0] - 0.5 * currentCard.width
            currentCard.posy = pygame.mouse.get_pos()[1] - 0.5 * currentCard.height

    # create enemies
    testWave.spawnEnemies()
    testWave.length -= 1
    if testWave.length <= 0:
        susWave.spawnEnemies()

    # plants attack
    for plant in plants:
        if plant.type == "passive":
            plant.passive()
        elif plant.type == "shoot":
            plant.attack()

        # bullet move
        if plant.type == "shoot":
            for bullet in plant.bulletArr:
                bullet.move()
                if bullet.destroy and bullet in plant.bulletArr:
                    plant.bulletArr.remove(bullet)
                    del bullet

    # check if enemy dead
    for enemy in enemyArr:
        enemy.checkDeath()
        if enemy.dead and enemy in enemyArr:
            enemyArr.remove(enemy)
            del enemy
        else:
            # enemies move
            enemy.move()

    # update text
    moneyTextRect = moneyFont.render(str(MONEY), True, (0, 0, 0))

    # clear screen
    pygame.draw.rect(screen, (0, 0, 0), [0, 0, WIDTH, HEIGHT])

    # draw tiles
    # tiles.draw()

    # draw the card bar
    pygame.draw.rect(screen, WHITE, [0, HEIGHT - 150, WIDTH, 150])

    # draw the cards
    for card in cards:
        card.draw()

    # draw the plants and their bullets (if they have any)
    for plant in plants:
        if plant.type == "shoot":
            for bullet in plant.bulletArr:
                if not bullet.destroy:
                    bullet.draw()

        plant.draw()

    # draw the enemies
    for enemy in enemyArr:
        enemy.draw()

    screen.blit(
        moneyTextRect,
        (
            WIDTH - moneyTextRect.get_width() - 10,
            HEIGHT - moneyTextRect.get_height() - 10,
        ),
    )

    # update screen
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
