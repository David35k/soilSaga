import pygame, pygame.freetype, random, utilClasses, spritesheet, waves

pygame.init()

# setting up the display
WIDTH, HEIGHT = 1000, 700
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Soil Saga")

clock = pygame.time.Clock()

carryOn = True
gameOver = False
won = False

# Colors
COLOR1 = (125, 125, 125)
COLOR2 = (100, 100, 100)
ORANGE = (255, 165, 0)
ORANGE2 = (240, 165, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
CANCEL_COLOR = (255, 0, 231)  # FF00E7

currentCard = 0

# MONEY!!!
MONEY = 75

# Fonts
pygame.freetype.init()
moneyFont = pygame.freetype.Font("font/font.ttf", 50)
tipFont = pygame.freetype.Font("font/font.ttf", 30)
gameOverFont = pygame.freetype.Font("font/font.ttf", 75)
gameOverSurf, gameOverRect = gameOverFont.render("Game Over!", WHITE)
questionSurf, questionRect = tipFont.render(
    "Should've planted more trees... Play again? (y/n)", WHITE
)
timerFont = pygame.freetype.Font("font/font.ttf", 25)

WAVE_TIME = 0
WAVE_NUM = 0

tip1 = utilClasses.TipWindow(
    WIDTH / 2 - 225,
    50,
    450,
    125,
    [
        "The farm needs your help!",
        "Defend the farm from",
        "the invading robots.",
    ],
    30,
    60 * 4,
)


tip2 = utilClasses.TipWindow(
    WIDTH / 2 - 300,
    50,
    600,
    150,
    [
        "You need money to place plants.",
        "Money grows on trees (obviously).",
        "Plant a tree to start earning money!",
        "Protip: lots of trees = lots of money",
    ],
    60 * 4,
    9 * 60,
)

tip3 = utilClasses.TipWindow(
    WIDTH / 2 - 300,
    50,
    600,
    200,
    [
        "Here they come!",
        "Place a corn plant in line with the",
        "robot. It will shoot automatically.",
        "Don't let the robots enter the farm!",
    ],
    30 * 60,
    34 * 60,
)

tip4 = utilClasses.TipWindow(
    WIDTH / 2 - 325,
    50,
    650,
    100,
    [
        "You can use the shovel to remove plants.",
        "No refunds!!!",
    ],
    13 * 60,
    16 * 60,
)

tip5 = utilClasses.TipWindow(
    WIDTH / 2 - 225,
    50,
    450,
    100,
    [
        "That's it from me.",
        "Good luck!",
    ],
    34 * 60,
    36 * 60,
)

tip6 = utilClasses.TipWindow(
    WIDTH / 2 - 225,
    50,
    450,
    100,
    ["You're gonna need it", ">:)"],
    36 * 60,
    37 * 60,
)

tip7 = utilClasses.TipWindow(
    WIDTH / 2 - 300,
    50,
    600,
    50,
    [
        "To place a card drag it onto the board.",
    ],
    9 * 60,
    13 * 60,
)

tipIndex = 0
tipArr = [tip1, tip2, tip3, tip4, tip5, tip6, tip7]
tipShowing = False


tiles = utilClasses.Tiles(100, 100, 5, 10)
tiles.createTiles()

# create all of the different types of cards
treeImage = pygame.image.load("images/cards/tree.png")
treeImage = pygame.transform.scale(treeImage, (96, 96))
moneyCard = utilClasses.Card(0, 50, True, "moneyTree", treeImage)
cornImage = pygame.image.load("images/cards/corn.png")
cornImage = pygame.transform.scale(cornImage, (96, 96))
cornCard = utilClasses.Card(1.1, 100, True, "corn", cornImage)
carrotImage = pygame.image.load("images/cards/carrot.png")
carrotImage = pygame.transform.scale(carrotImage, (96, 96))
carrotCard = utilClasses.Card(3.3, 500, True, "carrot", carrotImage)
cactusImage = pygame.image.load("images/cards/cactus.png")
cactusImage = pygame.transform.scale(cactusImage, (96, 96))
cactusCard = utilClasses.Card(2.2, 300, True, "cactus", cactusImage)
shovelImage = pygame.image.load("images/cards/shovel.png")
shovelImage = pygame.transform.scale(shovelImage, (96, 96))
shovelCard = utilClasses.Card(5.5, 0, True, "shovel", shovelImage)
bambooImage = pygame.image.load("images/cards/bamboo.png")
bambooImage = pygame.transform.scale(bambooImage, (96, 96))
bambooCard = utilClasses.Card(4.4, 200, True, "bamboo", bambooImage)

cards = [moneyCard, cornCard, carrotCard, cactusCard, bambooCard, shovelCard]
plants = []


enemyArr = []

IMPORT_SCALE = 3  # for images

# ---------- tile sprites ----------
tileSpritesArr = []
spritesImage = pygame.image.load("images/grass.png").convert_alpha()
tileSpriteSpritesheet = spritesheet.Spritesheet(spritesImage)

for i in range(32):
    tileSpritesArr.append(
        tileSpriteSpritesheet.get_image(i, 32, 32, 3.12, CANCEL_COLOR)
    )

# ---------- corn animations ----------
cornAnims = [[], []]
cornIdle = pygame.image.load("images/corn/cornIdle.png").convert_alpha()
cornIdleSheet = spritesheet.Spritesheet(cornIdle)
cornShoot = pygame.image.load("images/corn/cornShoot.png").convert_alpha()
cornShootSheet = spritesheet.Spritesheet(cornShoot)

for i in range(4):
    cornAnims[0].append(cornIdleSheet.get_image(i, 32, 32, IMPORT_SCALE, CANCEL_COLOR))
    cornAnims[1].append(cornShootSheet.get_image(i, 32, 32, IMPORT_SCALE, CANCEL_COLOR))

# bullet
cornBulletAnim = [[]]
cornBullet = pygame.image.load("images/corn/cornBullet.png").convert_alpha()
cornBulletSheet = spritesheet.Spritesheet(cornBullet)

for i in range(4):
    cornBulletAnim[0].append(
        cornBulletSheet.get_image(i, 32, 32, IMPORT_SCALE, CANCEL_COLOR)
    )

# ---------- tree animations ----------
moneyTreeAnims = [[], []]
moneyTreeIdle = pygame.image.load("images/moneyTree/moneyTreeIdle.png").convert_alpha()
moneyTreeIdleSheet = spritesheet.Spritesheet(moneyTreeIdle)

for i in range(4):
    moneyTreeAnims[0].append(
        moneyTreeIdleSheet.get_image(i, 32, 32, IMPORT_SCALE, CANCEL_COLOR)
    )

# ---------- carrot animations ----------
carrotAnims = [[], []]
carrotIdle = pygame.image.load("images/carrot/carrotIdle.png").convert_alpha()
carrotIdleSheet = spritesheet.Spritesheet(carrotIdle)

for i in range(4):
    carrotAnims[0].append(
        carrotIdleSheet.get_image(i, 32, 32, IMPORT_SCALE, CANCEL_COLOR)
    )

# ---------- cactus animations ----------
cactusAnims = [[], []]
cactusIdle = pygame.image.load("images/cactus/cactusIdle.png").convert_alpha()
cactusIdleSheet = spritesheet.Spritesheet(cactusIdle)
cactusShoot = pygame.image.load("images/cactus/cactusShoot.png").convert_alpha()
cactusShootSheet = spritesheet.Spritesheet(cactusShoot)

# bullet
cactusBulletAnim = [[]]
cactusBullet = pygame.image.load("images/cactus/bullet.png").convert_alpha()
cactusBulletSheet = spritesheet.Spritesheet(cactusBullet)

for i in range(4):
    cactusBulletAnim[0].append(
        cactusBulletSheet.get_image(i, 32, 32, IMPORT_SCALE, CANCEL_COLOR)
    )

for i in range(4):
    cactusAnims[0].append(
        cactusIdleSheet.get_image(i, 32, 32, IMPORT_SCALE, CANCEL_COLOR)
    )
    cactusAnims[1].append(
        cactusShootSheet.get_image(i, 32, 32, IMPORT_SCALE, CANCEL_COLOR)
    )

# ---------- bamboo animations ----------
bambooAnims = [[], []]
bambooIdle = pygame.image.load("images/bamboo/bambooIdle.png").convert_alpha()
bambooIdleSheet = spritesheet.Spritesheet(bambooIdle)

for i in range(4):
    bambooAnims[0].append(
        bambooIdleSheet.get_image(i, 32, 32, IMPORT_SCALE, CANCEL_COLOR)
    )

# bullet
bambooBulletAnim = [[], []]
bambooBullet = pygame.image.load("images/bamboo/bullet.png").convert_alpha()
bambooBulletSheet = spritesheet.Spritesheet(bambooBullet)

# bullet2
bambooBullet2 = pygame.image.load("images/bamboo/bulletInverted.png").convert_alpha()
bambooBulletSheet2 = spritesheet.Spritesheet(bambooBullet2)

for i in range(4):
    bambooBulletAnim[0].append(
        bambooBulletSheet.get_image(i, 32, 32, IMPORT_SCALE, CANCEL_COLOR)
    )
    bambooBulletAnim[1].append(
        bambooBulletSheet2.get_image(i, 32, 32, IMPORT_SCALE, CANCEL_COLOR)
    )

for tile in tiles.tileArr:
    tile[4] = tileSpritesArr[random.randint(1, 31)]


# ---------- all robots animations ----------
robotAnims = [[], [], [], [], []]

robotBasic = pygame.image.load("images/robots/robotBasic.png").convert_alpha()
robotBasicSpritesheet = spritesheet.Spritesheet(robotBasic)

assaultBot = pygame.image.load("images/robots/assaultBot.png").convert_alpha()
assaultBotSpritesheet = spritesheet.Spritesheet(assaultBot)

tractorBot = pygame.image.load("images/robots/tractorBot.png").convert_alpha()
tractorBotSpritesheet = spritesheet.Spritesheet(tractorBot)

teleportBot = pygame.image.load("images/robots/teleportBot.png").convert_alpha()
teleportBotSpritesheet = spritesheet.Spritesheet(teleportBot)

laneBot = pygame.image.load("images/robots/laneBot.png").convert_alpha()
laneBotSpritesheet = spritesheet.Spritesheet(laneBot)

for i in range(4):
    robotAnims[0].append(robotBasicSpritesheet.get_image(i, 20, 20, 4, CANCEL_COLOR))
    robotAnims[2].append(tractorBotSpritesheet.get_image(i, 24, 32, 4, CANCEL_COLOR))
    robotAnims[3].append(teleportBotSpritesheet.get_image(i, 24, 32, 4, CANCEL_COLOR))
    robotAnims[1].append(assaultBotSpritesheet.get_image(i, 24, 32, 4, CANCEL_COLOR))
    robotAnims[4].append(laneBotSpritesheet.get_image(i, 24, 32, 4, CANCEL_COLOR))

allWaves = [
    waves.wave1,
    waves.wave2,
    waves.wave3,
    waves.wave4,
    waves.wave5,
    waves.wave6,
    waves.wave7,
    waves.wave8,
    waves.wave9,
    waves.wave10,
]

while carryOn:
    if not gameOver:
        # check for input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
                gameOver = False

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
                    currentCard.posy = HEIGHT - currentCard.height - 50

                    # if hovering over a vacant tile place the plant
                    for tile in tiles.tileArr:
                        if (
                            pygame.mouse.get_pos()[0] >= tiles.tileWidth * tile[1]
                            and pygame.mouse.get_pos()[0]
                            <= tiles.tileWidth * tile[1] + tiles.tileWidth
                            and pygame.mouse.get_pos()[1] >= tiles.tileWidth * tile[0]
                            and pygame.mouse.get_pos()[1]
                            <= tiles.tileWidth * tile[0] + tiles.tileHeight
                            and MONEY >= currentCard.cost
                        ):
                            if currentCard.plantName == "shovel" and not tile[2]:
                                for plant in plants:
                                    if plant.tile == tile:
                                        plant.health = 0
                            if currentCard.plantName != "shovel" and tile[2]:
                                currentCard.place()
                                MONEY -= currentCard.cost
                                tile[2] = False  # cant plant there anymore

                    currentCard = 0

        # update positions of cards
        if currentCard:
            if currentCard.picked:
                currentCard.posx = pygame.mouse.get_pos()[0] - 0.5 * currentCard.width
                currentCard.posy = pygame.mouse.get_pos()[1] - 0.5 * currentCard.height

        # change waves (very bad code) and spawn enemies
        if waves.wave1.length > 0:
            waves.wave1.spawnEnemies()
            waves.wave1.length -= 1
            WAVE_NUM = "Preperation"
            WAVE_TIME = waves.wave1.length / 60
        elif waves.wave1.length <= 0 and waves.wave2.length > 0:
            waves.wave2.spawnEnemies()
            waves.wave2.length -= 1
            WAVE_NUM = 2
            WAVE_TIME = waves.wave2.length / 60
        elif waves.wave2.length <= 0 and waves.wave3.length > 0:
            waves.wave3.spawnEnemies()
            waves.wave3.length -= 1
            WAVE_NUM = 3
            WAVE_TIME = waves.wave3.length / 60
        elif waves.wave3.length <= 0 and waves.wave4.length > 0:
            waves.wave4.spawnEnemies()
            waves.wave4.length -= 1
            WAVE_NUM = 4
            WAVE_TIME = waves.wave4.length / 60
        elif waves.wave4.length <= 0 and waves.wave5.length > 0:
            waves.wave5.spawnEnemies()
            waves.wave5.length -= 1
            WAVE_NUM = 5
            WAVE_TIME = waves.wave5.length / 60
        elif waves.wave5.length <= 0 and waves.wave6.length > 0:
            waves.wave6.spawnEnemies()
            waves.wave6.length -= 1
            WAVE_NUM = 6
            WAVE_TIME = waves.wave6.length / 60
        elif waves.wave6.length <= 0 and waves.wave7.length > 0:
            waves.wave7.spawnEnemies()
            waves.wave7.length -= 1
            WAVE_NUM = 7
            WAVE_TIME = waves.wave7.length / 60
        elif waves.wave7.length <= 0 and waves.wave8.length > 0:
            waves.wave8.spawnEnemies()
            waves.wave8.length -= 1
            WAVE_NUM = 8
            WAVE_TIME = waves.wave8.length / 60
        elif waves.wave8.length <= 0 and waves.wave9.length > 0:
            waves.wave9.spawnEnemies()
            waves.wave9.length -= 1
            WAVE_NUM = 9
            WAVE_TIME = waves.wave9.length / 60
        elif waves.wave9.length <= 0 and waves.wave10.length > 0:
            waves.wave10.spawnEnemies()
            waves.wave10.length -= 1
            WAVE_NUM = 10
            WAVE_TIME = waves.wave10.length / 60

        # check if won game
        if waves.wave10.length <= 0 and not gameOver:
            won = True
            gameOver = True

        # plants attack
        for plant in plants:
            plant.checkDeath()
            if plant.dead:
                plant.tile[2] = True
                plants.remove(plant)
                del plant
            else:
                if plant.type == "passive":
                    plant.passive()
                elif plant.type == "shoot":
                    plant.attack()

                    # bullet move
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
                MONEY += 10
            else:
                # enemies move
                enemy.move()

        # check for enemy tp
        for enemy in enemyArr:
            if enemy.name == "teleport":
                enemy.teleport()
            elif enemy.name == "laneSwitch":
                enemy.switch()

        # update text
        moneySurf, moneyRect = moneyFont.render("$" + str(MONEY), BLACK)
        timerSurf, timerRect = timerFont.render(
            "Wave " + str(WAVE_NUM) + ", Next wave: " + str(round(WAVE_TIME)), WHITE
        )

        # clear screen
        pygame.draw.rect(screen, (50, 50, 50), [0, 0, WIDTH, HEIGHT])

        # draw tiles
        tiles.draw()

        for tip in tipArr:
            tip.draw()
            if tip.showing:
                tipShowing = True

        # draw the card bar
        pygame.draw.rect(screen, (240, 240, 240), [0, HEIGHT - 200, WIDTH, 200])

        # draw the cards
        for card in cards:
            card.draw()

        # draw the plants and their bullets (if they have any)
        for plant in plants:
            plant.sprite.animate(plant.x - 25, plant.y - 25)

            if plant.type == "shoot":
                for bullet in plant.bulletArr:
                    if not bullet.destroy:
                        bullet.sprite.animate(bullet.x - 25, bullet.y - 25)

        # draw the enemies
        for enemy in enemyArr:
            if enemy.name == "basic":
                enemy.sprite.animate(enemy.x - 15, enemy.y - 15)
            else:
                enemy.sprite.animate(enemy.x - 15, enemy.y - 50)

        # render text
        screen.blit(
            moneySurf, (WIDTH - moneyRect.width - 10, HEIGHT - moneyRect.height - 10)
        )
        screen.blit(timerSurf, (WIDTH / 2 - timerRect.width / 2, 5))

    elif gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
                gameOver = False

            if event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()

                if event.key == pygame.K_y:
                    gameOver = False
                    # restart
                    MONEY = 75
                    waves.wave1.length = 30 * 60 + 1
                    waves.wave2.length = 45 * 60 + 1
                    waves.wave3.length = 31 * 60 + 1
                    waves.wave4.length = 31 * 60 + 1
                    waves.wave5.length = 50 * 60 + 1
                    waves.wave6.length = 55 * 60 + 1
                    waves.wave7.length = 50 * 60 + 1
                    waves.wave8.length = 65 * 60 + 1
                    waves.wave9.length = 130 * 60 + 1
                    waves.wave10.length = 20 * 60 + 1

                    for wave in allWaves:
                        wave.timer = 0

                    for tip in tipArr:
                        tip.drawTimer = 0

                    tiles = utilClasses.Tiles(100, 100, 5, 10)
                    tiles.createTiles()

                    for tile in tiles.tileArr:
                        tile[4] = tileSpritesArr[random.randint(1, 31)]

                    while len(plants) > 0:
                        plants.remove(plants[0])

                    while len(enemyArr) > 0:
                        enemyArr.remove(enemyArr[0])
                        # del enemyArr[0]

                if event.key == pygame.K_n:
                    carryOn = False

        # clear screen
        pygame.draw.rect(screen, (50, 50, 50), [0, 0, WIDTH, HEIGHT])

        if not won:
            gameOverSurf, gameOverRect = gameOverFont.render("Game Over!", WHITE)
            questionSurf, questionRect = tipFont.render(
                "Should've planted more trees... Play again? (y/n)", WHITE
            )
        elif won:
            gameOverSurf, gameOverRect = gameOverFont.render("You win!", WHITE)
            questionSurf, questionRect = tipFont.render(
                "Nice! Play again? (y/n)", WHITE
            )

        screen.blit(
            gameOverSurf,
            (WIDTH / 2 - gameOverRect.width / 2, HEIGHT / 2 - gameOverRect.height / 2),
        )
        screen.blit(
            questionSurf,
            (
                WIDTH / 2 - questionRect.width / 2,
                HEIGHT / 2 - questionRect.height / 2 + 50,
            ),
        )

    # update screen
    pygame.display.update()
    clock.tick(60)


pygame.quit()
