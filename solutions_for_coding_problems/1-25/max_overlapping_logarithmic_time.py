'''
Problem #21 [Easy]: Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

'''
The solution in max_overlapping_quadratic_time.py takes O(n^2) time, since we're checking each interval pairwise.
We can do better.

One solution is to extract the start times and end times of all the intervals and sort them.
Then we can start two pointers on each list, and consider the following:
* If the current start is before the current end, then we have a new overlap. Increment the start pointer.
* If the current start is after the current end, then our overlap closes. Increment the end pointer.

All that's left to do is keep a couple variables to keep track of the maximum number of overlaps we've seen so far and the current number of overlaps.
'''

def max_overlapping(intervals):
	starts = sorted(start for start, end in intervals)
	ends = sorted(end for start, end in intervals)

	current_max = 0
	current_overlap = 0
	i, j = 0, 0
	while i < len(intervals) and j < len(intervals):
		if starts[i] < ends[j]:
			current_overlap += 1
			current_max = max(current_max, current_overlap)
			i += 1
		else:
			current_overlap -= 1
			j += 1
	return current_max


print("Given the [(30, 75), (0, 50), (60, 150)] array for classroom lectures (possibly overlapping).")
print("The minimum number of rooms required is {}".format(max_overlapping([(30, 75), (0, 50), (60, 150)])))
