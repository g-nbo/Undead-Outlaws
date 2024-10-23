import pygame
import classes
import random
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
scale = 0.3

characterSprite = pygame.image.load("../images/test-sprite-game.png")
characterSprite = pygame.transform.scale(characterSprite, (characterSprite.get_width() * scale, characterSprite.get_height() * scale))

charRect = characterSprite.get_rect()
charRect.center = (0 + 70, SCREEN_HEIGHT - 70)

playerHealth = 5
playerCanShoot = True

# Create enemy
enemySprite = pygame.image.load("../images/dino-enemy-sprite.png")
# enemySprite = pygame.transform.scale(enemySprite, (enemySprite.get_width() * scale, enemySprite.get_height() * scale))
#
# enemyRect = enemySprite.get_rect()
# enemyRect.center = (SCREEN_WIDTH - 70, SCREEN_HEIGHT - 70)
# canHit = True

# enemyHealth = 1

zomb1 = classes.Enemy(SCREEN_WIDTH - 70, SCREEN_HEIGHT - 70, "zombie", 0.3, enemySprite)
enemyArr = [zomb1]

# Time
clock = pygame.time.Clock()

# Create basic game loop
run = True
while run:
    screen.fill(("black"))

    screen.blit(characterSprite, charRect)
    screen.blit(zomb1.image, zomb1.rect)

    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if keys[pygame.K_a] and charRect.left > -30:
             charRect = charRect.move(-15, 0)
        if keys[pygame.K_d] and charRect.right < 1030:
            charRect = charRect.move(15, 0)

        for i in range(len(enemyArr)):

            if enemyArr[i].rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
                enemyArr[i].health -= 1

            if enemyArr[i].health <= 0:
                enemyArr[i].canHit = False
                enemyArr[i].rect = enemyArr[i].rect.move(-5000, -5000)


    for i in range(len(enemyArr)):


        zomb = classes.Enemy(SCREEN_WIDTH - 70, SCREEN_HEIGHT - 70, "zombie", 0.3, enemySprite)

        screen.blit(enemyArr[i].image, enemyArr[i].rect)\

        enemyArr[i].rect = enemyArr[i].rect.move(-3, 0)


        if charRect.colliderect(enemyArr[i].rect) and playerHealth > 1 and enemyArr[i].canHit:
            playerHealth -= 1
            enemyArr[i].canHit = False
            print("player health:", playerHealth)
        elif charRect.colliderect(enemyArr[i].rect) and playerHealth == 1:
            print("player dead")

        if random.randint(1, 400) == 400 and enemyArr[i].alive:
            enemyArr.append(zomb)
            print("appending")



    pygame.display.update()

    # Slow the game to update 60 times per second
    clock.tick(60)

pygame.quit()

