# 3D Grid Visualisation

A wrapper for Panda3D to visualise 2D grids 

## Installation

```
pip install grid_vis
```


## Usage

```python
from gird_vis import run_grid

def update(grid):
    return [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
]

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

run_grid(grid, update_func=update, tick_rate=1)
```
