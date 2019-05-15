'''
Problem #31 [Easy]: The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. 
For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
'''

'''
First, notice that we can probably define this problem recursively.
If we look at the example (kitten -> sitting) and its solution path (kitten -> sitten -> sittin -> sitting), we can see that it's the minimum distance between sitten and sitting plus one.

The recurrence, then, looks like this:

- If either s1 or s2 are empty, then return the size of the larger of the two strings (since we can trivially turn an empty string into a string by inserting all its characters)
- Otherwise, return the minimum between:
	* The edit distance between each string and the last n - 1 characters of the other plus one
	* If the first character in each string is the same, then the edit distance between s1[1:] and s2[1:], otherwise the same edit distance + 1

So, the naive recursive solution would look below.
'''

def distance(s1, s2):
	if len(s1) == 0 or len(s2) == 0:
		return max(len(s1), len(s2))

	return min(distance(s1[1:], s2) + 1,
		distance(s1, s2[1:]) + 1,
		distance(s1[1:], s2[1:]) if s1[0] == s2[0]
		else distance(s1[1:], s2[1:]) + 1)


print("The edit distance between kitten and sitting is {}".format(distance("kitten", "sitting")))