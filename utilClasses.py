import pygame, game, random, enemiesClasses, plantsClasses, spritesheet

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
        for i in range(self.rows):
            for j in range(self.columns):
                self.tileArr.append(
                    [i, j, True, game.BLACK, 0]
                )  # y, x, canPlant, color

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

            game.screen.blit(
                tile[4],
                (self.tileWidth * tile[1], self.tileHeight * tile[0]),
            )


class TipWindow:
    def __init__(self, x, y, width, height, lines, startTime, stopTime):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.lines = lines
        self.startTime = startTime
        self.stopTime = stopTime
        self.drawTimer = 0
        self.showing = False

    def draw(self):
        self.drawTimer += 1
        if self.drawTimer > self.startTime and self.drawTimer < self.stopTime:
            self.showing = True
            pygame.draw.rect(
                game.screen, game.WHITE, [self.x, self.y, self.width, self.height]
            )
            for i in range(len(self.lines)):
                tipSurf, tipRect = game.tipFont.render(self.lines[i], game.BLACK)
                game.screen.blit(
                    tipSurf,
                    (
                        self.x + self.width / 2 - tipRect.width / 2,
                        self.y
                        + self.height / 2
                        - tipRect.height * len(self.lines) / 2
                        + tipRect.height * i,
                    ),
                )


class Bullet:
    def __init__(self, plant, speed, damage, row, offsetX, offsetY, sprite):
        self.plant = plant
        self.speed = speed
        self.damage = damage
        self.offsetX = offsetX
        self.offsetY = offsetY
        self.x = plant.x + offsetX
        self.y = plant.y + offsetY
        self.destroy = False
        self.row = row
        self.sprite = sprite

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

                # if cactus bullet slow down
                if self.plant.name == "cactus":
                    enemy.speed /= 1.5

                self.destroy = True

    def draw(self):
        pygame.draw.rect(
            game.screen, PURPLE, [self.x, game.plant.y + self.offsetY, 25, 25]
        )


class Wave:
    def __init__(self, enemies, length):
        # each array inside has [type of enemy, time to spawn (frames since start of wave)]
        self.enemies = enemies
        self.length = length  # length of wave in frames
        self.timer = 0

    def spawnEnemies(self):
        self.timer += 1
        for enemy in self.enemies:
            # check if it is time to spawn
            if enemy[1] == self.timer:
                if enemy[0] == "robotBasicSlow":
                    game.enemyArr.append(
                        enemiesClasses.RobotBasicSlow(random.randint(0, 4))
                    )
                elif enemy[0] == "robotBasic":
                    game.enemyArr.append(
                        enemiesClasses.RobotBasic(random.randint(0, 4))
                    )
                elif enemy[0] == "assaultBot":
                    game.enemyArr.append(
                        enemiesClasses.AssaultRobot(random.randint(0, 4))
                    )
                elif enemy[0] == "tractorBot":
                    game.enemyArr.append(
                        enemiesClasses.TractorBot(random.randint(0, 4))
                    )
                elif enemy[0] == "teleportBot":
                    game.enemyArr.append(
                        enemiesClasses.TeleportBot(random.randint(0, 4))
                    )
                elif enemy[0] == "laneBot":
                    game.enemyArr.append(enemiesClasses.LaneBot(random.randint(0, 4)))


class Card:
    def __init__(self, order, cost, canPick, plantName, image):
        self.width = 100
        self.height = 100
        self.order = order
        self.cost = cost
        self.canPick = canPick
        self.posx = self.width * self.order + 10
        self.posy = game.HEIGHT - self.height - 50
        self.picked = False
        self.plantName = plantName
        self.image = image

    def place(self):
        if game.currentCard.plantName == "moneyTree":
            game.plants.append(plantsClasses.MoneyTreePlant())
        elif game.currentCard.plantName == "corn":
            game.plants.append(plantsClasses.CornPlant())
        elif game.currentCard.plantName == "carrot":
            game.plants.append(plantsClasses.CarrotPlant())
        elif game.currentCard.plantName == "cactus":
            game.plants.append(plantsClasses.CactusPlant())
        elif game.currentCard.plantName == "bamboo":
            game.plants.append(plantsClasses.BambooPlant())

    def draw(self):
        game.screen.blit(self.image, (self.posx, self.posy))
