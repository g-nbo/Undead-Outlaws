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


