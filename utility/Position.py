class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def as_tuple(self):
        return self.x,self.y

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

    def __lt__(self, other):
        if self.x < other.x:
            return True
        if self.x == other.x and self.y < other.y:
            return True
        return False

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x,self.y))

    def clone(self):
        return Position(self.get_x(), self.get_y())

    def __str__(self):
        return f'X: {self.x}  Y: {self.y}'
