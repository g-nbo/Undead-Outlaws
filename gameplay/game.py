import pygame
print("hello world!")

pygame.init()

# Create screen

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Undead Outlaws")

# Create initial character

x = 200
y = 200
scale = 0.5

img = pygame.image.load("../images/test-sprite-game.png")
img = pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))

rect = img.get_rect()
rect.center = (x, y)



# Create basic game loop

run = True
while run:

    screen.blit(img, rect)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

