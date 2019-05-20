'''
Problem #63 [Easy]: Given a 2D matrix of characters and a target word, write a function that returns whether the word can 
be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix and the target word 'FOAM', you should return true, since it's the leftmost column. 
Similarly, given the target word 'MASS', you should return true, since it's the last row.


[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

'''

'''
Solution 1: we can go through each entry in the array, try to create the word going right and down, and check if the word 
matches our word. 

To make bounds checking simple, we'll just try to grab everything from where we're looking at till the end, and then use the 
slice operator to just get what we want.

However, if the matrix was really big, then we would be grabbing the whole row or column just to shorten it.
'''

def build_word_right(matrix, r, c, length):
	return ''.join([matrix[r][i] for i in range(c, len(matrix[0]))])[:length]


def build_word_down(matrix, r, c, length):
	return ''.join([matrix[i][c] for i in range(r, len(matrix))])[:length]


def word_search(matrix, word):
	for r in range(len(matrix)):
		for c in range(len(matrix[0])):
			word_right = build_word_right(matrix, r, c, len(word))
			word_down = build_word_down(matrix, r, c, len(word))

			if word in (word_right, word_down):
				return True

	return False


matrix = [['F', 'A', 'C', 'I'], ['O', 'B', 'Q', 'P'], ['A', 'N', 'O', 'B'], ['M', 'A', 'S', 'S']]

target =  'FOAM'
print("Does the target word '{0}' exist in the matrix {1}? {2}".format(target, matrix, word_search(matrix, target)))

target =  'MASS'
print("Does the target word '{0}' exist in the matrix {1}? {2}".format(target, matrix, word_search(matrix, target)))

target =  'NOTFOUND'
print("Does the target word '{0}' exist in the matrix {1}? {2}".format(target, matrix, word_search(matrix, target)))

