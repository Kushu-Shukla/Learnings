# !. Basics of Array
# Quese -> What is an Array
# Ans -> An array is a collection of iterms stored at contiguous memory location of same type. The idea is to store the multuple items of the same type together. This make it easier to calulate the position of each element by simply adding an offset to a base value, i.e the memory location of the first element of the array
age_of_a = 22
age_of_k = 150
age_of_r = 24

print(id(age_of_a))
print(id(age_of_k))
print(id(age_of_r))

from array import *

arr = array('i', [1,2,3,4,5])
print(id(arr))
print(type(arr))

arr2 = array("B")

