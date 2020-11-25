import pygame
import sys

def main():
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    screen.fill((100,0,100))
    screen_rect = screen.get_rect()
    image = pygame.image.load('tree-2.bmp')
    image_rect = image.get_rect()
    image_width, image_height = image_rect.size
    screen_width, screen_height = screen_rect.size
    
    
    while True:
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                   
if __name__ == '__main__':
    main()