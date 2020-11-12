import sys
import pygame

screen = pygame.display.set_mode((1080,720))
screen_rect = screen.get_rect()
image = pygame.image.load("tree-2.bmp")
rect = image.get_rect()
while True:
    screen.fill((100, 0, 230))
    rect.midbottom = screen_rect.midbottom
    screen.blit(image, rect)

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()