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
The solution in make_palindrome_dynamic_programming.py is inefficient due to buildup in the call stack.
We can build a 2D table instead. We'll store, in each index, the shortest palindrome that can be made in 
the substring defined from i to i + j. Then instead of calling ourselves recursively, we'll just look up 
the values in our table:

Because we store a part of our input string in each index of our matrix, the time and space complexity 
for this solution is O(N^3).
'''

def make_palindrome(s):
    if len(s) <= 1:
        return s
    table = [['' for i in range(len(s) + 1)] for j in range(len(s) + 1)]

    for i in range(len(s)):
        table[i][1] = s[i]

    for j in range(2, len(s) + 1):
        for i in range(len(s) - j + 1):
            term = s[i:i + j]
            first, last = term[0], term[-1]
            if first == last:
                table[i][j] = first + table[i + 1][j - 2] + last
            else:
                one = first + table[i + 1][j - 1] + first
                two = last + table[i][j - 1] + last
                if len(one) < len(two):
                    table[i][j] = one
                elif len(one) > len(two):
                    table[i][j] = two
                else:
                    table[i][j] = min(one, two)

    return table[0][-1]
