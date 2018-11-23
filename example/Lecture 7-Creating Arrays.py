import numpy as np

my_list1 = [1, 2, 3, 4]
my_array = np.array(my_list1)

my_list2 = [5, 6, 7, 8]
my_list = [my_list1, my_list2]

my_array2 = np.array(my_list)

print(my_array2.shape)

print(my_array2.dtype)

my_zero_arrays = np.zeros(6)
print("Data type: ", my_zero_arrays)

array_metrix = np.ones([5, 5])
print("\nArray:\n", array_metrix)

array_metrix_empty = np.empty(5)
print("\nnumpy empty:\n", array_metrix_empty)

print("\nNp eye: \n", np.eye(5))

print("\nNp Arrange: \n", np.arange(5,50,4))