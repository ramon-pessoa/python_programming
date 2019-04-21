Some programming examples in Python
===========================

## Contents

1. [Solutions for coding problems](#solutions-for-coding-problems)

## Solutions for coding problems

33. Problem #33 [Easy]: Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

	* Recall that the median of an even-numbered list is the average of the two middle numbers.

	* For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

	```
	2
	1.5
	2
	3.5
	2
	2
	2
	```

	a. Solution (Python) [print_median.py]. The solution uses two heaps: a min-heap and a max-heap. This runs in O(N) space and in O(N log N) time. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/print_median.py) 

Go back to [Contents](#contents).
