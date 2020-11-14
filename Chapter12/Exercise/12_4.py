import sys
import pygame

class Tree:
    def __init__(self):
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.color = (230, 0, 90)
        self.image = pygame.image.load('tree-2.bmp')
        self.image_rect = self.image.get_rect()
        self.move_DOWN = False
        self.move_LEFT = False
        self.move_RIGHT = False
        self.move_UP = False
        
    def _move_bool(self, move_bool):
        if self.event.key == pygame.K_LEFT:
            self.move_LEFT = move_bool
        if self.event.key == pygame.K_RIGHT:
            self.move_RIGHT = move_bool 
        if self.event.key == pygame.K_UP:
            self.move_UP = move_bool
        if self.event.key == pygame.K_DOWN:
            self.move_DOWN = move_bool
            
    def _move(self):
        if self.move_DOWN and self.image_rect.bottom < self.screen_rect.bottom:
            self.image_rect.y += 1
        if self.move_UP and self.image_rect.top > self.screen_rect.top:
            self.image_rect.y -= 1
        if self.move_LEFT and self.image_rect.left > self.screen_rect.left:
            self.image_rect.x -= 1
        if self.move_RIGHT and self.image_rect.right < self.screen_rect.right:
            self.image_rect.x += 1
    def main(self):
        self.image_rect.center = self.screen_rect.center

        while True:
            self.screen.fill(self.color)
            self.screen.blit(self.image, self.image_rect)
            
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    sys.exit()
                elif self.event.type == pygame.KEYDOWN:
                    print(self.event.key)
                    if self.event.key == pygame.K_q:
                        sys.exit()
                    else:
                        self._move_bool(True)
                elif self.event.type == pygame.KEYUP:
                    self._move_bool(False)
            self._move()    
            
            pygame.display.flip()
            
if __name__ == '__main__':
    ai_game = Tree()
    ai_game.main()