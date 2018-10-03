import numpy as np

# TODO Make basis dynamic
class vector_space:

    # init vector space on creation of object
    def __init__(self, dim):
        self.origin = np.zeros(dim)
        self.non_zero_vectors = ["vect_" + str(i) for i in range(1,dim + 1)]

        self.origin = np.array([0,0])
        self.x_unit = np.array([1,0])
        self.y_unit = np.array([0,1])
        self.dim = 2

    def generate_basis(self):
        matching_dimensionality = len(self.non_zero_vectors) == self.dim
        print "basis generated", matching_dimensionality

    def one_shot_encode(self, vectors):
        pass

    def vector_dictionary(self, vectors):
        pass


space = vector_space(2)
space.generate_basis()
print space.non_zero_vectors
