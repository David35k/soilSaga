import pygame, game, random, enemiesClasses, plantsClasses

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
                game.screen,
                tile[3],
                [
                    self.tileWidth * tile[1],
                    self.tileHeight * tile[0],
                    self.tileWidth,
                    self.tileHeight,
                ],
            )


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
        if self.x >= game.WIDTH:
            game.plant.bulletArr.remove(self)
            self.destroy = True

        # if collides with enemy deal damage
        for enemy in game.enemyArr:
            if self.x >= enemy.x and self.x <= enemy.x + 50 and self.row == enemy.row:
                enemy.health -= self.damage
                self.destroy = True

    def draw(self):
        pygame.draw.rect(game.screen, PURPLE, [self.x, game.plant.y + 12.5, 25, 25])


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
                    game.enemyArr.append(enemiesClasses.ZombieBasic(random.randint(0, 4)))
                    self.enemies.remove(enemy)
            else:
                enemy[1] -= 1


class Card:
    def __init__(self, order, cost, canPick, plantName):
        self.width = 100
        self.height = 100
        self.order = order
        self.cost = cost
        self.canPick = canPick
        self.posx = self.width * self.order + 10
        self.posy = game.HEIGHT - self.height - 25
        self.picked = False
        self.plantName = plantName

    def place(self):
        print(
            "planted: "
            + self.plantName
            + ", row: "
            + str(game.tile[0])
            + ", column: "
            + str(game.tile[1])
        )

        if game.currentCard.plantName == "moneyTree":
            game.plants.append(plantsClasses.MoneyTreePlant())
        elif game.currentCard.plantName == "corn":
            game.plants.append(plantsClasses.CornPlant())

    def draw(self):
        color = ORANGE

        if (
            pygame.mouse.get_pos()[0] >= self.posx
            and pygame.mouse.get_pos()[0] <= self.posx + self.width
            and pygame.mouse.get_pos()[1] >= self.posy
            and pygame.mouse.get_pos()[1] <= self.posy + self.height
        ):
            color = BLUE

        pygame.draw.rect(
            game.screen, color, [self.posx, self.posy, self.width, self.height]
        )