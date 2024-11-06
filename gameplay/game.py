import pygame
import classes
import random
import time
print("hello world!")

pygame.init()

# Create screen
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.6)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Undead Outlaws")

# Create initial character
x = 200
y = 200
scale = 0.5

characterSprite = pygame.image.load("../images/player_2.png")
characterSprite = pygame.transform.scale(characterSprite, (characterSprite.get_width() * scale, characterSprite.get_height() * scale))

charRect = characterSprite.get_rect()
charRect.center = (0 + 70, SCREEN_HEIGHT - 80)

playerHealth = 3

# Create enemy
enemySprite = pygame.image.load("../images/zombie_2.png")
zomb1 = classes.Enemy(SCREEN_WIDTH - 70, SCREEN_HEIGHT - 110, "zombie", 0.6, enemySprite)
enemyArr = [zomb1]

# level vars
level = 1
fivePlayed = False
enemyCount = 0
waited = False

# create timers/delay
start = time.time()

# text/fonts
gameFont = pygame.font.Font(None, 64)
levelText = gameFont.render(f"Level: {level}", None, (255, 255, 255))
levelText_rect = levelText.get_rect()
levelText_rect.center = (SCREEN_WIDTH - 120, SCREEN_HEIGHT // 10)

healthText = gameFont.render(f"Health: {playerHealth}", None, (255, 255, 255))
healthText_rect = healthText.get_rect()
healthText_rect.center = (140, SCREEN_HEIGHT // 10)

# backgrounds
bg = pygame.image.load("../images/zombie_background.jpg")
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

# initialize music
pygame.mixer.init()

# Time
clock = pygame.time.Clock()


# Create basic game loop
run = True
while run:
    screen.fill(("black"))

    # change things like background depending on level using switch statement
    match level:
        case 1:
            bg = pygame.image.load("../images/level1_bg.jpg")
            bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        case 2:
            bg = pygame.image.load("../images/level2_bg.jpg")
            bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        case 3:
            bg = pygame.image.load("../images/level3_bg.png")
            bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        case 4:
            bg = pygame.image.load("../images/level4_bg.png")
            bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        case _:
            pass

    screen.blit(bg, (0, 0))
    screen.blit(characterSprite, charRect)
    screen.blit(zomb1.image, zomb1.rect)

    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    levelText = gameFont.render(f"Level: {level}", None, (255, 255, 255))
    healthText = gameFont.render(f"Health: {playerHealth}", None, (255, 255, 255))

    screen.blit(levelText, levelText_rect)
    screen.blit(healthText, healthText_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_ESCAPE]:
            run = False

        if keys[pygame.K_a] and charRect.left > -30:
             charRect = charRect.move(-15, 0)
        if keys[pygame.K_d] and charRect.right < 1230:
            charRect = charRect.move(15, 0)

        for i in range(len(enemyArr)):
            if enemyArr[i].rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
                enemyArr[i].health -= 1
                shootSound = pygame.mixer.Sound("../sounds/shoot-1-81135.mp3")
                shootSound.play()

            if enemyArr[i].health <= 0:
                enemyArr[i].canHit = False
                enemyArr[i].rect = enemyArr[i].rect.move(-5000, -5000)


    for i in range(len(enemyArr)):
        zomb = classes.Enemy(SCREEN_WIDTH - 70, SCREEN_HEIGHT - 100, "zombie", 0.6, enemySprite)
        screen.blit(enemyArr[i].image, enemyArr[i].rect)
        enemyArr[i].rect = enemyArr[i].rect.move(-(level * 2), 0)

        if charRect.colliderect(enemyArr[i].rect) and playerHealth > 1 and enemyArr[i].canHit:
            biteSound = pygame.mixer.Sound("../sounds/zombie-bite-96528.mp3")
            biteSound.play()
            playerHealth -= 1
            enemyArr[i].canHit = False
            print("player health:", playerHealth)
        elif charRect.colliderect(enemyArr[i].rect) and playerHealth == 1:
            # Game needs to restart completely if this happens
            # level = 1
            # enemyCount = 0
            # waited = False
            playerHealth = 10
            # start = time.time()
            print("player dead")

        if random.randint(1, 500) == 300 and enemyCount != (level * 2):
            # match random.randint(1, 4):
            #     case 1:

            enemyArr.append(zomb)
            enemyCount += 1
            print("appending")

        if enemyCount == (level * 2) and not waited:
            start = time.time()
            waited = True

        if enemyCount == (level * 2) and time.time() - start > 5 and waited and level < 4:
            print("waited 3 seconds, next level")
            enemyCount = 0
            level += 1
            start = time.time()
            waited = False

    pygame.display.update()

    # Slow the game to update 60 times per second
    clock.tick(60)

pygame.quit()

