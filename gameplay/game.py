import pygame
print("hello world!")

pygame.init()

# Create screen
SCREEN_WIDTH = 1000
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

# Create enemy
enemySprite = pygame.image.load("../images/dino-enemy-sprite.png")
enemySprite = pygame.transform.scale(enemySprite, (enemySprite.get_width() * scale, enemySprite.get_height() * scale))

enemyRect = enemySprite.get_rect()
enemyRect.center = (SCREEN_WIDTH - 70, SCREEN_HEIGHT - 70)
eHasHit = False

# Time
clock = pygame.time.Clock()

# Create basic game loop
run = True
while run:
    screen.fill(("BLACK"))

    screen.blit(characterSprite, charRect)
    screen.blit(enemySprite, enemyRect)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if keys[pygame.K_a] and charRect.left > -30:
             charRect = charRect.move(-15, 0)
        if keys[pygame.K_d] and charRect.right < 1030:
            charRect = charRect.move(15, 0)



    enemyRect = enemyRect.move(-3, 0)
    if charRect.colliderect(enemyRect) and playerHealth > 1 and not eHasHit:
        playerHealth -= 1
        eHasHit = True
        print("player health:", playerHealth)
    elif charRect.colliderect(enemyRect) and playerHealth == 1:
        print("player dead")


    pygame.display.update()

    # Slow the game to update 60 times per second
    clock.tick(60)

pygame.quit()

