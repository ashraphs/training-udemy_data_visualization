import numpy as np

arr = np.arange(5)
print('Array: ', arr)

arr2 = np.arange(10)
print('Second Array: ', arr2)

np.save('myarray', arr)
print("Call the array: ", np.load('myarray.npy'))

np.savez('Saveboth.npz', x=arr, y=arr2)
archive_array = np.load('Saveboth.npz')

print('X: ', archive_array['x'])
print('Y: ', archive_array['y'])

print("-------------------Save Text----------------------")
arr = np.array([[1, 2, 3], [4, 5, 6]])

np.savetxt('mytextarray.txt', arr, delimiter=',')
arr = np.loadtxt('mytextarray.txt', delimiter=',')
print(arr)
