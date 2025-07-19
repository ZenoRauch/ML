import matplotlib.pyplot as plt
import numpy as np


class Point:
    def __init__(self, X:float, Y:float):
        self.X = X
        self.Y = Y


class Straight:
    def __init__(self, m:float=1, b:float=0):
        self.m = m
        self.b = b

    def draw(self, ax, x_range=(-10, 10)):
        x = np.linspace(x_range[0], x_range[1], 100)
        y = self.m * x + self.b
        ax.plot(x, y, 'b-', linewidth=2, label=f'y = {self.m}x + {self.b}')


    def __str__(self):
        return f"m = {self.m}, b = {self.b}"

class Util:
    def find_range(self, points:list[Point]):
        min_x = 0
        max_x = 0
        min_y = 0 
        max_y = 0
        for point in points:
            if point.X < min_x : min_x = point.X
            if point.X > max_x : max_x = point.X
            if point.Y < min_y : min_y = point.Y
            if point.Y > max_y : max_y = point.Y
        return (min_x*1.1, max_x*1.1), (min_y*1.1, max_y*1.1)

# Supported by Claude.ai
class Drawer:
    def __init__(self, figsize=(10, 8)):
        self.figsize = figsize

    def print(self, straight:Straight, points:list[Point]):
        x_range, y_range = Util().find_range(points)
        fig, ax = plt.subplots(figsize=self.figsize)
        
        # Set up the grid
        ax.grid(True, alpha=0.3)
        ax.set_xlim(x_range)
        ax.set_ylim(y_range)
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.axvline(x=0, color='k', linewidth=0.5)
        
        # Draw the straight line
        straight.draw(ax, x_range)
        
        # Draw the points
        if points:
            x_coords = [point.X for point in points]
            y_coords = [point.Y for point in points]
            ax.scatter(x_coords, y_coords, color='red', s=50, zorder=5, label='Points')
            
            # Optionally annotate points with coordinates
            for i, point in enumerate(points):
                ax.annotate(f'({point.X}, {point.Y})', 
                           (point.X, point.Y), 
                           xytext=(5, 5), 
                           textcoords='offset points',
                           fontsize=8)
        
        # Labels and legend
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Grid with Line and Points')
        ax.legend()
        
        plt.tight_layout()
        plt.show()

def simple_regression(point_a:Point, point_b:Point):
    reg_straight = Straight()
    reg_straight.m = (point_a.Y - point_b.Y) / (point_a.X - point_b.X)
    reg_straight.b = point_a.Y - (point_a.X * reg_straight.m)
    print(reg_straight)
    Drawer().print(reg_straight, [point_a, point_b])

print("1 - 2 points")
print("2 - 3 points")
print("3 - 4 points")
print("4 - file with 20 points")
print("5 - file with 50 points")
print("6 - file with 250 points")
choice = int(input("Enter Choice -> "))

match choice:
    case 1:
        """
        x_a = float(input("X-Coordinate of point A -> "))
        y_a = float(input("Y-Coordinate of point A -> "))
        x_b = float(input("X-Coordinate of point B -> "))
        y_b = float(input("Y-Coordinate of point B -> "))
        simple_regression(Point(x_a, y_a), Point(x_b, y_b))
        """
        simple_regression(Point(-2, 4), Point(8, -1))
    case 2:
        pass
    case 3:
        pass
    case 4:
        pass
    case 5:
        pass
    case 6:
        pass
    case _:
        pass


    