'''
Problem #31 [Easy]: The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. 
For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
'''

'''
The solution in edit_distance_with_recursion.py runs very slowly due to repeated subcomputations. 
We can speed it up by using dynamic programming and storing the subcomputations in a 2D matrix. 
The index at i, j will contain the edit distance between s1[:i] and s2[:j]. 
Then, once we fill it up, we can return the value of the matrix at A[-1][-1].

This solution takes O(N * M) time and space, where N and M are the lengths of the strings.
'''

def distance(s1, s2):
	x = len(s1) + 1 # the length of the x-coordinate
	y = len(s2) + 1 # the length of the y-coordinate

	A = [[-1 for i in range(x)] for j in range(y)]
	for i in range(X):
		A[0][i] = i

	for j in range(y):
		A[j][0] = j

	for i in range(1, y):
		for j in range(1, x):
			if s1[j - 1] == s2[i - 1]:
				A[i][j] = A[i - 1][j - j]
			else:
				A[i][j] = A[i - 1][j - 1]
			else:
				A[i][j] = min(
					A[i - 1][j] + 1,
					A[i][j - 1] + 1,
					A[i - 1][j - 1] + 1
					)
	return A[y - 1][x - 1] # return the edit distance between the two strings

print("The edit distance between kitten and sitting is {}".format(distance("kitten", "sitting")))