import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.Surface((160, 40))
        self.image.fill('yellow')
        self.rect = self.image.get_rect(midtop=pos)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.speed = 800

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            if self.pos.x <= WINDOW_WIDTH - self.rect.width:
                self.direction.x = 1
            else:
                self.direction.x = 0
        elif keys[pygame.K_LEFT]:
            if self.pos.x > 0:
                self.direction.x = -1
            else:
                self.direction.x = 0
        else:
            self.direction.x = 0

    def move(self, dt):
        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)

        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = round(self.pos.y)

    def update(self, dt):
        self.input()
        self.move(dt)
