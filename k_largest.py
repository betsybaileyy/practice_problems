'''
Given an array of numbers and a count k 
find the k largest values in the array.
Example: a=[3, 5, 7, 8, 4], k=3  =>  [5, 7, 8]
'''

import math
"""
Sort the given array then return the largest(k) values.
"""
def get_largest_k_naive(array, k):
	# sort the array
	array = array[:]
	array.sort()
	# return the largest(k) values.
	return array[-k:]


"""
Create an array of length(k) then iterate through original array.
if a value is greater than any number in the "largest" array,
remove the lesser value and input the new value to the "largest" array.
"""
def get_k_largest(array, k):
    array = array[:]
    largest_nums = []
    max_num = 0
    
    # while the length is less than k
    while len(largest_nums) < k:
        max_num = max(array)
        max_num_index = array.index(max_num)
        array.pop(max_num_index)

        print("largest value:", max_num)
        largest_nums.append(max_num)
        print("length of array", len(largest_nums))
       
    return largest_nums

if __name__ == "__main__":
    array = [6, 9, 1, 11, 3, 2, 4, 20]
    k = 3
    print(get_k_largest(array, k)) 