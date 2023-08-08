import pygame, game, utilClasses, spritesheet


class Plant:
    def __init__(self, health, type, tile, sprite):
        self.x = tile[1] * 100 + 25
        self.y = tile[0] * 100 + 25
        self.width = 50
        self.height = 50
        self.health = health
        self.type = type
        self.dead = False
        self.tile = tile
        self.sprite = sprite

    def checkDeath(self):
        if self.health <= 0:
            self.dead = True

    def draw(self):
        pygame.draw.rect(
            game.screen, game.ORANGE, [self.x, self.y, self.width, self.height]
        )


class MoneyTreePlant(Plant):
    def __init__(self):
        super().__init__(
            30, "passive", game.tile, spritesheet.Sprite(game.moneyTreeAnims, 0, 4, 0)
        )
        self.rate = 60 * 4
        self.timer = 0
        self.name = "tree"  # for debugging

    def passive(self):
        if self.timer < self.rate:
            pass
        elif self.timer >= self.rate:
            game.MONEY = game.MONEY + 25
            self.timer = 0

        self.timer += 1


class CornPlant(Plant):
    def __init__(self):
        super().__init__(
            60, "shoot", game.tile, spritesheet.Sprite(game.cornAnims, 0, 4, 0)
        )
        self.damage = 10
        self.fireRate = 65  # lower means faster shooting
        self.shootTimer = 0
        self.bulletArr = []
        self.name = "corn"  # for debugging

    def attack(self):
        # check if enemies in the same lane
        shoot = False
        for enemy in game.enemyArr:
            if enemy.row == self.tile[0]:
                shoot = True

        if shoot:
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


class CarrotPlant(Plant):
    def __init__(self):
        super().__init__(
            65, "shoot", game.tile, spritesheet.Sprite(game.carrotAnims, 0, 4, 0)
        )
        self.damage = 15
        self.fireRate = 200  # lower means faster shooting
        self.shootTimer = 0
        self.bulletArr = []
        self.name = "carrot"  # for debugging
        self.bulletCount = 0

    def attack(self):
        # check if enemies in the same lane
        shoot = False
        for enemy in game.enemyArr:
            if enemy.row == self.tile[0]:
                shoot = True

        if shoot:
            # if the timer is less than what it should be dont fire, otherwise do
            if self.shootTimer < self.fireRate:
                pass
            elif self.shootTimer >= self.fireRate:
                # add 6 new bullets to the bullet array

                if self.shootTimer % 10 == 0:
                    self.bulletArr.append(
                        utilClasses.Bullet(self, 4, self.damage, (self.y - 25) / 100)
                    )
                    self.bulletCount += 1
                if self.bulletCount == 6:
                    self.shootTimer = 0
                    self.bulletCount = 0

        self.shootTimer += 1


class CactusPlant(Plant):
    def __init__(self):
        super().__init__(
            50, "shoot", game.tile, spritesheet.Sprite(game.cactusAnims, 0, 4, 0)
        )
        self.damage = 5
        self.fireRate = 150  # lower means faster shooting
        self.shootTimer = 0
        self.bulletArr = []
        self.name = "cactus"  # for debugging

    def attack(self):
        # check if enemies are in the same lane
        shoot = False
        for enemy in game.enemyArr:
            if enemy.row == self.tile[0]:
                shoot = True

        if shoot:
            # if the timer is less than what it should be dont fire, otherwise do
            if self.shootTimer < self.fireRate:
                pass
            elif self.shootTimer >= self.fireRate:
                # add a new bullet to the bullet array
                self.bulletArr.append(
                    utilClasses.Bullet(self, 8, self.damage, (self.y - 25) / 100)
                )
                self.shootTimer = 0
        self.shootTimer += 1

class BambooPlant(Plant):
    def __init__(self):
        super().__init__(30, "shoot", game.tile, spritesheet.Sprite(game.bambooAnims, 0, 4, 0))
        self.damage = 8
        self.fireRate = 80  # lower means faster shooting
        self.shootTimer = 0
        self.bulletArr = []
        self.name = "bamboo"  # for debugging

    def attack(self):
        # check if enemies are in the same lane
        shoot = False
        for enemy in game.enemyArr:
            if enemy.row == self.tile[0]:
                shoot = True

        if shoot:
            # if the timer is less than what it should be dont fire, otherwise do
            if self.shootTimer < self.fireRate:
                pass
            elif self.shootTimer >= self.fireRate:
                # add two new bullets to the bullet array, one going the opposite way
                self.bulletArr.append(
                    utilClasses.Bullet(self, 5, self.damage, (self.y - 25) / 100)
                )
                self.bulletArr.append(
                    utilClasses.Bullet(self, -5, self.damage, (self.y - 25) / 100)
                )
                self.shootTimer = 0
        self.shootTimer += 1