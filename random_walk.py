import numpy as np
import random as rand
import direction_space as ds

# step size
walk_step = 1.0
# range
start_time = 1
stop_time = 1000
# sample size
samples = 1000

# direction vectors
# 2 dimensions
space = ds.direction_space()
dim = space.dim

origin, x_hat, y_hat = space.origin, space.x_unit, space.y_unit

print "x_unit:", x_hat
print "y_unit:", y_hat
print "origin:", origin
print "dimension:", dim

# init sequence array
rand_walk_sequence = [origin] # start from origin

# zip data arrays
pair_data = lambda x , y : zip(x , y)
# random direction generator
direction = lambda : rand.randint(1,dim)
print direction()
# noise characteristics
mean, std_dev = 0, 0.1
noise = lambda : np.random.normal(mean, std_dev)
# movement including Gaussian noise
movement = lambda position : position + walk_step * direction() + noise()
