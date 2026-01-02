import numpy as np 
a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(f"Original array:\n{a}")
#accessing elements
print(f"Element at row 0, column 1: {a[0,1]}") #2
print(f"Element at row 1, column 4: {a[1,4]}") #12
#slicing arrays
print(f"Slicing rows 0 to 1 and columns 2 to 4:\n{a[0:2,2:5]}")
print(f"Slicing all rows and columns 3 to end:\n{a[:,3:]}")
print(f"Slicing row 1 and all columns:\n{a[1,:]}")
#using negative indices
print(f"Element at last row, last column: {a[-1,-1]}") #14
print(f"Slicing last two rows and last three columns:\n{a[-2:,-3:]}")
#modifying elements
a[1,6]=69
print(f"Modified array:\n{a}")
a[0,0:3]=[21,22,23]
print(f"Array after modifying first three elements of first row:\n{a}")
#advanced slicing
print(f"Every second element in second row:\n{a[1,::2]}")
print(f"Reversing first row:\n{a[0,::-1]}")
#2D array slicing with step
print(f"Slicing rows with step 2 and columns with step 3:\n{a[::2,::3]}")
#boolean indexing
bool_idx = a > 10
print(f"Boolean index array:\n{bool_idx}")
print(f"Elements greater than 10:\n{a[bool_idx]}")
print(f"Elements greater than 10 (directly):\n{a[a > 10]}")
#reshaping array
b=a.reshape(7,2)
print(f"Reshaped array (7x2):\n{b}")
#flattening array
flat_a=a.flatten()
print(f"Flattened array:\n{flat_a}")
#iterating through array
print("Iterating through array elements:")
for element in a.flat:
    print(element, end=' ')
print()
#same for 3D arrays
c=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(f"3D array:\n{c}")
print(f"Element at [1,0,2]: {c[1,0,2]}") #9
print(f"Slicing first block and all rows and columns:\n{c[0,:,:]}")
print(f"Slicing all blocks, first row, all columns:\n{c[:,0,:]}")
print(f"Slicing all blocks, all rows, first column:\n{c[:,:,0]}")
c[0,1,2]=42
print(f"Modified 3D array:\n{c}")   
c_reshaped=c.reshape(3,4)
print(f"Reshaped 3D array (3x4):\n{c_reshaped}")
flat_c=c.flatten()
print(f"Flattened 3D array:\n{flat_c}")
#iterating through 3D array
print("Iterating through 3D array elements:")
for element in c.flat:
    print(element, end=' ')
print()