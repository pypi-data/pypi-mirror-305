from vis import VoxelGrid
import numpy as np

def blank(grid):
    pass

def run_grid(npgrid, update_func=blank, tick_rate=0.1):
    npgrid = np.array(npgrid)
    app = VoxelGrid(npgrid, tick_rate)
    app.update_func = update_func
    app.run()
