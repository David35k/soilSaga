import pygame, game, utilClasses, spritesheet, random


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
        self.rate = 60 * 9
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
        self.damage = 5.5
        self.fireRate = 60  # lower means faster shooting
        self.shootTimer = (
            self.fireRate - 15
        )  # 15 is the number of frames until the shot is fired in the animation
        self.bulletArr = []
        self.name = "corn"  # for debugging
        self.currentAnim = "idle"

    def attack(self):
        # check if enemies in the same lane
        shoot = False
        for enemy in game.enemyArr:
            if enemy.row == self.tile[0]:
                shoot = True

        # change the animation
        # the code for this plant is much easier as the shooting perfectly lines up with its animation
        if (
            self.currentAnim == "idle"
            and shoot
            and self.shootTimer == self.fireRate - 15
        ):
            self.currentAnim = "shoot"
            self.sprite = spritesheet.Sprite(game.cornAnims, 1, 4, 0)
        elif self.currentAnim == "shoot" and not shoot:
            self.currentAnim = "idle"
            self.sprite = spritesheet.Sprite(game.cornAnims, 0, 4, random.randint(0, 3))

        # shoot!!!
        if shoot:
            # if the timer is less than what it should be dont fire, otherwise do
            if self.shootTimer < self.fireRate:
                pass
            elif self.shootTimer >= self.fireRate:
                # add a new bullet to the bullet array
                self.bulletArr.append(
                    utilClasses.Bullet(
                        self,
                        5,
                        self.damage,
                        (self.y - 25) / 100,
                        50,
                        20,
                        spritesheet.Sprite(game.cornBulletAnim, 0, 4, 0),
                    )
                )
                self.shootTimer = 0
            self.shootTimer += 1

        if not shoot:
            self.shootTimer = self.fireRate - 15


class CarrotPlant(Plant):
    def __init__(self):
        super().__init__(
            65, "shoot", game.tile, spritesheet.Sprite(game.carrotAnims, 0, 4, 0)
        )
        self.damage = 9
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
                        utilClasses.Bullet(
                            self,
                            4,
                            self.damage,
                            (self.y - 25) / 100,
                            0,
                            0,
                            spritesheet.Sprite(game.cactusBulletAnim, 0, 4, 0),
                        )
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
        self.damage = 9
        self.fireRate = 150  # lower means faster shooting
        self.shootTimer = self.fireRate - 45
        self.bulletArr = []
        self.name = "cactus"  # for debugging
        self.currentAnim = "idle"

    def attack(self):
        # check if enemies are in the same lane
        shoot = False
        for enemy in game.enemyArr:
            if enemy.row == self.tile[0]:
                shoot = True

        # change the animation
        if (
            self.shootTimer <= self.fireRate - 45
            and shoot
            and self.currentAnim != "idle"
        ):
            self.currentAnim = "idle"
            self.sprite = spritesheet.Sprite(
                game.cactusAnims, 0, 4, random.randint(0, 3)
            )
        elif (
            self.currentAnim == "idle"
            and shoot
            and self.shootTimer == self.fireRate - 45
        ):
            self.currentAnim = "shoot"
            self.sprite = spritesheet.Sprite(game.cactusAnims, 1, 5, 0)
        elif not shoot and self.currentAnim != "idle":
            self.currentAnim = "idle"
            self.sprite = spritesheet.Sprite(
                game.cactusAnims, 0, 4, random.randint(0, 3)
            )

        if shoot:
            # if the timer is less than what it should be dont fire, otherwise do
            if self.shootTimer < self.fireRate:
                pass
            elif self.shootTimer >= self.fireRate:
                # add a new bullet to the bullet array
                self.bulletArr.append(
                    utilClasses.Bullet(
                        self,
                        8,
                        self.damage,
                        (self.y - 25) / 100,
                        0,
                        0,
                        spritesheet.Sprite(game.cactusBulletAnim, 0, 4, 0),
                    )
                )
                self.shootTimer = 0
            self.shootTimer += 1

        if not shoot:
            self.shootTimer = self.fireRate - 45


class BambooPlant(Plant):
    def __init__(self):
        super().__init__(
            30, "shoot", game.tile, spritesheet.Sprite(game.bambooAnims, 0, 4, 0)
        )
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
