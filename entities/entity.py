import pygame


class Entity:
    def __init__(self, screen_width, screen_height, width, height):
        self.screen_width, self.screen_height = screen_width, screen_height
        self.width = width
        self.height = height
        self.color = (0, 255, 255)
        self.posX = 0
        self.posY = 0
        self.velocity = 5
        self.rect = None

    def get_info(self):
        return self.posX, self.posY, self.width, self.height

    def moveX(self, delta):
        if not self.posX + self.width + delta > self.screen_width and not self.posX + delta < 0:
            self.posX += delta

    def moveY(self, delta):
        if not self.posY + self.height + delta > self.screen_height and not self.posY + delta < 0:
            self.posY += delta

    def draw(self, window):
        self.rect = pygame.draw.rect(window, self.color, self.get_info())
