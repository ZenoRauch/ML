import matplotlib.pyplot as plt
import numpy as np
from Point import Point 
from Straight import Straight
from Util import Util

# Supported by Claude.ai
class Drawer:
    def __init__(self, figsize=(5, 5)):
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