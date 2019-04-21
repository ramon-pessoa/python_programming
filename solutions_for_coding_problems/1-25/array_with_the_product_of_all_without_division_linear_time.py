'''
Problem #2 [Hard]: Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
'''

'''
In order to find the product of numbers before i, we can generate a list of prefix products.
Specifically, the ith element in the list would be a product of all numbers including i.
Similarly, we could generate the list of suffix products.
This runs in O(N) time and space, since iterating over the input arrays takes O(N) time 
and creating the prefix and sufix take up O(N) space.
'''
def get_array_with_the_product_of_all(nums):
    # Generate prefix products
    prefix_products = []
    for num in nums:
    	if prefix_products:
    		prefix_products.append(prefix_products[-1] * num)
    	else:
    		prefix_products.append(num)

    # Generate suffix products
    suffix_products = []
    for num in reversed(nums):
    	if suffix_products:
    		suffix_products.append(suffix_products[-1] * num)
    	else:
    		suffix_products.append(num)

    suffix_products = list(reversed(suffix_products))

    # Generate result
    result = []
    for i in range(len(nums)):
    	if i == 0:
    		result.append(suffix_products[i + 1])
    	elif i == len(nums) - 1:
    		result.append(prefix_products[i - 1])
    	else:
    		result.append(prefix_products[i - 1] * suffix_products[i + 1])
    return result


arr1 = [3, 2, 1]
new_arr = get_array_with_the_product_of_all(arr1)
# New array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i
print("New array using [3, 2, 1] input array: ", new_arr)
arr2 = [1, 2, 3, 4, 5]
new_arr = get_array_with_the_product_of_all(arr2)
print("New array using [1, 2, 3, 4, 5] input array: ", new_arr)
