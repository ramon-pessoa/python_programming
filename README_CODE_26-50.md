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

Go back to [Contents](#contents).
