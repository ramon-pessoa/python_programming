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
We can improve our build_word_right and build_word_down functions a bit by just taking what we need, which is whichever is 
shorter between the length of the word and the end of the row or column.

However, let's say our word were both really big.  Another otimization is in word_search3.py.
'''

def build_word_right(matrix, r, c, length):
	row_len = len(matrix[0])
	return ''.join([matrix[r][i] for i in range(c, min(row_len, length))])


def build_word_down(matrix, r, c, length):
	col_len = len(matrix)
	return ''.join([matrix[i][c] for i in range(r, min(col_len, length))])


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

