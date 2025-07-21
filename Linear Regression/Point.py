class Point:
    def __init__(self, X:float, Y:float):
        self.X = X
        self.Y = Y


class PointND:
    def __init__(self, coordinates:list[float]):
        self.coordinates = coordinates