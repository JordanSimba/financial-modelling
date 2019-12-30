import numpy as np
import random as rand
import direction_space as ds
import matplotlib
matplotlib.use('TKAgg')
from matplotlib import pyplot as plt
from matplotlib import animation

# step size
walk_step = 1.0
# range
start_time = 1
stop_time = 100
# sample size
samples = 1000

# direction vectors
# 2 dimensions
space = ds.direction_space()
dim = space.dim

# TODO possibly make list of vectors available from contract of direction_space
origin, x_hat ,y_hat = space.origin, space.x_unit, space.y_unit
vector_space = [x_hat, y_hat]
sign = [1, -1]

# zip data arrays
pair_data = lambda x , y : zip(x , y)
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
# TODO Add significant statistics

fig = plt.figure()
ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    x = rand_walk_array[:,0]
    y = rand_walk_array[:,1]
    # x = np.linspace(0, 2, 1000)
    # y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
# anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
# save data as txt file
# np.savetxt('multi_dim_random_walk.txt', rand_walk_array, fmt='%1.2f')
