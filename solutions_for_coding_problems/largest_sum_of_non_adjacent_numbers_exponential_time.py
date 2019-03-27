'''
Problem #9 [Hard]: Given a list of integers, write a function that returns the 
largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] 
should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

'''
This problem is actually quite tricky. It's tempting to try to use a greedy strategy like pick 
the largest number (or first), then the 2nd-largest if it's non-adjacent and 
so on, but these don't work -- there will always be some edge case that breaks it.

Instead, we should look at this problem recursively. Say we had a function that already returns the 
largest sum of non-adjacent integers on smaller inputs. How could we use it to figure out what we want?

Say we used this function on our array from a[1:] and a[2:]. Then our solution should be a[1:] 
OR a[0] + a[2:], whichever is largest. This is because choosing a[1:] precludes us from picking a[0]. 
So, we could write a straightforward recursive solution like below. 
This solution runs in O(2^n) time.
'''

def largest_non_adjacent(arr):
	if not arr:
		return 0

	return max(
		largest_non_adjacent(arr[1:]),
		arr[0] + largest_non_adjacent(arr[2:]))


arr1 = [2, 4, 6, 2, 5]
print('largest_non_adjacent([2, 4, 6, 2, 5]):', largest_non_adjacent(arr1))

arr2 = [5, 1, 1, 5] 
print('largest_non_adjacent([5, 1, 1, 5]):', largest_non_adjacent(arr2))