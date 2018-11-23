import numpy as np

arr = np.arange(0, 11)
print("Array Number: ", arr)
print(arr[8])
print(arr[0:5])

arr[0:5] = 100

arr_copy = arr.copy()
print("\nArr Copy: ", arr_copy)

arr_2d = np.array(([5, 10, 15], [20, 25, 30], [35, 40, 45]))
print("\nArray second: ", arr_2d)

print("\nGet First Row: ", arr_2d[0])
print("\nGet Second Row: ", arr_2d[1])
print("\nGet Third Row: ", arr_2d[2])

print("\nGet value of row x column", arr_2d[1], [0])

arr_2d
print("Get value everything row x column", arr_2d[:2, 1:])
print("Get Array: ", arr_2d[2])

arr_2d = np.zeros((10, 10))
arr_length = arr_2d.shape[1]
print(arr_length)

for i in range(arr_length): arr_2d[i] = i
print(arr_2d[[2, 4, 6, 8]])
