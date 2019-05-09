Some programming examples in Python
===========================

## Contents

1. [Solutions for coding problems](#solutions-for-coding-problems)

## Solutions for coding problems

33. Problem #33 [Easy]: Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

	* Recall that the median of an even-numbered list is the average of the two middle numbers.

	* For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

	```
	2
	1.5
	2
	3.5
	2
	2
	2
	```

	a. Solution (Python) [print_median.py]. The solution uses two heaps: a min-heap and a max-heap. This runs in O(N) space and in O(N log N) time. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/print_median.py) 

34. Problem #34 [Medium]: Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

	* For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

	* As another example, given the string "google", you should return "elgoogle".

	a. Solution (Python) [make_palindrome_exponential_time.py]. Naive recursive solution. This solution runs in O(2^N) time. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/make_palindrome_exponential_time.py) 

	b. Solution (Python) [make_palindrome_dynamic_programming.py]. Dynamic programming solution. This solution is inefficient due to buildup in the call stack. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/make_palindrome_dynamic_programming.py) 

	c. Solution (Python) [make_palindrome_cubic_time.py]. A solution that builds a 2D table. This solution stores a part of the input string in each index of a matrix, therefore the time and space complexity for this solution is O(N^3). (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/make_palindrome_cubic_time.py) 

42. Problem #42 [Hard]: Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

	* Integers can appear more than once in the list. You may assume all numbers in the list are positive.

	* For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
	

43. Problem #43 [Easy]: Implement a stack that has the following methods:
	* push(val), which pushes an element onto the stack
	* pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
	* max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

		* Each method should run in constant time.

	a. Solution (Python) [max_stack.py]. Max Stack with methods that runs in constant time. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/max_stack.py)

44. Problem #44 [Medium]: We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

	* Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

	* You may assume each element in the array is distinct.

	* For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion: (5, 4), (5, 3), (5, 2), (5, 1), (4, 3), (4, 2), (4, 1), (3, 2), (3, 1), (2, 1).

	a. Solution (Python) [count_inversions_brute_force_solution.py]. Brute force solution that runs in O(N^2) time. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/count_inversions_brute_force_solution.py)

	a. Solution (Python) [count_inversions_divide_and_conquer_solution.py]. Divide-and-conquer solution that runs in O(N log N) time. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/count_inversions_divide_and_conquer_solution.py)

45. Problem #45 [Easy]: Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).
	
	a. Solution (Python) [rand7.py]: Solution by computing rand5() twice. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/rand7.py)

46. Problem #46 [Hard]: Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one. 

	* For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
	
	a. Solution (Python) [longest_palindrome_brute_force.py]: Brute force solution. This solution runs in O(N^3) time. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/longest_palindrome_brute_force.py)

	b. Solution (Python) [longest_palindrome_dynamic_programming.py]: Dynamic programming solution. This solution runs in O(N^2) time and space. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/longest_palindrome_dynamic_programming.py)

47. Problem #47 [Easy]: Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

	* For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

	a. Solution (Python) [buy_and_sell_brute_force.py]: Brute force solution. This solution runs in O(N^2) time. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/buy_and_sell_brute_force.py)

	b. Solution (Python) [buy_and_sell_linear_time.py]: Linear time solution. This solution runs in O(N) time and O(1) space. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/buy_and_sell_linear_time.py)

48. Problem #48 [Medium]: Given pre‑order and in‑order traversals of a binary tree, write a function to reconstruct the tree.

	* For example, given the following preorder traversal: [a, b, d, e, c, f, g]
	* And the following inorder traversal: [d, b, e, a, f, c, g]

	* You should return the following tree:

	```
	   a
	  / \
	 b   c
	/ \ / \
	d e f g
	```

	a. Solution (Python) [reconstruct.py]: Recursive solution (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/reconstruct.py)

Go back to [Contents](#contents).
