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
If we notice, when we're checking the current row or column, that the first few letters are off, then we can quit the search 
early.

The Python built-in function zip is very handy:
'''

def check_word_right(matrix, r, c, word):
	word_len = len(word)
	row_len = len(matrix[0])
	if word_len != row_len - c:
		return False
	for c1, c2 in zip(word, (matrix[r][i] for i in range(c, row_len))):
		if c1 != c2:
			return False

	return True


def check_word_down(matrix, r, c, word):
	word_len = len(word)
	col_len = len(matrix)
	if word_len != col_len - r:
		return False
	for c1, c2 in zip(word, (matrix[i][c] for i in range(r, col_len))):
		if c1 != c2:
			return False

	return True

	return ''.join([matrix[i][c] for i in range(r, min(col_len, length))])


def word_search(matrix, word):
	for r, row in enumerate(matrix):
		for c, val in enumerate(row):
			if check_word_right(matrix, r, c, word):
				return True
			if check_word_down(matrix, r, c, word):
				return True

	return False


matrix = [['F', 'A', 'C', 'I'], ['O', 'B', 'Q', 'P'], ['A', 'N', 'O', 'B'], ['M', 'A', 'S', 'S']]

target =  'FOAM'
print("Does the target word '{0}' exist in the matrix {1}? {2}".format(target, matrix, word_search(matrix, target)))

target =  'MASS'
print("Does the target word '{0}' exist in the matrix {1}? {2}".format(target, matrix, word_search(matrix, target)))

target =  'NOTFOUND'
print("Does the target word '{0}' exist in the matrix {1}? {2}".format(target, matrix, word_search(matrix, target)))

