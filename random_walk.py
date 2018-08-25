import numpy as np
import random as rand

# step size
walk_step = 1.0

# range
start_time = 1
stop_time = 1000

# sample size
samples = 1000

# direction vectors
# 1 dimension
x_pos = 1
x_neg = -1
directions = [x_pos, x_neg]

# zip data arrays
pair_data = lambda x , y : zip(x , y)
# random direction generator
direction = lambda : rand.choice(directions)
# noise characteristics
mean, std_dev = 0, 0.1
noise = lambda : np.random.normal(mean, std_dev)
# movement including Gaussian noise
movement = lambda position : position + walk_step * direction() + noise()

# init sequence array
rand_walk_sequence = [0] # start from origin
time = np.linspace(start_time, stop_time, samples)
print "len time:", len(time)
print "sqrt(num_of_steps):", np.sqrt(samples)
for i in range(1, len(time)):
    prev_pos = rand_walk_sequence[i - 1]
    current_pos = movement(prev_pos)
    rand_walk_sequence.append(current_pos)

rand_walk_array = np.array(rand_walk_sequence)
xy_data = pair_data(time, rand_walk_sequence)

print "mean:", np.average(rand_walk_array)
print "rms:", np.sqrt(np.average(np.square(rand_walk_array)))

# save data as txt file
np.savetxt('random_walk.txt', xy_data, fmt='%1.2f')
