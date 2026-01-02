import numpy as np
a=np.array([1,2,3]) #1D array
print(a)
b=np.array([[1,2,3],[4,5,6]]) #2D array
print(b)
#getting array dimensions
print(f"Dimensions of a: {a.ndim}")
print(f"Dimensions of b: {b.ndim}")
#getting shape of arrays
print(f"Shape of a: {a.shape}") #(3,): 3 elements in 1 dimension
print(f"Shape of b: {b.shape}") #(2, 3): 2 rows and 3 columns
#getting type
print(f"Data type of a: {a.dtype}")
print(f"Data type of b: {b.dtype}")
c=np.array([1.5,2.5,3.5], dtype=np.float16) #specifying data type
print(f"Array c: {c}, Data type: {c.dtype}")
#getting size
print(f"Item size of a: {a.itemsize} bytes") #bytes per element
print(f"Total size of a: {a.nbytes} bytes") #total bytes
print(f"size of a: {a.size} elements") #total number of elements
print(f"Total size of a: {a.size * a.itemsize} bytes") #total bytes calculated
#other ways to create arrays
arr1 = np. array([1, 2, 3, 4, 5])
arr2 = np.zeros(5)
arr3 = np.ones(5)
arr4 = np.arange(0, 10, 2)  # 0, 2, 4, 6, 8
arr5 = np.linspace(0, 1, 5)  # 5 numbers between 0 and 1
print(f"arr1: {arr1}, arr2: {arr2}, arr3: {arr3}, arr4: {arr4}, arr5: {arr5}")