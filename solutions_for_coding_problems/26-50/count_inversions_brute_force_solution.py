'''
Problem #44 [Medium]: We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion: (5, 4), (5, 3), (5, 2), (5, 1), (4, 3), (4, 2), (4, 1), (3, 2), (3, 1), (2, 1).
'''

'''
The brute force solution comes naturally from the definition: we can run a
doubly nested for loop over all pairs, and increment a counter whenever we encounter a
larger element before a smaller element. Like the solution below:
'''

def count_inversions(arr):
	count = 0
	for i in range(len(arr) - 1):
		for j in range(i + 1, len(arr)):
			if arr[i] > arr[j]:
				print("[%s, %s]" % (arr[i], arr[j]), end=" ")
				count += 1

	return count


print("\nNumber of inversions [5, 4, 3, 2, 1] has: %s" % count_inversions([5, 4, 3, 2, 1]))