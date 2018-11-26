import numpy as np
import matplotlib.pyplot as plt

plt.show()

points = np.arange(-5, 5, 0.01)
dx, dy = np.meshgrid(points, points)

print("-----------------dx-------------------")
print(dx)

print("-----------------dy-------------------")
print(dy)

print("-----------------Z = sin value-------------------")
z = (np.sin(dx) + np.sin(dy))
print(z)

plt.imshow(z)
plt.colorbar()
plt.title('Plot for sin(x) + sin(y)')
plt.show()

# Numpy where
print("-------------if/else condition--------------")
A = np.array([1, 2, 3, 4])
B = np.array([100, 200, 300, 400])

condition = np.array([True, True, False, False])

answer = [(A_val if cond else B_val) for A_val, B_val, cond in zip(A, B, condition)]
print(answer)

answer2 = np.where(condition, A, B)
print("Using numpy: ", answer2)

print("--------------numpy random-------------------")
from numpy.random import randn

arr = randn(5, 5)
print(arr)

print("------numpy random with condition------------")
condition3 = np.where(arr < 0, 0, arr)
print(condition3)

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("---------------------------------------------")
print("Array Matrix :\n", arr2)
print("Sum: ", sum(arr2))
print("Mean: ", arr2.mean())
print("Standard Deviation: ", arr2.std())
print("Population Variance: ", arr2.var())

print("-------------------Bool Array----------------")
bool_arr = np.array([True, False, True])
print(bool_arr.any())
print(bool_arr.all())

print("-------------------Sort----------------------")
arr = randn(5)
print(arr)
print(arr.sort())

print("-------------------Unique Value----------------------")
countries = np.array(['France', 'Germany', 'USA', 'Russia', 'USA', 'Mexico', 'Germany'])
print(np.unique(countries))
print(np.in1d(['France', 'rusia', 'Germany'], countries))
