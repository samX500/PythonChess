class move:
    position = None
    color = None

    def __init__(self, positon, color):
        self.positon = positon
        self.color = color

    def getPosition(self):
        return self.positon

    def setPosition(self, position):
        self.positon = position

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def __str__(self):
        return self.color + ' ' + self.position
