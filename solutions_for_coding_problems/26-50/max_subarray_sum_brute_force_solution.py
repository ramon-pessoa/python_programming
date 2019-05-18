'''
Problem #49 [Medium]: Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
'''

'''
The brute force approach here would be to iterate over every contiguous subarray and calculate its sum, keeping track of the largest one seen.
This would run in O(N^3) time. 
'''

def max_subarray_sum(arr):
	current_max = 0
	for i in range(len(arr)):
		for j in range(i, len(arr)):
			current_max = max(current_max, sum(arr[i:j+1]))
	return current_max


arr = [34, -50, 42, 14, -5, 86]
print("Given the array {0}, the maximum sum of any contiguous subarray of the array is {1}".format(arr, max_subarray_sum(arr)))

arr = [-5, -1, -8, -9]
print("Given the array {0}, the maximum sum of any contiguous subarray of the array is {1}".format(arr, max_subarray_sum(arr)))

