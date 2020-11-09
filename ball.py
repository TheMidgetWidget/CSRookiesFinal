from entity import Entity
import pygame
import random


class Ball(Entity):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, 8, 8)
        self.color = (255, 255, 255)
        self.posX = (screen_width - self.width) // 2
        self.posY = int(screen_height * 0.8) - self.height * 8
        coeff = 1 if random.random() < 0.5 else -1
        self.velX = random.randint(250, 301) / 100 * coeff
        self.velY = -3
        self.can_collide = True

    def check_collision(self, blocks):
        for block in blocks:
            if block.rect is not None and self.rect is not None and self.rect.colliderect(block.rect):
                self.velY *= -1
                blocks.remove(block)
                self.can_collide = True

    def check_player_collision(self, player):
        if player.rect is not None and self.rect is not None and self.rect.colliderect(
                player.rect) and self.can_collide:
            self.velY *= -1
            if self.rect.collidepoint(player.rect.topleft) or self.rect.collidepoint(
                    player.rect.topright) or self.rect.collidepoint(player.rect.midleft) or self.rect.collidepoint(
                player.rect.midright):
                self.velX *= -1
            self.can_collide = False

    def move(self, player):
        self.check_player_collision(player)
        self.posX, self.velX = self._move(self.posX, self.velX, self.width, self.screen_width, False)
        self.posY, self.velY = self._move(self.posY, self.velY, self.height, self.screen_height, True)
        return self.posY == -1

    def _move(self, pos, vel, ball_dim, scrn_dim, check):
        pos += vel
        if pos < ball_dim:
            pos, vel = ball_dim, -vel
            if check:
                self.can_collide = True
        if pos > scrn_dim - ball_dim:
            if check:
                pos, vel = -1, -1
            else:
                pos, vel = pos - ball_dim, -vel
        return pos, vel
