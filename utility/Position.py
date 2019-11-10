class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def add(self, x, y):
        self.x += x
        self.y += y

    def __str__(self):
        return f'X: {self.x}  Y: {self.y}'
