# Linear Regression

With linear regression, we are able to calculate a value on the Y-axis based on the input on the X-axis. The functional curve of this mathematical operation is a straight with the formula `m * X + b = Y`. Based on some data, in our case trainingdata, the parameters m and b are adjusted to pass through the data cloud with the minimum error.

## 2D 2 Points

To find the best fitting straight for to points is pretty straight forward:
- Calculate Delta between two points `m = (point_a.Y - point_b.Y) / (point_a.X - point_b.X)` to get gradient m
- insert values of either point a or b in equation `m * X + b = Y` with the new infromation m
- transform equation by subtracting `m * X` to receive `b = point_a.Y - (point_a.X * m)`

<img src='pictures/simple_twopoint_regression.png' alt='simple regression' style='width:400px;'>

In this bit, I started by using the classes `Point` and `straight`:
```Python
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
```

With the following function, the necessary data gets calculated and printed using matplotlib:
```Python
def simple_regression(point_a:Point, point_b:Point):
    reg_straight = Straight()
    # Calculating Slope
    reg_straight.m = (point_a.Y - point_b.Y) / (point_a.X - point_b.X)
    # Inserting Values from Point A into function to calculate b
    reg_straight.b = point_a.Y - (point_a.X * reg_straight.m)
    # Possibility to extend is to insert Values from Point B into function and check, if b is still the same
    print(reg_straight)
    Drawer().print(reg_straight, [point_a, point_b])
```

## 2D Multiple Points

The formula stays (nearly) the same for calculating the straight with multiple points.
- Calculate average x an y for all points
- Calcualte the sum of cross-products and sum of squared deviations from the mean. In this step, the difference from the averge point to the rest of the points gets calculated. Dividing these numbers results in the slope m.
- Inserting m, average x and average y in to the formula `b = Y - (X * m)`

<img src='pictures/fivepoint_regression.png' alt='5 point regression' style='width:400px;'>

The classes stayed the same, however the function needed adjustments:
```Python
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
```

## 3d Multiple Points

For this part, I needed to consult ChatGPT and Calude.ai due to me not properly understanding, how to calculate a multidimensional regression. On the top level, we work with vectors. I still need to understand the math behind calculating and scaling the following methods:

```Python
# Input in form of vectors
[
    [x1, z1, y1],
    [x2, z2, y2],
    [x3, z3, y3],
    [x4, z4, y4]
]
# Achiveable information in form of a vector
[
    m1,
    m2,
    b
]
# Final equation
# the number 1 on first_array[2] is for the y-intercept b => 1*b equals b
[x1, z1, 1] * [m1, m2, b] = y1
```
I thought, that I simple can use the concept of using Delta Y over Delta X. However, I can use the principle of squares of sum from the 2-dimensional regression. Therefore I started with the matrix to calculate all sum of squares to ... to ... to do what? Because someone told me that? At the moment, I still don't understand the math quite yet, but I am working on it.

## n-D Multiple Points - Final Form

# Code
I created