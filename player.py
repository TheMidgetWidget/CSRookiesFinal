from entity import Entity


class Player(Entity):
    def __init__(self, screen_width, screen_height):
        width, height = 80, 10
        super().__init__(width, height)
        self.posX = (screen_width - width) // 2
        self.posY = int(screen_height * 0.8)
