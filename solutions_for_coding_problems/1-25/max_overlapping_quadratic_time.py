'''
Problem #21 [Easy]: Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

'''
First, notice that the minimum number of classroom halls is the maximum number of overlapping intervals.

Now let's consider the naive approach. 
We could go through each interval and check every other interval and see if it overlaps, keeping track of the largest number of overlapping intervals.

This solution would take O(n^2) time, since we're checking each interval pairwise.
'''

def overlaps(a, b):
	start_a, end_a = a
	start_b, end_b = b
	# It doesn't overlap if it's like this:
	# |start_a .... end_a| <---> |start_b ... end_b|
	# or like this:
	# |start_b .... end_b| <---> |start_a ... end_a|
	# so return not or either of these

	return not (end_a < start_b or start_a > end_b)


def max_overlapping(intervals):
	current_max = 0
	for interval in intervals:
		num_overlapping = sum(overlaps(interval, other_interval)
			for other_interval in intervals
			if interval is not other_interval)
		current_max = max(current_max, num_overlapping)
	return current_max

print("Given the [(30, 75), (0, 50), (60, 150)] array for classroom lectures (possibly overlapping).")
print("The minimum number of rooms required is {}".format(max_overlapping([(30, 75), (0, 50), (60, 150)])))
