import pygame
import sys
from settings import *
from player import Player


class Main:
    def __init__(self):
        super().__init__()

        # Init Pygame
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Shoot')
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()

        self.player = Player((WINDOW_WIDTH / 2, WINDOW_HEIGHT - 100), self.all_sprites)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # frame rate limit
            dt = self.clock.tick() / 1000

            self.display_surface.fill((249, 131, 103))

            self.all_sprites.update(dt)

            self.all_sprites.draw(self.display_surface)

            pygame.display.update()


if __name__ == '__main__':
    shooter = Main()
    shooter.run()
