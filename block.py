from entity import Entity


class Block(Entity):
    def __init__(self, screen_width, screen_height, width, height, posX, posY):
        super().__init__(screen_width, screen_height, width, height)
        self.posX = posX
        self.posY = posY
