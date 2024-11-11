import pygame

# initialize music
pygame.mixer.init()
menuMusic = pygame.mixer.Sound("../sounds/intense-horror-music-01-14890.mp3")
menuMusic.set_volume(0.6)

gameMusic = pygame.mixer.Sound("../sounds/horror_music_clipped.mp3")
gameMusic.play()
# menuMusic.play()

biteSound = pygame.mixer.Sound("../sounds/zombie-bite-96528.mp3")
shootSound = pygame.mixer.Sound("../sounds/shoot-1-81135.mp3")