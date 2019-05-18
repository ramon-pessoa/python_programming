'''
Problem #12 [Hard]: There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:


1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''

''' 
The solution in staircase_recursion_fibonacci.py is really slow (O(2 ^ N)).
We are doing a lot of repeated computations! 

We can do it a lot faster by just computing iteratively:
'''

def staircase(n):
	a, b = 1, 2
	for _ in range(n - 1):
		a, b = b, a + b
	return a



for n in range(1, 10):
	print("Given n={0}, the number of unique ways you can climb the staircase is {1}.".format(n, staircase(n)))