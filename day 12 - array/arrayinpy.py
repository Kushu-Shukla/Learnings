# !. Basics of Array
# Quese -> What is an Array
# Ans -> An array is a collection of iterms stored at contiguous memory location of same type. The idea is to store the multuple items of the same type together. This make it easier to calulate the position of each element by simply adding an offset to a base value, i.e the memory location of the first element of the array
age_of_a = -22
age_of_k = 150
age_of_r = 24

print(age_of_a)
print(id(age_of_k))
print(id(age_of_r))

from array import *

arr = array('i', [1,2,3,4,5])
print(id(arr))
print(type(arr))

arr2 = array("I", [23,53,32,35,1,2,535])
print(arr2)

# here to define an array of a particular type we need to use type-code, just like in the above case we used 'i' for integer type array. 
# Some commonly used type codes are:
# 'i' - signed integer
# 'I' - unsigned integer
# 'f' - floating point
# 'd' - double floating point
# 'u' - Unicode character
# 'b' - signed char (0 to 255)
# 'B' - unsigned char
# 'h' - signed short   
# 'H' - unsigned short
# 'l' - signed long
# 'L' - unsigned long
# 'q' - signed long long
# 'Q' - unsigned long long
# 'I' - unsigned integer
# 'c' - char (string of length 1)
# 'P' - pointer (used for storing memory addresses)
# '?' - boolean (True or False)

# signed integer -> -2,147,483,648 to 2,147,483,64
var = -1923147483648
print(var)
print(type(var))
# unsigned integer -> 0 to 4,294,967,28

# Ques -> Static vs Dynamic Arrays
# Ans -> 
# 
# Static Arrays:
# 1. Fixed Size: The size of a static array is defined at the time of declaration and cannot be changed during runtime.
# 2. Memory Allocation: Memory for static arrays is allocated on the stack, which can lead to faster access times.
# 3. Performance: Static arrays can be more efficient in terms of performance due to their fixed size and stack allocation.
# 4. Example: In languages like C and C++, arrays declared with a fixed size are static arrays.
#
# Dynamic Arrays:
# 1. Variable Size: The size of a dynamic array can be changed during runtime, allowing for more flexibility in handling varying amounts of data.
# 2. Memory Allocation: Memory for dynamic arrays is allocated on the heap, which can lead to slower access times compared to stack allocation.
# 3. Performance: Dynamic arrays may have overhead due to resizing operations and heap allocation, which can impact performance.
# 4. Example: In languages like Python, lists are dynamic arrays that can grow and shrink in size.

# Ques -> Python list vs array.array (differences, when to use)
# Ans -> Python lists are dynamic arrays that can hold elements of different types, while array.array is a more efficient array implementation that requires all elements to be of the same type. Use lists when you need flexibility in element types and array.array when you need better performance for large amounts of data of the same type.
#
# Ques -> Advantages and Disadvantages of Arrays
# Ans -> Advantages of Arrays:
# 1. Fast Access: Arrays provide O(1) time complexity for accessing elements by index.
# 2. Memory Efficiency: Arrays use contiguous memory locations, which can lead to better cache
#    performance.
# 3. Simplicity: Arrays are simple to understand and use for storing collections of
#    homogeneous data.
# Disadvantages of Arrays:
# 1. Fixed Size: Static arrays have a fixed size, which can lead to wasted memory or overflow if the size is not properly managed.
# 2. Homogeneous Data: Arrays can only store elements of the same type, limiting flexibility.
# 3. Insertion/Deletion: Inserting or deleting elements in an array can be inefficient, as it may require shifting elements.    
# 4. Memory Allocation: Dynamic arrays may require resizing, which can lead to performance overhead.

# Ques -> Creating an array (using array module)
# Ans -> You can create an array using the array module by specifying the type code and initial values. For example:
# ```python
# from array import array
# arr = array('i', [1, 2, 3, 4, 5])  # 'i' is the type code for signed integers
# ```

# Ques -> Memory representation of arrays
# Ans -> Arrays are stored in contiguous memory locations, which allows for efficient access and manipulation of elements. The memory layout is typically a single block of memory that holds all the elements of the array.

# Ques -> Indexing & Negative Indexing
# Ans -> You can access elements in an array using their index, with the first element at index 0. Negative indexing is also supported, allowing you to access elements from the end of the array (e.g., -1 refers to the last element).
print(vals[0])  # Accessing first element
print(vals[-1]) # Accessing last element
# Ques -> Slicing arrays
# Ans -> You can slice arrays to create a new array containing a subset of elements. For example:
print(vals[1:4])  # Slicing from index 1 to 3
print(vals[:3])   # Slicing from start to index 2
print(vals[2:])   # Slicing from index 2 to end
print(vals[:])    # Slicing the entire array
# Ques -> Iterating through an array
for i in vals:
    print(i)


# Ques -> Traversing an array (for loop, while loop, for-each)
# Ans -> You can traverse an array using different types of loops. For example:
# Using a for loop
for i in range(len(vals)):
    print(vals[i])
# Using a while loop
i = 0
while i < len(vals):
    print(vals[i])
    i += 1
# Using a for-each loop
for val in vals:
    print(val)

# Ques -> Input/Output of arrays
# Ans -> You can read input into an array and print the elements of an array. For example:
# Input
n = int(input("Enter number of elements: "))
user_vals = array('i', [])
for _ in range(n):  # Using underscore for unused variable
    user_vals.append(int(input("Enter element: ")))     
print("Array elements are:")
for val in user_vals:
    print(val)  
# Output
print("Array elements are:", user_vals) 


