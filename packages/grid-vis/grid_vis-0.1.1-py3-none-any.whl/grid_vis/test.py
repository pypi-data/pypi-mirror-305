from gird_vis import run_grid

import random as rn
import numpy as np

def update(grid):
    height = rn.randint(0, 20)
    width = rn.randint(0, 20)
    return np.ones((height, width))

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

run_grid(grid, update_func=update, tick_rate=1)
