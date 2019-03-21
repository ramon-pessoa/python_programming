'''
Problem #2 [Hard]: Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
'''

'''
This problem can be solve with division: 
an optimal solution is find the product of all numbers in the array and then divide by each of the numbers.
This solution is O(n) + O(n) = O(n)
'''
def get_array_with_the_product_of_all(arr):
	prod = 1
	for value in arr:
		prod = prod * value
	print("prod", prod)
	new_arr = []
	for value in arr:
		new_value = prod/value
		new_arr.append(new_value)
	return new_arr


arr1 = [3, 2, 1]
new_arr = get_array_with_the_product_of_all(arr1)
# New array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i
print("New array using [3, 2, 1] input array: ", new_arr)
arr2 = [1, 2, 3, 4, 5]
new_arr = get_array_with_the_product_of_all(arr2)
print("New array using [1, 2, 3, 4, 5] input array: ", new_arr)
