import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.6)

pygame.init()

gameFont = pygame.font.SysFont('segoeprint', 64)
game_overFont = pygame.font.SysFont(None, 200)

textfont = pygame.font.SysFont(None, 60)
instructText = textfont.render("A and D to move", 1, (255, 255, 255))
instructText2 = textfont.render("left and right", 1, (255, 255, 255))
instructText3 = textfont.render("Click on zombies", 1, (255, 255, 255))
instructText4 = textfont.render("to kill them", 1, (255, 255, 255))
instructText5 = textfont.render("You get 5 lives", 1, (255, 255, 255))
