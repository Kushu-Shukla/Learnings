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

Ques -> Static Array vs Dynamic Array
Ans -> 

Static Array