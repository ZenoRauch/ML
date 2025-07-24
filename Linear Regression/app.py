from Point import Point, PointND
from Straight import Straight, StraightND
from Drawer import Drawer

def simple_regression_2d(point_a:Point, point_b:Point):
    reg_straight = Straight()
    reg_straight.m = (point_a.Y - point_b.Y) / (point_a.X - point_b.X)
    reg_straight.b = point_a.Y - (point_a.X * reg_straight.m)
    print(reg_straight)
    Drawer().print(reg_straight, [point_a, point_b])

def regression_2d(points:list[Point]):
    straight = Straight()
    x_total = 0
    y_total = 0 
    for point in points:
        x_total += point.X
        y_total += point.Y
    _x = x_total / len(points)
    _y = y_total / len(points)
    s_xy = 0
    s_xx = 0
    for point in points:
        s_xy += (point.X - _x)*(point.Y - _y)
        s_xx += (point.X - _x)*(point.X - _x)
    straight.m = s_xy/s_xx
    straight.b = _y - (_x * straight.m)
    print(straight)
    Drawer().print(straight, points)


def getSums(points:list[PointND]) -> list:
    dimensions = len(points[0].coordinates)
    variables_sums = []
    first = True
    # Calcualting n maxes
    for point in points:
        if first: 
            for i in range(dimensions):
                variables_sums.append(point.coordinates[i])
            first = False
        else:
            for i in range(dimensions):
                variables_sums[i] += point.coordinates[i]
    return variables_sums

def getSquaredSums(sums:list[float]) -> list:
    """
    Calculating sum of squares
    [
          x1        x2        x3        ...   xn
    x1   [x1 * x1] [x1 * x2] [x1 * x3] [...] [x1 * xn]
    x2   [x2 * x1] [x2 * x2] [x2 * x3] [...] [x2 * xn]
    x3   [x3 * x1] [x3 * x2] [x3 * x3] [...] [x3 * xn]
    ...  [...]     [...]     [...]     [...] [...]
    xn   [xn * x1] [xn * x2] [xn * x3] [...] [xn * xn]
    ]
    """
    returnlist = []
    for i in range(len(sums)):
        if i == 0:
            for y in range(len(sums)):
                returnlist.append([sums[i]*sums[y]])
        else:
            for y in range(len(sums)):
                returnlist[y].append(sums[i]*sums[y])
    return returnlist

def regression(points:list[PointND]):
    straight = StraightND()
    n = len(points)
    dimensions = len(points[0].coordinates)
    variables_sums = getSums(points)
    print(variables_sums)
    variables_squaresums = getSquaredSums(variables_sums)
    print(variables_squaresums)

    

print("1 - 2D 2 points")
print("2 - 2D 5 points")
print("3 - 3D 10 points")
choice = int(input("Enter Choice -> "))

match choice:
    case 1:
        x_a = float(input("X-Coordinate of point A -> "))
        y_a = float(input("Y-Coordinate of point A -> "))
        x_b = float(input("X-Coordinate of point B -> "))
        y_b = float(input("Y-Coordinate of point B -> "))
        simple_regression_2d(Point(x_a, y_a), Point(x_b, y_b))
    case 2:
        points = []
        for i in range(5):
            points.append(Point(
                float(input(f"X-Coordinate of point {i+1} -> ")),
                float(input(f"Y-Coordinate of point {i+1} -> ")))
            )
        regression_2d(points)
        pass
    case 3:
        points = [
            PointND([1, 1, 10]),
            PointND([2, 0, 9]),
            PointND([0, 2, 11]),
            PointND([3, 1, 14]),
            PointND([4, 2, 19]),
            PointND([5, 0, 15]),
            PointND([1, 3, 16]),
            PointND([2, 2, 15]),
            PointND([6, 1, 20]),
            PointND([0, 0, 5]),
        ]
        regression(points)
        pass
    case 5:
        pass
    case 6:
        pass
    case _:
        pass


    