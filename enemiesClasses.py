import pygame, game, random, spritesheet


class Enemy:
    def __init__(self, row, speed, damage, health, dead):
        self.row = row
        self.x = game.WIDTH
        self.y = self.row * 100 + 25
        self.speed = speed
        self.damage = damage
        self.health = health
        self.dead = dead
        self.attackTimer = 0
        self.attackRate = 60
        self.canMove = True

    def move(self):
        if len(game.plants) == 0:
            self.canMove = True

        if self.canMove:
            self.x -= self.speed

        # check if it should attack the plants
        for plant in game.plants:
            if (
                (plant.y - 25) / 100 == self.row
                and self.x - 70 <= plant.x
                and self.x - 70 - self.speed >= plant.x - 10
            ):
                self.attack(plant)
                self.canMove = False
            if plant.health <= 0:
                self.canMove = True

        # if it is off the screen to the left you lose
        if self.x < -25:
            game.gameOver = True
            self.dead = True

    def attack(self, plant):
        if self.attackTimer >= self.attackRate:
            plant.health -= self.damage
            self.attackTimer = 0

        self.attackTimer += 1

    def checkDeath(self):
        if self.health <= 0:
            self.dead = True

    def draw(self):
        pygame.draw.rect(game.screen, game.GREEN, [self.x, self.y, 50, 50])


class RobotBasicSlow(Enemy):
    def __init__(self, row):
        super().__init__(row, 0.6, 10, 50, False)
        self.name = "basic"
        self.sprite = spritesheet.Sprite(game.robotAnims, 0, 4, random.randint(0, 3))


class RobotBasic(Enemy):
    def __init__(self, row):
        super().__init__(row, 1, 15, 50, False)
        self.name = "basic"
        self.sprite = spritesheet.Sprite(game.robotAnims, 0, 4, random.randint(0, 3))


class AssaultRobot(Enemy):
    def __init__(self, row):
        super().__init__(row, 1.6, 45, 30, False)
        self.name = "assault"
        self.sprite = spritesheet.Sprite(game.robotAnims, 1, 4, 0)


class TractorBot(Enemy):
    def __init__(self, row):
        super().__init__(row, 0.6, 500, 100, False)
        self.name = "tractor"
        self.sprite = spritesheet.Sprite(game.robotAnims, 2, 4, random.randint(0, 3))


class TeleportBot(Enemy):
    def __init__(self, row):
        super().__init__(row, 0.8, 30, 45, False)
        self.name = "teleport"
        self.tpTimer = 0
        self.sprite = spritesheet.Sprite(game.robotAnims, 3, 4, random.randint(0, 3))

    def teleport(self):
        if self.tpTimer >= 60 * 2:
            self.x -= 100
            self.canMove = True
            self.tpTimer = 0

        self.tpTimer += 1


class LaneBot(Enemy):
    def __init__(self, row):
        super().__init__(row, 0.8, 30, 75, False)
        self.name = "laneSwitch"
        self.switchTimer = 0
        self.sprite = spritesheet.Sprite(game.robotAnims, 4, 4, random.randint(0, 3))

    def switch(self):
        if self.switchTimer >= 60 * 3:
            self.row = random.randint(0, 4)
            self.y = self.row * 100 + 25
            self.canMove = True
            self.switchTimer = 0

        self.switchTimer += 1
