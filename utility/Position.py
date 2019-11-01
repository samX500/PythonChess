class Position:

    x = 0
    y = 0

    def __init__(self,x,y):
        self,x = x
        self.y = y

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def __str__(self):
        return 'X:' + self.x +' Y:' + self.y