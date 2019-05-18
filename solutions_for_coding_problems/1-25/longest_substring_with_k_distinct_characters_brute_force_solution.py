'''
Problem #13 [Hard]: Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
'''


'''
The most obvious brute force solution here is to simply try every possible substring of the string and check whether it contains at most k distinct characters. 

If it does and it is greater than the current longest valid substring, then update the current one. 

This takes O(n^2 * k) time, since we use n2 to generate each possible substring, and then take k to check each character.
'''

def longest_substring_with_k_distinct_characters(s, k):
	current_longest_substring = ''
	for i in range(len(s)):
		for j in range(i + 1, len(s) + 1):
			substring = s[i:j]
			if len(set(substring)) <= k and len(substring) > len(current_longest_substring):
				current_longest_substring = substring

	return len(current_longest_substring)


n = 2
s = "abcba"
print("Given an integer {0} and the string {1}, the length of the longest substring that contains at most k distinct characters is {2}".format(n, s, longest_substring_with_k_distinct_characters("abcba", 2)))
