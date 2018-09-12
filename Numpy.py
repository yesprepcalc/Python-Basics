#install with pip: go to Python directory containing pip and pip install numpy
import numpy as np

#can make matrices as numpy arrays
#which takes a list of lists representing rows
X = np.array([[1, 3, 2, 5], [4, 2, 2, 1], [6, 5, 1, 3]])
X
print(X.shape)
print(X.ndim)
print(X)

#linspace makes equal divisions from a start to end point
A = np.linspace(0, 1, 5)
print(A)

#makes diagonal matrices
B = np.diag(np.array([1,2,3,4]))
print(B)

#random numbers from uniform dist
C = np.random.rand(4)
print(C)

#random numbers from normal dist
D = np.random.randn(4)
print(D)

E = np.random.randn(4)
Y = np.array([C, D, E])

#matrix multiplication
print(Y.T.dot(X))

#sums
print(X.sum(axis=0)) #col sums
print(X.sum(axis=1)) #row sums
print(X.sum()) #total sum

#other useful attributes/operations:
#min, max, argmin, argmax, mean, median, std

