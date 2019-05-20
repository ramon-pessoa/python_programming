Some programming examples in Python
===========================

## Contents

1. [Problems from 1 to 25](#problems-from-1-to-25)

2. [All solutions for coding problem](https://github.com/ramonfigueiredopessoa/python_programming#solutions-for-coding-problems)

## Problems from 1 to 25

1. Problem #1 [Easy]: Given a list of numbers and a number k, return whether any two numbers from the list add up to k. 
	* For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17. 
	* Bonus: Can you do this in one pass?

	a. Solution (Python): [contains_pair_with_sum.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/contains_pair_with_sum.py)

	b. Solution (Python) - Brute force solution. Involve a nested iteration to check for every pair of numbers. This solution is O(N^2): [contains_pair_with_sum_brute_force.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/contains_pair_with_sum_brute_force.py)

	c. Solution (Python) - This solution uses a set to remember the numbers we've seen so far. This would be O(N) since lookups of sets are O(1) each: [contains_pair_with_sum_using_set_linear_time.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/contains_pair_with_sum_using_set_linear_time.py)

	d. Solution (Python) - This solution uses sorting and binary search. Since we run binary search on N elements, this would take O(N log N) with O(1) space: [contains_pair_with_sum_using_sorting_and_binary_search.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/contains_pair_with_sum_using_sorting_and_binary_search.py)


2. Problem #2 [Hard]: Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

	* For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
	* Follow-up: what if you can't use division?

	a. Solution (Python) - Solution without division that takes O(nˆ2): [array_with_the_product_of_all_without_division.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/array_with_the_product_of_all_without_division.py)

	b. Solution (Python) - Solution with division that takes O(n): [array_with_the_product_of_all_with_division.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/array_with_the_product_of_all_with_division.py)

	c. Solution (Python) - Solution without division that takes O(n): [array_with_the_product_of_all_without_division_linear_time.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/array_with_the_product_of_all_without_division_linear_time.py)

3. Problem #3 [Medium]: Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

	* For example, given the following Node class

	```python
	class Node:
	    def __init__(self, val, left=None, right=None):
	        self.val = val
	        self.left = left
	        self.right = right
	```

	The following test should pass:

	```python
	node = Node('root', Node('left', Node('left.left')), Node('right'))
	assert deserialize(serialize(node)).left.left.val == 'left.left'
	```
	a. Solution (Python) - Solution with binary tree: [serialize_deserialize.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/serialize_deserialize.py)


4. Problem #4 [Hard]: Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

	* For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
	* You can modify the input array in-place.

	a. Solution (Python) - Solution in O(N) time and no extra space: [first_missing_positive.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/first_missing_positive.py)

	b. Solution (Python) - Solution in O(N) time and O(N) space: [first_missing_positive_using_set.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/first_missing_positive_using_set.py)

5. Problem #5 [Medium]: cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
	
	* For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

	* Given this implementation of cons:

	```python
	def cons(a, b):
	    def pair(f):
	        return f(a, b)
	    return pair
	```

	* Implement car and cdr.

	a. Solution (Python) - Solution using closures to store data: [car_cdr.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/car_cdr.py)


6. Problem #6 [Hard]: An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

	* If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

	a. Solution (Python) - Solution where add runs in O(1) time and get runs in O(N) time: [xor_linked_list.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/xor_linked_list.py)

7. Problem #7 [Medium]: Problem #7 [Medium]: Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

	* For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

	* You can assume that the messages are decodable. For example, '001' is not allowed.

	a. Solution (Python) - Solution runs in O(2n). However, this solution is not very efficient. Every branch calls itself recursively twice: [num_encodings_O_2n.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/num_encodings_O_2n.py)

	b. Solution (Python) - Solution runs O(n) by using dynamic programming. [num_encodings_O_n.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/num_encondings_O_n.py)

8. Problem #8 [Easy]: A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

	* Given the root to a binary tree, count the number of unival subtrees.

	* For example, the following tree has 5 unival subtrees:

	```
	   0
	  / \
	 1   0
	    / \
	   1   0
	  / \
	 1   1
 	```

	a. Solution (Python) - Solution in O(N^2) time: [unival_tree_o_n_2.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/unival_tree_o_n_2.py)

	b. Solution (Python) - Solution in O(N) time: [unival_tree_o_n.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/unival_tree_o_n.py)

9. Problem #9 [Hard]: Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

	* For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

	* Follow-up: Can you do this in O(N) time and constant space?

	a. Solution (Python) - Solution in O(2^N) time. Recursive calls: [largest_sum_of_non_adjacent_numbers_exponential_time.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/largest_sum_of_non_adjacent_numbers_exponential_time.py) 

	b. Solution (Python) - Solution runs in O(n) time and in O(n) space. Solution using dynamic programming to store: [largest_sum_of_non_adjacent_numbers_linear_time.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/largest_sum_of_non_adjacent_numbers_linear_time.py) 

	c. Solution (Python) - Solution runs in O(n) time and in O(n) space with improvements: [largest_sum_of_non_adjacent_numbers_linear_time_improvement.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/largest_sum_of_non_adjacent_numbers_linear_time_improvement.py)

10. Problem #10 [Medium]: Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

	a. Solution (Python) - While this solution works, we spin off a new thread each time we call delay (the number of threads we use could easily explode): [scheduler_new_thread_each_call.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/scheduler_new_thread_each_call.py) 

	b. Solution (Python) - Solution with dedicated thread to call the functions, and storing the functions we need to call in some data structure: [scheduler_dedicated_thread.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/scheduler_dedicated_thread.py)

11. Problem #11 [Medium]: Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

	* For example, given the query string 'de' and the set of strings [dog, deer, deal], return [deer, deal].

	* Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

	a. Solution (Python) - This solution runs in O(N) time, where N is the number of words in the dictionary: [autocomplete.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/autocomplete.py) 

	b. Solution (Python) - More efficient implementation using a data structure known as a trie: [autocomplete_using_trie.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/autocomplete_using_trie.py) 

12. Problem #12 [Hard]: There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

	* For example, if N is 4, then there are 5 unique ways:

	```
	1, 1, 1, 1
	2, 1, 1
	1, 2, 1
	1, 1, 2
	2, 2
	```

	* What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

	a. Solution (Python) - Solution using recursive Fibonacci. This solution runs in O(2 ^ N) time: [staircase_recursion_fibonacci.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/staircase_recursion_fibonacci.py) 

	b. Solution (Python) - Solution using iterative Fibonacci: [staircase_iterative_fibonacci.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/staircase_iterative_fibonacci.py) 

	c. Solution (Python) - Solution that works if you can take a number of steps from the set X. This solution is very slow (O(|X| ^ N)) since we are repeating computations: [staircase_x_steps.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/staircase_x_steps.py) 

	d. Solution (Python) - Solution that works if you can take a number of steps from the set X. Solution using dynamic programming to speed it up: [staircase_dynamic_programming.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/staircase_dynamic_programming.py) 

13. Problem #13 [Hard]: Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

	* For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

	a. Solution (Python) - Brute force solution. This solution runs in O(n^2 + k) time, since we use n^2 to generate each possible substring, and then take k to check each character: [longest_substring_with_k_distinct_characters_brute_force_solution.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/longest_substring_with_k_distinct_characters_brute_force_solution.py)

	b. Solution (Python) - Solution using dictionary. This solution runs in O(n * k) time and O(k) space: [longest_substring_with_k_distinct_characters_using_dictionary.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/longest_substring_with_k_distinct_characters_using_dictionary.py)

14. Problem #14 [Medium]: The area of a circle is defined as pi r ^ 2. Estimate pi to 3 decimal places using a Monte Carlo method.

	* Hint: The basic equation of a circle is x^2 + y^2 = r^2.

	a. Solution (Python) - Solution using a Monte Carlo method: [estimate_pi.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/estimate_pi.py)

15. Problem #15 [Medium]: Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

	a. Solution (Python) - Solution using reservoir sampling: [pick_random_element.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/pick_random_element.py)

16. Problem #16 [Easy]: You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

	* record(order_id): adds the order_id to the log
	* get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

	* You should be as efficient with time and space as possible.

	a. Solution (Python) - Solution initializing an array to have size N, and index it in constant time. Record takes O(N) time: [log_record_get_last_linear_time.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/log_record_get_last_linear_time.py)

	b. Solution (Python) - Solution using ring buffer or circular buffer. Both record and get_last should take constant time: [log_record_get_last_constant_time.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/log_record_get_last_constant_time.py)

19. Problem #19 [Medium]: A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color. Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

	a. Solution (Python): Solution using dynamic programming. [build_houses_using_dynamic_programming.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/build_houses_using_dynamic_programming.py)

		* Solution 1 (build_houses1): This solution runs in O(N * K^2) time and O(N * K) space. 

		* Solution 2 (build_houses2): This solution is only using O(K) space.

		* Solution 3 (build_houses3): This solution is only O(N * K) and the space complexity is O(1).

20. Problem #20 [Easy]: Given two linked lists that intersect at some point, find the intersection node. The lists are non-cyclical.

	* For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with calue 8.

	* In this example, assume nodes with the same value are exact same node objects.

	Do this in O(M + N) time

	a. Solution (Python) - Solution by finding the difference between the two, and then keep two pointers at the head of each list. This solution runs in O(M + N) time: [find_intersecting_node.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/find_intersecting_node.py)

21. Problem #21 [Easy]: Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

	* For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

	a. Solution (Python) - Solution checking each interval pairwise. This solution would take O(n^2) time: [max_overlapping_quadratic_time.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/max_overlapping_quadratic_time.py) 

	b. Solution (Python) - Solution that extract the start times and end times of all the intervals and sort them. This solution runs in O(n log n) time, since we have to sort the intervals: [max_overlapping_logarithmic_time.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/max_overlapping_logarithmic_time.py) 

22. Problem #22 [Medium]: Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

	* For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

	* Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].


	a. Solution (Python) - Solution using backtracking. This will run in O(2^N) time: [find_sentence_backtracking.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/find_sentence_backtracking.py)

	b. Solution (Python) - Solution using dynamic programming. This will run in runs in O(N^2) time and O(N) space: [find_sentence_dynamic_programming.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/1-25/find_sentence_dynamic_programming.py)

Go back to [Contents](#contents).
