import pygame, game, utilClasses


class Plant:
    def __init__(self, health, type, tile):
        self.x = tile[1] * 100 + 25
        self.y = tile[0] * 100 + 25
        self.width = 50
        self.height = 50
        self.health = health
        self.type = type
        self.dead = False
        self.tile = tile

    def checkDeath(self):
        if self.health <= 0:
            self.dead = True

    def draw(self):
        pygame.draw.rect(
            game.screen, game.ORANGE, [self.x, self.y, self.width, self.height]
        )


class MoneyTreePlant(Plant):
    def __init__(self):
        super().__init__(30, "passive", game.tile)
        self.rate = 60 * 4
        self.timer = 0

    def passive(self):
        if self.timer < self.rate:
            pass
        elif self.timer >= self.rate:
            game.MONEY = game.MONEY + 25
            self.timer = 0

        self.timer += 1


class CornPlant(Plant):
    def __init__(self):
        super().__init__(60, "shoot", game.tile)
        self.damage = 10
        self.fireRate = 80  # lower means faster shooting
        self.shootTimer = 0
        self.bulletArr = []

    # TODO: make it so that it only attacks if there is an enemy in its lane
    def attack(self):
        # if the timer is less than what it should be dont fire, otherwise do
        if self.shootTimer < self.fireRate:
            pass
        elif self.shootTimer >= self.fireRate:
            # add a new bullet to the bullet array
            self.bulletArr.append(
                utilClasses.Bullet(self, 5, self.damage, (self.y - 25) / 100)
            )
            self.shootTimer = 0

        self.shootTimer += 1
