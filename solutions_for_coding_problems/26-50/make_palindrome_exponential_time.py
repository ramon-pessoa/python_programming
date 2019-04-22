'''
Problem #34 [Medium]: Given a string, find the palindrome that can be made by inserting the fewest number of characters as 
possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the 
lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the 
smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three 
letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
'''

'''
Notice that whenever we add a character, it should ideally match the one on the other side of the string. 
We can use the following recurrence to solve this problem:

* If s is already a palindrome, then just return s -- it's already the shortest palindrome we can make

* If the first character of s (let's call it a) is the same as the last, then return a + make_palindrome(s[1:-1]) + a

* If the first character of s is different from the last (let's call this b), then return the minimum between:
a + make_palindrome(s[1:]) + a
b + make_palindrome(s[:-1]) + b or the lexicographically earliest one if their lengths are equal.

So a naive recursive solution might look like below.

Recall that the min of two strings in python will return the lexicographically earliest one!

However, this algorithm runs in O(2^N) time.
'''

def is_palindrome(s):
	return s == s[::-1]

def make_palindrome(s):
	if is_palindrome(s):
		return s

	if s[0] == s[-1]:
		return s[0] + make_palindrome(s[1:-1]) + s[-1]
	else:
		one = s[0] + make_palindrome(s[1:]) + s[0]
		two = s[-1] + make_palindrome(s[:-1]) + s[-1]
		if len(one) < len(two):
			return one
		elif len(one) > len(two):
			return two
		else:
			return min(one, two)