'''
Problem #1 [Easy]: Given a list of numbers and a number k, return whether any two numbers from the list add up to k. 
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17. 
Bonus: Can you do this in one pass?
'''

'''
This solution uses sorting and binary search.
After sorting the list, we can iterate through the list and run a binary search on K - list[i].
Since we run binary search on N elements, this would take O(N log N) with O(1) space.
'''

from bisect import bisect_left

def contains_pair_with_sum(list1, k):
	list1.sort()

	for i in range(len(list1)):
		target = k - list1[i]
		j = binary_search(list1, target)
		# Check that binary search found the target and that it's not in the same index as i.
		# If it is in the same index, we can check list[i + 1] and list[i - 1] 
		# to see if there is another number that is the same value as list[i]
		if j == -1:
			continue
		elif j != i:
			return True
		elif j + 1 < len(list1) and list1[j + 1] == target:
			return True
		elif j - 1 >= 0 and list1[j - 1] == target:
			return True
	return False


def binary_search(list1, target):
	lo = 0
	hi = len(list1)
	
	ind = bisect_left(list1, target, lo, hi)

	if 0 <= ind < hi and list1[ind] == target:
		return ind

	return -1


list1 = [10, 15, 3, 7]
k = 17
contains_sum = contains_pair_with_sum(list1, k)
print("Contains pair with sum list={10, 15, 3, 7}, k=17? ", contains_sum)

list2 = [10, 15, 3, 6]
contains_sum = contains_pair_with_sum(list2, k)
print("Contains pair with sum list={10, 15, 3, 6}, k=17? ", contains_sum)
