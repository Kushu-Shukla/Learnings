# Array -> array is a data structure that stores a fixed size collection of elements of the same data type, all located in contigous memory location.

import array

nums = array.array('i', [10, 20, 30]) # i means integer type
nums.append(40)
print(nums * 2)

import numpy as np

arr = np.array([1,2,3,4])
print(arr * 2)