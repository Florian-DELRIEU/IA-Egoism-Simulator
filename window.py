import pygame as pygame
pygame.init()

ecran = pygame.display.set_mode((1200, 800))

continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False

pygame.quit()