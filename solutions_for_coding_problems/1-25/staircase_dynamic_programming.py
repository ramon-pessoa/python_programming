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
The solution in staircase_x_steps.py is very slow (O(|X|^N)) since we are repeating computations again. 
We can use dynamic programming to speed it up.

Each entry cache[i] will contain the number of ways we can get to step i with the set X. 
Then, we'll build up the array from zero using the same recurrence.
'''

def staircase(n, X):
	cache = [0 for _ in range(n + 1)]
	cache[0] = 1
	for i in range(1, n + 1):
		cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
	return cache[n]


for n in range(1, 10):
	X = {1, 3, 5} 
	print("Given n={0} and X={1}, the number of unique ways you can climb the staircase is {2}.".format(n, X, staircase(n, X)))
