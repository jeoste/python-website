class Coordinate:
    def __init__(self, x, y):
        # definition of the constructor
        self.x = x
        self.y = y


point = Coordinate(10, 20)
# override if call after the constructor
point.x = 11
print('x:', point.x)
print('y:', point.y)
