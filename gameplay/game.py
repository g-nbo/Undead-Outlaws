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
scale = 0.7

characterSprite = pygame.image.load("../images/player_2.png")
characterSprite = pygame.transform.scale(characterSprite, (characterSprite.get_width() * scale, characterSprite.get_height() * scale))

charRect = characterSprite.get_rect()
charRect.center = (0 + 90, SCREEN_HEIGHT - 100)

playerHealth = 5
hearts = pygame.image.load("../images/hearts_5.png")
heartsRect = hearts.get_rect()
# heartsRect.center = (220, SCREEN_HEIGHT // 10)
heartsRect.center = (SCREEN_WIDTH - 210, SCREEN_HEIGHT // 10)

# Create enemy
dgSprite = pygame.image.load("../images/dgZomb.png")
lgSprite = pygame.image.load("../images/lgZomb.png")
redSprite = pygame.image.load("../images/redZomb.png")
purpleSprite = pygame.image.load("../images/purpZomb.png")

zomb1 = classes.Enemy(SCREEN_WIDTH - 70, SCREEN_HEIGHT - 140, "zombie", 0.5, dgSprite)
enemyArr = [zomb1]

# level vars
level = 1
fivePlayed = False
enemyCount = 0
waited = False

# create timers/delay
start = time.time()

# text/fonts
gameFont = pygame.font.SysFont('segoeprint', 64)
levelText = pygame.image.load("../images/level1_real.png")
levelText = pygame.transform.scale(levelText, (800, 450))
levelText_rect = levelText.get_rect()
# levelText_rect.center = (SCREEN_WIDTH - 170, SCREEN_HEIGHT // 12)
levelText_rect.center = (140, SCREEN_HEIGHT // 12)

healthText = gameFont.render(f"Health: {playerHealth}", None, (255, 255, 255))
healthText_rect = healthText.get_rect()
healthText_rect.center = (140, SCREEN_HEIGHT // 10)

# backgrounds
bg = pygame.image.load("../images/level1_bg.jpg")
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

# initialize music
pygame.mixer.init()
menuMusic = pygame.mixer.Sound("../sounds/intense-horror-music-01-14890.mp3")
menuMusic.set_volume(0.6)

gameMusic = pygame.mixer.Sound("../sounds/horror_music_clipped.mp3")
gameMusic.play()
# menuMusic.play()

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
            levelText = pygame.image.load("../images/level1_real.png")
            levelText = pygame.transform.scale(levelText, (800, 450))
        case 2:
            bg = pygame.image.load("../images/level2_bg.jpg")
            bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
            levelText = pygame.image.load("../images/level2.png")
            levelText = pygame.transform.scale(levelText, (800, 450))
        case 3:
            bg = pygame.image.load("../images/level3_bg.png")
            bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
            levelText = pygame.image.load("../images/level3.png")
            levelText = pygame.transform.scale(levelText, (800, 450))
        case 4:
            bg = pygame.image.load("../images/level4_bg.png")
            bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
            levelText = pygame.image.load("../images/level4.png")
            levelText = pygame.transform.scale(levelText, (800, 450))
        case _:
            pass

    match playerHealth:
        case 5:
            hearts = pygame.image.load("../images/hearts_5.png")
        case 4:
            hearts = pygame.image.load("../images/hearts_4.png")
        case 3:
            hearts = pygame.image.load("../images/hearts_3.png")
        case 2:
            hearts = pygame.image.load("../images/hearts_2.png")
        case 1:
            hearts = pygame.image.load("../images/hearts_1.png")
        case 0:
            hearts = pygame.image.load("../images/hearts_0.png")
        case _:
            hearts = pygame.image.load("../images/hearts_5.png")

    screen.blit(bg, (0, 0))
    screen.blit(characterSprite, charRect)
    screen.blit(zomb1.image, zomb1.rect)
    screen.blit(hearts, heartsRect)

    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    # levelText = gameFont.render(f"Level: {level}", None, (255, 255, 255))
    healthText = gameFont.render(f"Health: {playerHealth}", None, (255, 255, 255))

    screen.blit(levelText, levelText_rect)
    # screen.blit(healthText, healthText_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_ESCAPE]:
            run = False

        if keys[pygame.K_a] and charRect.left > -80:
             charRect = charRect.move(-15, 0)
        if keys[pygame.K_d] and charRect.right < 1230:
            charRect = charRect.move(15, 0)

        for i in range(len(enemyArr)):
            if enemyArr[i].rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
                enemyArr[i].health -= 1
                shootSound = pygame.mixer.Sound("../sounds/shoot-1-81135.mp3")
                shootSound.set_volume(0.2)
                shootSound.play()

            if enemyArr[i].health <= 0:
                enemyArr[i].canHit = False
                enemyArr[i].rect = enemyArr[i].rect.move(-5000, -5000)


    for i in range(len(enemyArr)):
        dgZomb = classes.Enemy(SCREEN_WIDTH - 70, SCREEN_HEIGHT - 140, "zombie", 0.5, dgSprite)
        lgZomb = classes.Enemy(SCREEN_WIDTH - 70, SCREEN_HEIGHT - 140, "zombie", 0.5, lgSprite)
        redZomb = classes.Enemy(SCREEN_WIDTH - 70, SCREEN_HEIGHT - 140, "zombie", 0.5, redSprite)
        purpZomb = classes.Enemy(SCREEN_WIDTH - 70, SCREEN_HEIGHT - 140, "zombie", 0.5, purpleSprite)



        screen.blit(enemyArr[i].image, enemyArr[i].rect)
        enemyArr[i].rect = enemyArr[i].rect.move(-(level * 2), 0)

        if charRect.colliderect(enemyArr[i].rect) and playerHealth > 1 and enemyArr[i].canHit:
            biteSound = pygame.mixer.Sound("../sounds/zombie-bite-96528.mp3")
            biteSound.set_volume(0.5)
            biteSound.play()
            playerHealth -= 1
            enemyArr[i].canHit = False
            print("player health:", playerHealth)
        elif charRect.colliderect(enemyArr[i].rect) and playerHealth == 1:
            # Game needs to restart completely if this happens
            # level = 1
            # enemyCount = 0
            # waited = False
            playerHealth -= 1
            # start = time.time()
            print("player dead")

        if random.randint(1, 300) == 300 and enemyCount != (level * 2):
            match random.randint(1, 4):
                case 1:
                    enemyArr.append(dgZomb)
                case 2:
                    enemyArr.append(lgZomb)
                case 3:
                    enemyArr.append(redZomb)
                case 4:
                    enemyArr.append(purpZomb)

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

