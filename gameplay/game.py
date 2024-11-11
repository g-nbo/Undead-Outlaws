import pygame
import enemies
import buttons
import random
import time
import fonts
import images
import sounds

print("hello world!")

pygame.init()

# Create screen
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.6)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Undead Outlaws")

x = 200
y = 200
scale = 0.7

characterSprite = pygame.transform.scale(images.characterSprite, (images.characterSprite.get_width() * scale, images.characterSprite.get_height() * scale))

charRect = characterSprite.get_rect()
charRect.center = (0 + 90, SCREEN_HEIGHT - 100)

playerHealth = 5

zomb1 = enemies.Enemy(SCREEN_WIDTH - 70, SCREEN_HEIGHT - 140, "zombie", 0.5, images.dgSprite)
enemyArr = [zomb1]

# level vars
level = 1
enemyCount = 0
waited = False

# create timers/delay
start = time.time()

play_button = buttons.Button(610, 300, images.play_img, 1)
quit_button = buttons.Button(605, 530, images.quit_img, 1)
instructions_button = buttons.Button(600, 415, images.instruct_img, 1)
gameover_button = buttons.Button(600, 480, images.gameoverquit_img, 4)

# menu state for switching menus
menu_state = "main"

# Needed these out of main game loop for menu
keys = pygame.key.get_pressed()
mouse_pos = pygame.mouse.get_pos()

# Time
clock = pygame.time.Clock()

bg = images.bg

# Create basic game loop
run = True
while run:
    if menu_state == "main":
        screen.blit(images.menu_full, (0, 0))
        if quit_button.draw(screen):
            run = False
        if instructions_button.draw(screen):
            images.menu_full = pygame.transform.scale(images.menu_full, (0, 0))

            screen.blit(fonts.instructText5, (50, 250))

            screen.blit(fonts.instructText, (50, 330))
            screen.blit(fonts.instructText2, (50, 380))

            screen.blit(fonts.instructText3, (50, 450))
            screen.blit(fonts.instructText4, (50, 500))

        if play_button.draw(screen):
            while run:
                clock.tick(60)
                pygame.display.update()
                # change things like background depending on level using switch statement
                match level:
                    case 1:
                        bg = pygame.image.load("../images/level1_bg.jpg")
                        bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        images.levelText = pygame.image.load("../images/level1_real.png")
                        images.levelText = pygame.transform.scale(images.levelText, (800, 450))
                    case 2:
                        bg = pygame.image.load("../images/level2_bg.jpg")
                        bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        images.levelText = pygame.image.load("../images/level2.png")
                        images.levelText = pygame.transform.scale(images.levelText, (800, 450))
                    case 3:
                        bg = pygame.image.load("../images/level3_bg.png")
                        bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        images.levelText = pygame.image.load("../images/level3.png")
                        images.levelText = pygame.transform.scale(images.levelText, (800, 450))
                    case 4:
                        bg = pygame.image.load("../images/level4_bg.png")
                        bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        images.levelText = pygame.image.load("../images/level4.png")
                        images.levelText = pygame.transform.scale(images.levelText, (800, 450))
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
                screen.blit(hearts, images.heartsRect)

                keys = pygame.key.get_pressed()
                mouse_pos = pygame.mouse.get_pos()

                # levelText = gameFont.render(f"Level: {level}", None, (255, 255, 255))
                healthText = fonts.gameFont.render(f"Health: {playerHealth}", None, (255, 255, 255))

                screen.blit(images.levelText, images.levelText_rect)
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

                            sounds.shootSound.set_volume(0.2)
                            sounds.shootSound.play()

                        if enemyArr[i].health <= 0:
                            enemyArr[i].canHit = False
                            enemyArr[i].rect = enemyArr[i].rect.move(-5000, -5000)


                for i in range(len(enemyArr)):
                    dgZomb = enemies.Enemy(SCREEN_WIDTH - 70, SCREEN_HEIGHT - 140, "zombie", 0.5, images.dgSprite)
                    lgZomb = enemies.Enemy(SCREEN_WIDTH - 70, SCREEN_HEIGHT - 140, "zombie", 0.5, images.lgSprite)
                    redZomb = enemies.Enemy(SCREEN_WIDTH - 70, SCREEN_HEIGHT - 140, "zombie", 0.5, images.redSprite)
                    purpZomb = enemies.Enemy(SCREEN_WIDTH - 70, SCREEN_HEIGHT - 140, "zombie", 0.5, images.purpleSprite)



                    screen.blit(enemyArr[i].image, enemyArr[i].rect)
                    enemyArr[i].rect = enemyArr[i].rect.move(-(level * 4), 0)

                    if charRect.colliderect(enemyArr[i].rect) and playerHealth > 1 and enemyArr[i].canHit:

                        sounds.biteSound.set_volume(0.5)
                        sounds.biteSound.play()
                        playerHealth -= 1
                        enemyArr[i].canHit = False
                        print("player health:", playerHealth)
                    elif charRect.colliderect(enemyArr[i].rect) and enemyArr[i].canHit and playerHealth == 1 and level != 5:
                        playerHealth -= 1
                        sounds.biteSound.play()
                        print("player dead")

                    if random.randint(1, 350) == 350 and enemyCount != (level * 3):
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

                    if enemyCount == (level * 3) and not waited:
                        start = time.time()
                        waited = True

                    if enemyCount == (level * 3) and time.time() - start > 4 and waited and level <= 4:
                        print("waited 3 seconds, next level")
                        enemyCount = 0
                        level += 1
                        start = time.time()
                        waited = False

                    if playerHealth == 0 and level != 5:
                        sounds.biteSound.set_volume(0)
                        sounds.shootSound.set_volume(0)
                        screen.fill("black")
                        game_overText = fonts.game_overFont.render("GAME OVER", 1, (255, 0, 0))
                        screen.blit(game_overText, (180, 130))
                        if gameover_button.draw(screen):
                            run = False
                        pygame.display.update()

                    if level == 5:
                        sounds.biteSound.set_volume(0)
                        sounds.shootSound.set_volume(0)
                        screen.fill("black")
                        game_overText = fonts.game_overFont.render("YOU WIN", 1, (0, 255, 0))
                        screen.blit(game_overText, (280, 130))
                        if gameover_button.draw(screen):
                            run = False
                        pygame.display.update()
                        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_ESCAPE]:
            run = False
    pygame.display.update()

    # Slow the game to update 60 times per second
    clock.tick(60)

pygame.quit()
