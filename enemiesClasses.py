import pygame, game


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


class RobotBasic(Enemy):
    def __init__(self, row):
        super().__init__(row, 1, 30, 50, False)

class AssaultRobot(Enemy):
    def __init__(self, row):
        super().__init__(row, 1.5, 40, 30, False)