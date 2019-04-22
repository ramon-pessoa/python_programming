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
The solution in make_palindrome_exponential_time.py runs in O(2^N) time, since we could potentially make two recursive 
calls each time. We can speed up using dynamic programming, as usual. We can either memoize our results so that we don't 
duplicate any work, or use a table and do bottom-up programming.

Let's start with memoization. We can keep a cache and store all our results when we compute them in the cache. If we come 
across a string we've seen before, then we just need to look it up in the cache.

However, this is inefficient due to buildup in the call stack.
'''

cache = {}

def is_palindrome(s):
	return s == s[::-1]

def make_palindrome(s):
	if s in cache:
		return cache[s]

	if is_palindrome(s):
		cache[s] = s
		return s
	if s[0] == s[-1]:
		result = s[0] + make_palindrome(s[1:-1]) + s[-1]
		cache[s] = result
		return result
	else:
		one = s[0] + make_palindrome(s[1:]) + s[0]
		two = s[-1] + make_palindrome(s[:-1]) + s[-1]
		cache[s] = min(one, two)
		return min(one, two)
