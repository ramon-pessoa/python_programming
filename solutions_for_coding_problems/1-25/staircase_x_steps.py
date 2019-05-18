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
Let's generalize what we've learned so that it works if you can take a number of steps from the set X. 

Similar reasoning tells us that if X = {1, 3, 5}, then our algorithm should be f(n) = f(n - 1) + f(n - 3) + f(n - 5). 

If n < 0, then we should return 0 since we can't start from a negative number of steps.

This solution is very slow (O(|X|^N)) since we are repeating computations again.
'''

def staircase(n, X):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	else:
		return sum(staircase(n - x, X) for x in X)


for n in range(1, 10):
	X = {1, 3, 5} 
	print("Given n={0} and X={1}, the number of unique ways you can climb the staircase is {2}.".format(n, X, staircase(n, X)))
