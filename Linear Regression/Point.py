class Point:
    def __init__(self, X:float, Y:float):
        self.X = X
        self.Y = Y


class PointND:
    def __init__(self, coordinates:list[float]=[1,1]):
        self.coordinates = coordinates