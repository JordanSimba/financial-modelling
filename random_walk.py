import numpy as np
import random as rand
import direction_space as ds
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import animation

# step size
walk_step = 1.0
# range
start_time = 1
stop_time = 10
# sample size
samples = 100

# direction vectors
# 2 dimensions
space = ds.direction_space()
dim = space.dim

# TODO possibly make list of vectors available from contract of direction_space
origin, x_hat ,y_hat = space.origin, space.x_unit, space.y_unit
vector_space = [x_hat, y_hat]
sign = [1, -1]

# random number generator
rand_int = lambda m, n : rand.randint(m,n)
# noise characteristics
mean, std_dev = 0, 0.01 # 1/10 deviation. Careful with dev as percentage of step size
noise = lambda : np.random.normal(mean, std_dev, dim)
# movement including Gaussian noise

def get_rand_linear_comb(vector_space):
    random_vectors = rand.sample(vector_space, rand_int(1,dim))
    # TODO add random linear weights alpha & beta in future
    signed_vectors = [rand.choice(sign) * vector for vector in random_vectors]
    return sum(signed_vectors)

movement = lambda position : position + \
                    walk_step * get_rand_linear_comb(vector_space) + noise()
print movement(origin)

# init sequence array
rand_walk_sequence = [origin] # start from origin
time = np.linspace(start_time, stop_time, samples)
print "len time:", len(time)
print "sqrt(num_of_steps):", np.sqrt(samples)
for i in range(1, len(time)):
    prev_pos = rand_walk_sequence[i - 1]
    current_pos = movement(prev_pos)
    rand_walk_sequence.append(current_pos)

rand_walk_array = np.array(rand_walk_sequence)
print "shape of walk:", rand_walk_array.shape

x = rand_walk_array[:,0]
y = rand_walk_array[:,1]
# TODO Add significant statistics

# TODO Add animated graph to visualise walk
plt.plot(x, y, lw=2)
plt.show()
# save data as txt file
# np.savetxt('multi_dim_random_walk.txt', rand_walk_array, fmt='%1.2f')
