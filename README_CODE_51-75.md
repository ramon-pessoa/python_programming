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

64. Problem #64 [Hard]: A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.

65. Problem #65 [Easy]: Given a N by M matrix of numbers, print out the matrix in a clockwise spiral. 

For example, given the following matrix:

```
[[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20]]
```

You should print out the following:

```
1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
```

66. Problem #66 [Medium]: Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.

67. Problem #67 [Hard]: Implement an LFU (Least Frequently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

* set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least frequently used item. If there is a tie, then the least recently used key should be removed.
* get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.

68. Problem #68 [Hard]: On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

* (0, 0)
* (1, 2)
* (2, 2)
* (4, 0)

The board would look like this:

```
[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]
```

69. Problem #69 [Easy]: Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.

70. Problem #70 [Easy]: A number is considered perfect if its digits sum up to exactly 10. 

Given a positive integer n, return the n‑th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.

71. Problem #71 [Easy]: Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).

72. Problem #72 [Hard]: In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most frequently-occurring letter along that path. For example, if a path in the graph goes through "ABACA", the value of the path is 3, since there are 3 occurrences of 'A' on the path.

Given a graph with n nodes and m directed edges, return the largest value path of the graph. If the largest value is infinite, then return null.

The graph is represented with a string and an edge list. The i-th character represents the uppercase letter of the i-th node. Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node. Self-edges are possible, as well as multi-edges.

For example, the following input graph:

ABACA

```
[(0, 1),
(0, 2),
(2, 3),
(3, 4)]
```

Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).

The following input graph:

A

```
[(0, 0)]
```

Should return null, since we have an infinite loop.

73. Problem #73 [Easy]: Given the head of a singly linked list, reverse it in-place.

74. Problem #74 [Medium]: Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the i‑th row and j‑th column is (i + 1) * (j + 1) (if 0‑indexed) or i * j (if 1‑indexed).

Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.

For example, given N = 6 and X = 12, you should return 4, since the multiplication table
looks like this:

```
| 1 | 2 | 3 | 4 | 5 | 6 |
| 2 | 4 | 6 | 8 | 10 | 12 |
| 3 | 6 | 9 | 12 | 15 | 18 |
| 4 | 8 | 12 | 16 | 20 | 24 |
| 5 | 10 | 15 | 20 | 25 | 30 |
| 6 | 12 | 18 | 24 | 30 | 36 |
```

75. Problem #75 [Hard]: Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.

Go back to [Contents](#contents).
