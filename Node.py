from dataclasses import dataclass
# from typing import Union
import numpy as np

class Node:

    def __init__(self, xy: tuple, f: float = np.Inf, g: float = np.Inf, h: float = np.Inf):

        self.xy  = xy
        self.g  = g
        self.h  = h 
        self.closed = False
        self.camefrom = None

    # def same(self, node):
    #     return True if (self.x == node.x and self.y == node.y) else False
    
    # Equals functionality     
    def __eq__(self, node):
        x1, y1  = self.xy
        x2, y2  = node.xy
        return x1 == x2 and y1 == y2
    
    # Hash functionality
    def __hash__(self):
        x, y  = self.xy
        return hash((x, y)) 
    
    # Get f score (g+h)
    def get_score(self):
        return self.g + self.h

    # Determine neighbors
    def neighbors(self, grid):

        # Shape of grid
        rows = len(grid)
        cols = len(grid[0])

        # Empty list of neighbors to be filled
        neighbors = []

        # Get position
        xc, yc = self.xy

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1,-1), (-1, 1), (1, 1), (1, -1)] 
        for x, y in dirs: 
            new_x, new_y = xc + x, yc + y
            if new_x in range(rows) and new_y in range(cols):
                # new_node = Node( (new_x, new_y) )    
                neighbors.append((new_x, new_y))

        return neighbors
    
    def dist(self, node):

        x1, y1  = self.xy
        x2, y2  = node.xy
         
        # Euclidean distance to include diagonals
        return np.sqrt( (x2 - x1)**2 +  (y2 - y1)**2  )

