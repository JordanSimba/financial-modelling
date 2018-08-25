import numpy as np

class direction_space:

    def __init__(self):
        self.origin = np.array([0,0])
        self.x_unit = np.array([1,0])
        self.y_unit = np.array([0,1])
        self.dim = 2
