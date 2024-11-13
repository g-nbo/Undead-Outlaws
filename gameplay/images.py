import pygame

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.6)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

characterSprite = pygame.image.load("../images/player_2.png")

hearts = pygame.image.load("../images/hearts_5.png")
heartsRect = hearts.get_rect()
# heartsRect.center = (220, SCREEN_HEIGHT // 10)
heartsRect.center = (SCREEN_WIDTH - 210, SCREEN_HEIGHT // 10)

# Create enemy
dgSprite = pygame.image.load("../images/dgZomb.png")
lgSprite = pygame.image.load("../images/lgZomb.png")
redSprite = pygame.image.load("../images/redZomb.png")
purpleSprite = pygame.image.load("../images/purpZomb.png")

levelText = pygame.image.load("../images/level1_real.png")
levelText = pygame.transform.scale(levelText, (800, 450))
levelText_rect = levelText.get_rect()
# levelText_rect.center = (SCREEN_WIDTH - 170, SCREEN_HEIGHT // 12)
levelText_rect.center = (140, SCREEN_HEIGHT // 12)

# backgrounds
bg = pygame.image.load("../images/level1_bg.jpg")
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

# buttons for menus
play_img = pygame.image.load("../images/playbutton.png").convert_alpha()
quit_img = pygame.image.load("../images/quitbutton.png").convert_alpha()
instruct_img = pygame.image.load("../images/instructionsbutton.png").convert_alpha()
gameoverquit_img = pygame.image.load("../images/gameoverquit.png").convert_alpha()

menu_full = pygame.image.load("../images/menuimage.png").convert_alpha()
menu_full = pygame.transform.scale(menu_full, (SCREEN_WIDTH, SCREEN_HEIGHT))

win_img = pygame.image.load("../images/winimage.png")
win_img = pygame.transform.scale(win_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
lose_img = pygame.image.load("../images/loseimage.png")
lose_img = pygame.transform.scale(lose_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
