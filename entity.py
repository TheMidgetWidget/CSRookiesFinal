class Entity:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = (0, 0, 255)
        self.posX = 0
        self.posY = 0

    def get_info(self):
        return self.posX, self.posY, self.width, self.height
