from panda3d.core import Point3
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import LVector3, LVector4
from panda3d.core import DirectionalLight
from panda3d.core import CullFaceAttrib, AntialiasAttrib
import numpy as np
import random
import math

class VoxelGrid(ShowBase):
    def __init__(self, numpy_grid, tick_rate):
        super().__init__()

        self.update_func: function

        self.done = False
        self.tick_rate = tick_rate
        self.tick = self.tick_rate
        self.ticked = False
        self.grid2d = numpy_grid

        self.cam_pos = Point3(0, 0, 0)

        self.render.setShaderAuto()  # Enable shaders
        
        # Set up camera
        self.camLens.setNearFar(1, 500)

        # Set up lighting
        self.setup_lighting()

        # Create the voxel grid
        self.create_voxel_grid(self.grid2d)
        self.create_floor()

        # Update the scene at a consistent frame rate
        self.taskMgr.add(self.spin_camera, "spin_camera_task")
        self.taskMgr.add(self.update_empty, "update_grid_task")
        self.taskMgr.add(self.tick_frame, "tick_frame_task")

        self.render.setDepthTest(True)
        self.render.setDepthWrite(True)

    def update_empty(self, task):
        if self.ticked:
            self.grid2d = np.array(self.update_func(self.grid2d))
            self.update_grid()
            self.update_floor()
            self.spin_camera(task)
        return Task.cont
    
    def update_grid(self):
        for node in self.render.findAllMatches("=type=GridCube"):
            node.removeNode()
        self.create_voxel_grid(self.grid2d)

    def update_floor(self):
        floor = self.render.find("=type=Floor")
        floor.setSx(self.grid2d.shape[0] + 2)
        floor.setSy((self.grid2d.shape[1] + 2))
        floor.setPos(Point3(self.grid2d.shape[0]/2 - 1, self.grid2d.shape[1]/2 - 1, -1))

    def tick_frame(self, task):
        order = math.floor(math.log(self.tick_rate, 10))
        if self.tick == round(task.time, -order):
            self.tick = round(task.time + self.tick_rate, -order)
            self.ticked = True
        else:
            self.ticked = False
            self.tick == round(task.time + 0.1, 1)
        return Task.cont

    def setup_lighting(self):
        # self.light = self.render.attachNewNode(Spotlight("Spot"))
        self.light = self.render.attachNewNode(DirectionalLight("DirectionalLights"))
        self.light.node().setDirection(LVector3(-1, -0.5, -1))
        self.light.node().setScene(self.render)
        self.light.node().setColor(LVector4(0.7, 0.7, 0.7, 1))
        self.light.node().setShadowCaster(True)
        self.render.setLight(self.light)

        self.light2 = self.render.attachNewNode(DirectionalLight("DirectionalLights"))
        self.light2.node().setDirection(LVector3(1, 1, -1))
        self.light2.node().setScene(self.render)
        self.light2.node().setColor(LVector4(0.5, 0.5, 0.5, 1))
        self.light2.node().setShadowCaster(True)
        self.render.setLight(self.light2)

        # Important! Enable the shader generator.
        self.render.setShaderAuto()

    def create_floor(self):
        voxel = self.loader.loadModel("models/box")
        voxel.setTag("type", "Floor")
        voxel.setSx(self.grid2d.shape[0] + 2)
        voxel.setSy((self.grid2d.shape[1] + 2))
        voxel.setPos(Point3(self.grid2d.shape[0]/2 - 1, self.grid2d.shape[1]/2 - 1, -1))
        colour = (0.647, 0.509, 0.444)
        voxel.setColor(*colour, 1)

        voxel.setAttrib(CullFaceAttrib.make(CullFaceAttrib.MCullNone))
        
        voxel.reparentTo(self.render)

    def create_voxel_grid(self, grid):
        """Creates a grid of small cubes."""
        width, depth = grid.shape
        for x in range(width):
            for y in range(depth):
                if self.grid2d[x][y] == 1:
                    self.create_voxel(x, y, 0)

    def create_voxel(self, x, y, z):
        """Creates a single voxel cube at a given position."""
        voxel = self.loader.loadModel("models/box")
        # voxel.setTwoSided(True)
        voxel.setTag("type", "GridCube")

        size = 1.0
        voxel.setPos(Point3(x - size/2, y - size/2, z))
        voxel.setScale(size)  # Smaller size for visibility in a large grid

        colours = [(0.8, 0.84, 0.68), (0.91, 0.93, 0.79), (1.0, 0.98, 0.88), (0.98, 0.93, 0.8)]
        colour = random.choice(colours)
        voxel.setColor(*colour, 1)

        voxel.setAttrib(AntialiasAttrib.make(AntialiasAttrib.M_line))
        voxel.setAttrib(CullFaceAttrib.make(CullFaceAttrib.MCullNone))

        # voxel.setShaderAuto()
        voxel.reparentTo(self.render)

    def spin_camera(self, task):
        """Rotate camera around the grid."""
        angleDegrees = task.time * 0.3
        angleRadians = angleDegrees * (3.14159 / 180.0)
        centre = (self.grid2d.shape[0]/2, self.grid2d.shape[1]/2)
        distance = 5 + 2 * max(self.grid2d.shape[0], self.grid2d.shape[1])
        self.cam_pos = LVector3(centre[0] + math.sin(angleRadians)*distance, -centre[1] + math.cos(angleRadians)*distance, 25)

        self.camera.setPos(self.cam_pos)
        self.camera.lookAt(*centre, 0)
        return Task.cont
