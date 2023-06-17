import pygame, random, utilClasses, spritesheet

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
BLACK = (0, 0, 0)
CANCEL_COLOR = (255, 0, 231)

currentCard = 0

# MONEY!!!
MONEY = 1000

# Fonts
moneyFont = pygame.font.SysFont(None, 50)

tiles = utilClasses.Tiles(100, 100, 5, 10)
tiles.createTiles()

# create all of the different types of cards
moneyCard = utilClasses.Card(0, 50, True, "moneyTree")
cornCard = utilClasses.Card(1.1, 100, True, "corn")
cornCard = utilClasses.Card(1.1, 100, True, "corn")


cards = [moneyCard, cornCard]
plants = []

testWave = utilClasses.Wave(
    [["zombieBasic", 120], ["zombieBasic", 500], ["zombieBasic", 300]], 60 * 15
)
susWave = utilClasses.Wave(
    [
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
        ["zombieBasic", random.randint(0, 1000)],
    ],
    1000,
)

enemyArr = []

sussy = pygame.image.load("images\corn\cornIdle.png").convert_alpha()

sprite_sheet = spritesheet.Spritesheet(sussy)

bruh = sprite_sheet.get_image(0, 32, 32, 2, CANCEL_COLOR)
bruh2 = sprite_sheet.get_image(1, 32, 32, 2, CANCEL_COLOR)

while carryOn:
    # check for input
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

    # update text
    moneyTextRect = moneyFont.render(str(MONEY), True, (0, 0, 0))

    # clear screen
    pygame.draw.rect(screen, (50, 50, 50), [0, 0, WIDTH, HEIGHT])

    # draw tiles
    # tiles.draw()

    # draw the card bar
    pygame.draw.rect(screen, WHITE, [0, HEIGHT - 150, WIDTH, 150])

    # draw the cards
    for card in cards:
        card.draw()

    # draw the plants and their bullets (if they have any)
    for plant in plants:
        plant.draw()

        if plant.type == "shoot":
            for bullet in plant.bulletArr:
                if not bullet.destroy:
                    bullet.draw()

    # draw the enemies
    for enemy in enemyArr:
        enemy.draw()

    screen.blit(bruh, (0, 0))
    screen.blit(bruh2, (32, 0))

    screen.blit(
        moneyTextRect,
        (
            WIDTH - moneyTextRect.get_width() - 10,
            HEIGHT - moneyTextRect.get_height() - 10,
        ),
    )

    # update screen
    pygame.display.update()
    clock.tick(60)


pygame.quit()
