class Movement:

    def __init__(self, direction, length):
        self.direction = direction
        self.length = length

    def get_length(self):
        return self.length

    def get_direction(self):
        return self.direction.value.copy()

    def __str__(self):
        return f'{self.direction}  {self.length}'
