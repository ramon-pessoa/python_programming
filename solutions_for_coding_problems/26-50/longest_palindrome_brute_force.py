'''
Problem #46 [Hard]: Given a string, find the longest palindromic contiguous substring. 
If there are more than one with the maximum length, return any one. 

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". 
The longest palindromic substring of "bananas" is "anana".
'''

'''
We can compute the longest palindromic contiguous substring in O(N^3) using brute force. 
We can just iterate over each substring of the array and check if it's a palindrome.
'''

def is_palindrome(s):
	return s[::-1] == s


def longest_palindrome(s):
	longest = ''
	for i in range(len(s) - 1):
		for j in range(1, len(s)):
			substring = s[i:j]
			if is_palindrome(substring) and len(substring) > len(longest):
				longest = substring
	return longest


print("The longest palindromic contiguous substring of aabcdcb is %s" % longest_palindrome("aabcdcb"))
print("The longest palindromic contiguous substring of bananas is %s" % longest_palindrome("bananas"))