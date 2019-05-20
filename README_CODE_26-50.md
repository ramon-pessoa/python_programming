Some programming examples in Python
===========================

## Contents

1. [Problems from 26 to 50](#problems-from-26-to-50)

2. [All solutions for coding problem](https://github.com/ramonfigueiredopessoa/python_programming#solutions-for-coding-problems)

## Problems from 26 to 50

26. Problem #26 [Medium]: Given a singly linked list and an integer k, remove the k th last element from the list. k is guaranteed to be smaller than the length of the list.

	* The list is very long, so making more than one pass is prohibitively expensive.

	* Do this in constant space and in one pass.

	a. Solution (Python) - Solution that only makes one pass and is constant time: [remove_kth_from_linked_list.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/remove_kth_from_linked_list.py)

27. Problem #27 [Easy]: Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

	* For example, given the string "([])[]({})", you should return true.
	
	* Given the string "([)]" or "((()", you should return false. 

	a. Solution (Python) - Solution using Stack: [balance.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/balance.py)

28. Problem #28 [Medium]: Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

	* More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

	* If you can only fit one word on a line, then you should pad the right-hand side with spaces.

	* Each word is guaranteed not to be longer than k.

	* For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

	```
	["the  quick brown", # 1 extra space on the left
	"fox  jumps  over", # 2 extra spaces distributed evenly
	"the   lazy   dog"] # 4 extra spaces distributed evenly
	```
	
29. Problem #29 [Easy]: Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

	* Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

	a. Solution (Python) - Run-length encoding implementation: [run_length_encoding.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/run_length_encoding.py)

30. Problem #30 [Medium]: You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up. Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

	* For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

	* Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.

31. Problem #31 [Easy]: The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

	* Given two strings, compute the edit distance between them.

	a. Solution (Python) - Solution using recursion. This runs very slowly due to repeated subcomputations: [edit_distance_with_recursion.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/edit_distance_with_recursion.py)

	b. Solution (Python) - Solution using dinamic programming. This solution takes O(N * M) time and space, where N and M are the lengths of the strings: [edit_distance_dinamic_programming.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/edit_distance_dinamic_programming.py) 

32. Problem #32 [Hard]: Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.

	* There are no transaction costs and you can trade fractional quantities.

	a. Solution (Python) - Solution using the Bellman-Ford algorithm (graph modeling). The solution runs in O(N^3) time: [arbitrage.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/arbitrage.py) 

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

	a. Solution (Python) - The solution uses two heaps: a min-heap and a max-heap. This runs in O(N) space and in O(N log N) time: [print_median.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/print_median.py) 

34. Problem #34 [Medium]: Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

	* For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

	* As another example, given the string "google", you should return "elgoogle".

	a. Solution (Python) - Naive recursive solution. This solution runs in O(2^N) time: [make_palindrome_exponential_time.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/make_palindrome_exponential_time.py) 

	b. Solution (Python) - Dynamic programming solution. This solution is inefficient due to buildup in the call stack: [make_palindrome_dynamic_programming.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/make_palindrome_dynamic_programming.py) 

	c. Solution (Python) - A solution that builds a 2D table. This solution stores a part of the input string in each index of a matrix, therefore the time and space complexity for this solution is O(N^3): [make_palindrome_cubic_time.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/make_palindrome_cubic_time.py) 

35. Problem #35 [Hard]: Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

	* Do this in linear time and in‑place.

	* For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

	a. Solution (Python): [partition.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/partition.py) 

36. Problem #36 [Medium]: Given the root to a binary search tree, find the second largest node in the tree.
	
	a. Solution (Python) - Solution using a reverse in-order traversal: [second_largest.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/second_largest.py) 
	
37. Problem #37 [Easy]: The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

	* For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

	* You may also use a list or array to represent a set.

	a. Solution (Python) - This solution runs in O(2^N) time and space: [power_set.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/power_set.py) 

38. Problem #38 [Hard]: You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.

	a. Solution (Python) - Solution for the problem of N Queens using backtracking technique. Note: If we solve this problem using brute force, we would quickly find out that it would be prohibitively expensive. That's factorial in runtime: [n_queens.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/n_queens.py)


39. Problem #39 [Medium]: Conway's Game of Life takes place on an infinite two‑dimensional board of square cells. 

	* Each cell is either dead or alive, and at each tick, the following rules apply:

		- Any live cell with less than two live neighbours dies.
		- Any live cell with two or three live neighbours remains living.
		- Any live cell with more than three live neighbours dies.
		- Any dead cell with exactly three live neighbours becomes a live cell.

	* A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

	* Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top‑leftmost live cell to bottom‑rightmost live cell.

	* You can represent a live cell with an asterisk (asterisk symbol) and a dead cell with a dot (.).

	a. Solution (Python) - Solution for Conway's Game of Life: [game_of_life.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/game_of_life.py) 

40. Problem #40 [Hard]: Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

	* For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
	* Do this in O(N) time and O(1) space.

	a. Solution (Python) - Solution in linear time and space: [find_unique.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/find_unique.py) 

41. Problem #41 [Medium]: Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

	* For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

	* Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

	* Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.

	a. Solution (Python) - Backtracking solution (similar to the solution for the N queens problem): [get_itinerary.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/get_itinerary.py)

42. Problem #42 [Hard]: Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

	* Integers can appear more than once in the list. You may assume all numbers in the list are positive.

	* For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

43. Problem #43 [Easy]: Implement a stack that has the following methods:
	* push(val), which pushes an element onto the stack
	* pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
	* max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

		* Each method should run in constant time.

	a. Solution (Python) - Max Stack with methods that runs in constant time: [max_stack.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/max_stack.py)

44. Problem #44 [Medium]: We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

	* Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

	* You may assume each element in the array is distinct.

	* For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion: (5, 4), (5, 3), (5, 2), (5, 1), (4, 3), (4, 2), (4, 1), (3, 2), (3, 1), (2, 1).

	a. Solution (Python) - Brute force solution that runs in O(N^2) time: [count_inversions_brute_force_solution.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/count_inversions_brute_force_solution.py)

	a. Solution (Python) - Divide-and-conquer solution that runs in O(N log N) time: [count_inversions_divide_and_conquer_solution.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/count_inversions_divide_and_conquer_solution.py)

45. Problem #45 [Easy]: Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).
	
	a. Solution (Python) - Solution by computing rand5() twice: [rand7.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/rand7.py)

46. Problem #46 [Hard]: Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one. 

	* For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
	
	a. Solution (Python) - Brute force solution. This solution runs in O(N^3) time: [longest_palindrome_brute_force.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/longest_palindrome_brute_force.py)

	b. Solution (Python) - Dynamic programming solution. This solution runs in O(N^2) time and space: [longest_palindrome_dynamic_programming.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/longest_palindrome_dynamic_programming.py)

47. Problem #47 [Easy]: Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

	* For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

	a. Solution (Python) - Brute force solution. This solution runs in O(N^2) time: [buy_and_sell_brute_force.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/buy_and_sell_brute_force.py)

	b. Solution (Python) - Linear time solution. This solution runs in O(N) time and O(1) space: [buy_and_sell_linear_time.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/buy_and_sell_linear_time.py)

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

	a. Solution (Python) - Recursive solution: [reconstruct.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/reconstruct.py)

49. Problem #49 [Medium]: Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

	* For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

	* Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

	* Do this in O(N) time.

	a. Solution (Python) - Brute force solution. This solution run in O(N^3) time: [max_subarray_sum_brute_force_solution.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/max_subarray_sum_brute_force_solution.py)

	b. Solution (Python) - Solution using Kadane's algorithm. This algoritm runs in O(N) time and O(1) space: [max_subarray_sum_using_kadane_algorithm.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/max_subarray_sum_using_kadane_algorithm.py)

50. Problem #50 [Easy]: Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'. 

	* Given the root to such a tree, write a function to evaluate it.

	* For example, given the following tree:

	```
	   *
	  / \
	 +   +
	/ \ / \
	3 2 4 5
	```

	* You should return 45, as it is (3 + 2) * (4 + 5).

	a. Solution (Python) - Solution using binary tree and recursion. This solution runs in O(N) time and space: [evaluate_arithmetic_expression.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/evaluate_arithmetic_expression.py)

Go back to [Contents](#contents).
