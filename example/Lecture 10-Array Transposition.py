import numpy as np

arr = np.arange(8).reshape((2, 4))
print(arr)

print("\n Change to vertical: \n", arr.T)
print("\n Vertical arr: \n", np.dot(arr.T, arr))

arr3d = np.arange(50).reshape((5, 5, 2))
print("\nArray 3d matrix: \n", arr3d)

transpose = arr3d.transpose((1, 0, 2))
print("\nTranspose:\n ", transpose)

print("---------------Arrange------------")
points = np.arange(-5, 5, 1)
print(points)