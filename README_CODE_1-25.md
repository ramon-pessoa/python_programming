Some programming examples in Python
===========================

## Contents

1. [Solutions for coding problems](#solutions-for-coding-problems)

## Solutions for coding problems

1. Problem #1 [Easy]: Given a list of numbers and a number k, return whether any two numbers from the list add up to k. 
	* For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17. 
	* Bonus: Can you do this in one pass?

	a. Solution (Python) [contains_pair_with_sum.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/contains_pair_with_sum.py)

	b. Solution (Python) [contains_pair_with_sum_brute_force.py]: Brute force solution. Involve a nested iteration to check for every pair of numbers. This solution is O(N^2). (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/contains_pair_with_sum_brute_force.py)

	c. Solution (Python) [contains_pair_with_sum_using_set_linear_time.py]: This solution uses a set to remember the numbers we've seen so far. This would be O(N) since lookups of sets are O(1) each. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/contains_pair_with_sum_using_set_linear_time.py)

	d. Solution (Python) [contains_pair_with_sum_using_sorting_and_binary_search.py]: This solution uses sorting and binary search. Since we run binary search on N elements, this would take O(N log N) with O(1) space. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/contains_pair_with_sum_using_sorting_and_binary_search.py)


2. Problem #2 [Hard]: Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

	* For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
	* Follow-up: what if you can't use division?

	a. Solution (Python) [array_with_the_product_of_all_without_division.py]. Solution without division that takes O(nˆ2). (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/array_with_the_product_of_all_without_division.py)

	b. Solution (Python) [array_with_the_product_of_all_with_division.py]. Solution with division that takes O(n). (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/array_with_the_product_of_all_with_division.py)

	c. Solution (Python) [array_with_the_product_of_all_without_division_linear_time.py]. Solution without division that takes O(n). (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/array_with_the_product_of_all_without_division_linear_time.py)

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
	a. Solution (Python) [serialize_deserialize.py]. Solution with binary tree. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/serialize_deserialize.py)


4. Problem #4 [Hard]: Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

	* For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
	* You can modify the input array in-place.

	a. Solution (Python) [first_missing_positive.py]. Solution in O(N) time and no extra space. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/first_missing_positive.py)

	b. Solution (Python) [first_missing_positive_using_set.py]. Solution in O(N) time and O(N) space. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/first_missing_positive_using_set.py)

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

	a. Solution (Python) [car_cdr.py]. Solution using closures to store data. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/car_cdr.py)


6. Problem #6 [Hard]: An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

	* If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

	a. Solution (Python) [xor_linked_list.py]. Solution where add runs in O(1) time and get runs in O(N) time. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/xor_linked_list.py)

7. Problem #7 [Medium]: Problem #7 [Medium]: Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

	* For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

	* You can assume that the messages are decodable. For example, '001' is not allowed.

	a. Solution (Python) [num_encodings_O_2n.py]. Solution runs in O(2n). However, this solution is not very efficient. Every branch calls itself recursively twice. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/num_encodings_O_2n.py)

	b. Solution (Python) [num_encodings_O_n.py]. Solution runs O(n) by using dynamic programming. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/num_encondings_O_n.py)

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

	a. Solution (Python) [unival_tree_o_n_2.py]. Solution in O(N^2) time. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/unival_tree_o_n_2.py)

	b. Solution (Python) [unival_tree_o_n.py]. Solution in O(N) time. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/unival_tree_o_n.py)

9. Problem #9 [Hard]: Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

	* For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

	* Follow-up: Can you do this in O(N) time and constant space?

	a. Solution (Python) [largest_sum_of_non_adjacent_numbers_exponential_time.py]. Solution in O(2^N) time - recursive calls. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/largest_sum_of_non_adjacent_numbers_exponential_time.py) 

	b. Solution (Python) [largest_sum_of_non_adjacent_numbers_linear_time.py]. Solution runs in O(n) time and in O(n) space - using dynamic programming to store. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/largest_sum_of_non_adjacent_numbers_linear_time.py) 

	c. Solution (Python) [largest_sum_of_non_adjacent_numbers_linear_time_improvement.py]. Solution runs in O(n) time and in O(n) space with improvements. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/largest_sum_of_non_adjacent_numbers_linear_time_improvement.py)

10. Problem #10 [Medium]: Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

	a. Solution (Python) [scheduler_new_thread_each_call.py]. While this solution works, we spin off a new thread each time we call delay (the number of threads we use could easily explode). (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/scheduler_new_thread_each_call.py) 

	b. Solution (Python) [scheduler_dedicated_thread.py]. Solution with dedicated thread to call the functions, and storing the functions we need to call in some data structure. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/scheduler_dedicated_thread.py)

11. Problem #11 [Medium]: Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

	* For example, given the query string 'de' and the set of strings [dog, deer, deal], return [deer, deal].

	* Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

	a. Solution (Python) [autocomplete.py]. This solution runs in O(N) time, where N is the number of words in the dictionary. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/autocomplete.py) 

	b. Solution (Python) [autocomplete_using_trie.py]. More efficient implementation using a data structure known as a trie. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/autocomplete_using_trie.py) 

Go back to [Contents](#contents).
