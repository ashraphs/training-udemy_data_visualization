import numpy as np

arr = np.arange(11)
print(arr)

print("Square Root: \n", np.sqrt(arr))
print("\nExponential: \n", np.exp(arr))

A = np.random.randn(10)
print("\nRandom Number: \n", A)

B = np.random.randn(10)
print("\nRandom Number: \n", B)

# Binary Function
print("\nBinary Function: \n", np.add(A, B))

# Find max
print("\nMax Value: \n", np.maximum(A, B))
