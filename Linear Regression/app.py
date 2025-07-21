from Point import Point 
from Straight import Straight
from Drawer import Drawer

def simple_regression(point_a:Point, point_b:Point):
    reg_straight = Straight()
    reg_straight.m = (point_a.Y - point_b.Y) / (point_a.X - point_b.X)
    reg_straight.b = point_a.Y - (point_a.X * reg_straight.m)
    print(reg_straight)
    Drawer().print(reg_straight, [point_a, point_b])

def regression(points:list[Point]):
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


print("1 - 2D 2 points")
print("2 - 2D 5 points")
choice = int(input("Enter Choice -> "))

match choice:
    case 1:
        x_a = float(input("X-Coordinate of point A -> "))
        y_a = float(input("Y-Coordinate of point A -> "))
        x_b = float(input("X-Coordinate of point B -> "))
        y_b = float(input("Y-Coordinate of point B -> "))
        simple_regression(Point(x_a, y_a), Point(x_b, y_b))
    case 2:
        points = []
        for i in range(5):
            points.append(Point(
                float(input(f"X-Coordinate of point {i+1} -> ")),
                float(input(f"Y-Coordinate of point {i+1} -> ")))
            )
        regression(points)
        pass
    case 4:
        pass
    case 5:
        pass
    case 6:
        pass
    case _:
        pass


    