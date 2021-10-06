import numpy as np


# Create numpy array from list L
L = [1,2,3]
np_arr = np.array(L)
print(np_arr)

# Create multidimensional tensors
t = np.array([[1,2,3],[4,5,6]])
print(t)
print(t.shape)

# Generate zeros
print(np.zeros((2,3)))

# Generate random numbers
print("Random int values upto 100:\n", np.random.randint(100,size = (2,3)))
print("Random float values from uniform distribution over [0,1] of shape (2,3):\n", np.random.rand(2,3))
print("Random float values from normal distribution of shape (2,3):\n", np.random.randn(2,3))

# Add tensors
t1 = np.array([[1,2,3],[4,5,6]])
t2 = np.array([[7,8,9],[10,11,12]])
t3 = t1+t2
print(t3)

# Sum elements
print(np.sum(t3))

# Sum across axis
print(np.sum(t3, axis=0))
print(np.sum(t3, axis=1))

# Transpose
print(t1.T)

# Dot product
print(np.dot(t1, t2.T))

# Concatenate tensors
print("Along axis = 0:\n", np.concatenate((t1,t2), axis = 0))
print("Along axis = 1:\n", np.concatenate((t1,t2), axis = 1))
print("Flatten:\n", np.concatenate((t1,t2), axis = None))
