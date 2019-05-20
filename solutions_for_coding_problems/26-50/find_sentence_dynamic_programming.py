'''
Problem #22 [Medium]: Given a dictionary of words and a string made up of those words (no spaces), return the original sentence 
in a list. 
If there is more than one possible reconstruction, return any of them. 
If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return 
['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either 
['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
'''

'''
The solution in find_sentence_backtracking.py will run in O(2^N) time.

We can improve the running time by using dynamic programming to store repeated subcomputations. 
This reduces the running time to just O(N^2). 
We'll keep a dictionary that maps from indices to the last word that can be made up to that index. 
We'll call these starts. 
Then, we just need to do two nested for loops, one that iterates over the whole string and tries to find a start at that index, 
and a loop that checks each start to see if a new word can be made from that start to the current index.

Now we can simply take the start at the last index and build our sentence backwards:

Now this runs in O(N^2) time and O(N) space.
'''

def find_sentence(dictionary, s):
	starts = {0: ''}
	for i in range(len(s) + 1):
		new_starts = starts.copy()
		for start_index, _ in starts.items():
			word = s[start_index:i]
			if word in dictionary:
				new_starts[i] = word
		starts = new_starts.copy()

	result = []
	current_length = len(s)
	if current_length not in starts:
		return None
	while current_length > 0:
		word = starts[current_length]
		current_length -= len(word)
		result.append(word)

	return list(reversed(result))


dic = {'quick', 'brown', 'the', 'fox'}
sentence = "thequickbrownfox"
print("Given the dictionary {0} and the string '{1}', the original sentence in a list is {2}.".format(dic, sentence, find_sentence(dic, sentence)))

dic = {'bed', 'bath', 'bedbath', 'and', 'beyond'}
sentence = "bedbathandbeyond"
print("Given the dictionary {0} and the string '{1}', the original sentence in a list is {2}.".format(dic, sentence, find_sentence(dic, sentence)))

dic = {'bed', 'bath', 'bedbath', 'and', 'beyond'}
sentence = "nomatch"
print("Given the dictionary {0} and the string '{1}', the original sentence in a list is {2}.".format(dic, sentence, find_sentence(dic, sentence)))
