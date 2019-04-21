'''
Problem #9 [Hard]: Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

'''
The code in largest_sum_of_non_adjacent_numbers_linear_time.py run in O(n) and in O(n) space.
But we can improve this even further. Notice that we only ever use the last two elements of the 
cache when iterating through the array. This suggests that we could just get rid of most of the 
array and just store them as variables:
'''

def largest_non_adjacent(arr):
	if len(arr) <= 2:
		return max(0, max(arr))

	max_excluding_last = max(0, arr[0])
	max_including_last = max(max_excluding_last, arr[1])

	for num in arr[2:]:
		prev_max_including_last = max_including_last

		max_including_last = max(max_including_last, max_excluding_last + num)
		max_excluding_last = prev_max_including_last

	return max(max_including_last, max_excluding_last)


arr1 = [2, 4, 6, 2, 5]
print('largest_non_adjacent([2, 4, 6, 2, 5]):', largest_non_adjacent(arr1))

arr2 = [5, 1, 1, 5] 
print('largest_non_adjacent([5, 1, 1, 5]):', largest_non_adjacent(arr2))