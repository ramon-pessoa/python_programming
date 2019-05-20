Some programming examples in Python
===========================

## Contents

1. [Problems from 51 to 75](#problems-from-51-to-75)

2. [All solutions for coding problem](https://github.com/ramonfigueiredopessoa/python_programming#solutions-for-coding-problems)

## Problems from 51 to 75

51. Problem #51 [Medium]: Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

	* It should run in O(N) time.

	* Hint: Make sure each one of the 52! permutations of the deck is equally likely.

52. Problem #52 [Hard]: Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

	* set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
	* get(key): gets the value at key. If no such key exists, return null.

	* Each operation should run in O(1) time.

53. Problem #53 [Medium]: Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.

	a. Solution (Python): [queue_using_two_stacks.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/51-75/queue_using_two_stacks.py)

54. Problem #54 [Hard]: Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9. Implement an efficient sudoku solver.

55. Problem #55 [Easy]: Implement a URL shortener with the following methods:

	* shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
	* restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.

	* Hint: What if we enter the same URL twice?

	a. Solution (Python) - Generating a shortened url and store it in a dictionary where the shortened url is the key and the actual url is the value: [url_shortener.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/51-75/url_shortener.py)

	b. Solution (Python) - Create a second dict that maps urls to shortened urls and update that appropriately. When we see a url we've seen before, we can just then just re-use that shortened url: [url_shortener_same_url_twice.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/51-75/url_shortener_same_url_twice.py)

56. Problem #56 [Medium]: Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine whether each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.

	a. Solution (Python) - Solution using backtracking. This solution runs in O(k^N) time and O(k) space, where N is the number of vertices: [colorable.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/51-75/colorable.py)

57. Problem #57 [Medium]: Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.

	* You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

	* For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.

	a. Solution (Python) - Greedy algorithm: [break_string_in_length_of_k.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/51-75/break_string_in_length_of_k.py)

58. Problem #58 [Medium]: An sorted array of integers was rotated an unknown number of times. Given such an array, find the index of the element in the array in faster than linear time.  If the element doesn't exist in the array, return null.

	* For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

	* You can assume all the integers in the array are unique.

	a. Solution (Python) - Solution using an adapted binary search. This solution runs in O(log n): [shifted_array_search.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/51-75/shifted_array_search.py)

59. Problem #59 [hard]: Implement a file syncing algorithm for two computers over a low-bandwidth network. What if we know the files in the two computers are mostly the same?

	a. Solution (Python) - File syncing algorithm: [file_syncing_algorithm.txt](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/51-75/file_syncing_algorithm.txt)

60. Problem #60 [Medium]: Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

	* For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

	* Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.

61. Problem #61 [Medium]: Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

	* Do this faster than the naive method of repeated multiplication.

	* For example, pow(2, 10) should return 1024.

62. Problem #62 [medium]: There is an N by M matrix of zeros. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

	* For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

		* Right, then down
		* Down, then right

	* Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

63. Problem #63 [Easy]: Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

	* For example, given the following matrix and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.

	```
	[['F', 'A', 'C', 'I'],
	 ['O', 'B', 'Q', 'P'],
	 ['A', 'N', 'O', 'B'],
	 ['M', 'A', 'S', 'S']]
	```
	
	a. Solution (Python): [word_search1.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/51-75/word_search1.py)

	b. Solution (Python) - Optimization the previous solution (a): [word_search2.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/51-75/word_search2.py)

	c. Solution (Python) - Optimization the previous solution (b): [word_search3.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/51-75/word_search3.py)

Go back to [Contents](#contents).
