import matplotlib.pyplot as plt
import numpy as np

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
    
class StraightND:
    def __init__(self, m:list[float] = [1], b:float=1):
        pass