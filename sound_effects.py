import pygame

pygame.mixer.init()

# sounds for various tasks
bullet_sound = pygame.mixer.Sound('sounds/laser.wav')
alien_sound = pygame.mixer.Sound('sounds/explosion.wav')
level_up_sound = pygame.mixer.Sound('sounds/levlup.mp3')
collision_sound = pygame.mixer.Sound('sounds/crash.mp3')
intro_sound = pygame.mixer.Sound('sounds/intro.mp3')