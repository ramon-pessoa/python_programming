Some programming examples in Python
===========================

## Contents

1. [Solutions for coding problems](#solutions-for-coding-problems)

## Solutions for coding problems

27. Problem #27 [Easy]: Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

	* For example, given the string "([])[]({})", you should return true.
	
	* Given the string "([)]" or "((()", you should return false. 

	a. Solution (Python) [balance.py]. Solution using Stack. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/balance.py)

29. Problem #29 [Easy]: Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

	* Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

	a. Solution (Python) [run_length_encoding.py]. Run-length encoding implementation. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/run_length_encoding.py)

31. Problem #31 [Easy]: The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

	* Given two strings, compute the edit distance between them.

	a. Solution (Python) [edit_distance_with_recursion.py]. Solution using recursion. This runs very slowly due to repeated subcomputations. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/edit_distance_with_recursion.py)

	b. Solution (Python) [edit_distance_dinamic_programming.py]. Solution using dinamic programming. This solution takes O(N * M) time and space, where N and M are the lengths of the strings. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/edit_distance_dinamic_programming.py) 

32. Problem #32 [Hard]: Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.

	* There are no transaction costs and you can trade fractional quantities.

	a. Solution (Python) [arbitrage.py]. Solution using the Bellman-Ford algorithm (graph modeling). The solution runs in O(N^3) time. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/arbitrage.py) 

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

35. Problem #35 [Hard]: Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

	* Do this in linear time and in‑place.

	* For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

	a. Solution (Python) [partition.py]. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/partition.py) 

36. Problem #36 [Medium]: Given the root to a binary search tree, find the second largest node in the tree.
	
	a. Solution (Python) [second_largest.py]. Solution using a reverse in-order traversal. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/second_largest.py) 
	
37. Problem #37 [Easy]: The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

	* For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

	* You may also use a list or array to represent a set.

	a. Solution (Python) [power_set.py]. This solution runs in O(2^N) time and space (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/power_set.py) 

37. Problem #37 [Medium]: Given the root to a binary search tree, find the second largest node in the tree.

	a. Solution (Python) [second_largest.py]. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/second_largest.py)

38. Problem #38 [Hard]: You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.

	a. Solution (Python) [n_queens.py]. We show a solution for the problem of N Queens using backtracking technique. Note: If we solve this problem using brute force, we would quickly find out that it would be prohibitively expensive. That's factorial in runtime! (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/n_queens.py)


39. Problem #39 [Medium]: Conway's Game of Life takes place on an infinite two‑dimensional board of square cells. 

	* Each cell is either dead or alive, and at each tick, the following rules apply:

		- Any live cell with less than two live neighbours dies.
		- Any live cell with two or three live neighbours remains living.
		- Any live cell with more than three live neighbours dies.
		- Any dead cell with exactly three live neighbours becomes a live cell.

	* A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

	* Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top‑leftmost live cell to bottom‑rightmost live cell.

	* You can represent a live cell with an asterisk (asterisk symbol) and a dead cell with a dot (.).

	a. Solution (Python) [game_of_life.py]. Solution for Conway's Game of Life. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/game_of_life.py) 

40. Problem #40 [Hard]: Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

	* For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
	* Do this in O(N) time and O(1) space.

	a. Solution (Python) [find_unique.py]. Solution in linear time and space. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/find_unique.py) 

41. Problem #41 [Medium]: Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

	* For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

	* Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

	* Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.

	a. Solution (Python) [get_itinerary.py]. Backtracking solution (similar to the solution for the N queens problem) (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/get_itinerary.py)

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

	a. Solution (Python) [evaluate_arithmetic_expression.py]: Solution using binary tree and recursion. This solution runs in O(N) time and space. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/evaluate_arithmetic_expression.py)

55. Problem #55 [Easy]: Implement a URL shortener with the following methods:

	* shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
	* restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.

	* Hint: What if we enter the same URL twice?

	a. Solution (Python) [url_shortener.py]: Generating a shortened url and store it in a dictionary where the shortened url is the key and the actual url is the value. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/url_shortener.py)

	b. Solution (Python) [url_shortener_same_url_twice.py]: Create a second dict that maps urls to shortened urls and update that appropriately. When we see a url we've seen before, we can just then just re-use that shortened url. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/26-50/url_shortener_same_url_twice.py)

Go back to [Contents](#contents).
