import sys
import pygame

screen = pygame.display.set_mode((1080, 720))

while True:
    screen.fill((0, 0, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    pygame.display.flip()