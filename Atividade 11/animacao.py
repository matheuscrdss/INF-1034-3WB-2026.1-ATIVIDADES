import pygame, sys
from pygame.locals import QUIT

pygame.init()

window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Animação')
clock = pygame.time.Clock()
running = True

hero_img = pygame.image.load("Atividade 11/megaman_spritesheet.png")

while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    window.fill("white")

    pygame.draw.rect(window, (0, 153, 0), (0, 550, 1280, 300))


    pygame.display.update()

    clock.tick(60)