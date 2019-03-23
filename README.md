Some programming examples in Python
===========================

## Contents
1. [Reading and writing XML files in Python](#reading-and-writing-xml-files-in-python)

2. [Data structures algorithms](#data-structures-algorithms)

3. [Solutions for coding problems](#solutions-for-coding-problems)

## Reading and writing XML files in Python

1. Reading XML Documents

	a. Solution (Python) using minidom: [minidom_reading_xml_in_python.py](https://github.com/ramon-pessoa/python_programming/blob/master/reading_and_writing_xml_files_in_python/minidom_reading_xml_in_python.py)

	b. Solution (Python) using ElementTree: [etree_reading_xml_in_python.py](https://github.com/ramon-pessoa/python_programming/blob/master/reading_and_writing_xml_files_in_python/etree_reading_xml_in_python.py)

2. Counting the Elements of an XML Document

	a. Solution (Python) using minidom: [minidom_counting_elements_in_xml.py](https://github.com/ramon-pessoa/python_programming/blob/master/reading_and_writing_xml_files_in_python/minidom_counting_elements_in_xml.py)

	b. Solution (Python) using ElementTree: [etree_counting_elements_in_xml.py](https://github.com/ramon-pessoa/python_programming/blob/master/reading_and_writing_xml_files_in_python/etree_counting_elements_in_xml.py)

3. Writing XML Documents

	a. Solution (Python) using ElementTree: [writing_xml_in_python.py](https://github.com/ramon-pessoa/python_programming/blob/master/reading_and_writing_xml_files_in_python/writing_xml_in_python.py)

4. Finding XML Elements

	a. Solution (Python) using ElementTree: [finding_xml_elements.py](https://github.com/ramon-pessoa/python_programming/blob/master/reading_and_writing_xml_files_in_python/finding_xml_elements.py)

5. Modifying XML Elements

	a. Solution (Python) using ElementTree: [modifying_xml_elements.py](https://github.com/ramon-pessoa/python_programming/blob/master/reading_and_writing_xml_files_in_python/modifying_xml_elements.py)

6. Creating XML Sub-Elements

	a. Solution (Python) using ElementTree: [creating_xml_sub_elements.py](https://github.com/ramon-pessoa/python_programming/blob/master/reading_and_writing_xml_files_in_python/creating_xml_sub_elements.py)

7. Deleting XML Elements

	a. Solution (Python) using ElementTree - deleting an attribute: [deleting_xml_attribute.py](https://github.com/ramon-pessoa/python_programming/blob/master/reading_and_writing_xml_files_in_python/deleting_xml_attribute.py)

	b. Solution (Python) using ElementTree - deleting one sub-element: [deleting_xml_sub_element.py](https://github.com/ramon-pessoa/python_programming/blob/master/reading_and_writing_xml_files_in_python/deleting_xml_sub_element.py)

	c. Solution (Python) using ElementTree - deleting all sub-elements: [deleting_all_xml_sub_elements.py](https://github.com/ramon-pessoa/python_programming/blob/master/reading_and_writing_xml_files_in_python/deleting_all_xml_sub_elements.py)

## Data structures algorithms

1. Binary search: [binary_search.py](https://github.com/ramon-pessoa/python_programming/blob/master/data_structures_algorithms/binary_search.py)

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

Go back to [Contents](#contents).