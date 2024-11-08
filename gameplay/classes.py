import pygame

class Enemy:
    def __init__(self, x, y, type, scale, sprite):


        if type == "zombie":

            self.sprite = sprite
            self.image = pygame.transform.scale(self.sprite, (self.sprite.get_width() * scale, self.sprite.get_height() * scale))
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

            self.health = 1
            self.canHit = True
            self.alive = self.health > 0


class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
