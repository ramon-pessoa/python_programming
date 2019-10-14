Some programming examples in Python
===========================

## Contents

1. [Problems from 76 to 100](#problems-from-76-to-100)

2. [All solutions for coding problem](https://github.com/ramonfigueiredopessoa/python_programming#solutions-for-coding-problems)

## Problems from 76 to 100

76. Problem #76 [Hard]: You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically.

For example, given the following table:

```
cba
daf
ghi
```

This is not ordered because of the a in the center. We can remove the second column to make it ordered:

```
ca
df
gi
```

So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

```
abcdef
```

Your function should return 0, since the rows are already ordered (there's only one row).

As another example, given the following table:

```
zyx
wvu
tsr
```

Your function should return 3, since we would need to remove all the columns to order it.

77. Problem #77 [Easy]: Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

78. Problem #78 [Medium]: Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.

79. Problem #79 [Medium]: Given an array of integers, write a function to determine whether the array could become non‑decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non‑decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non‑decreasing array.

80. Problem #80 [Easy]: Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

```
    a
   / \
  b   c
 /
d
```

81. Problem #81 [Easy]: Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {"2": ["a", "b", "c"], 3: ["d", "e", "f"], …} then "23" should return ["ad", "ae", "af", "bd", "be”, "bf", "cd", "ce", "cf"].

82. Problem #82 [Easy]: Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.
For example, given a file with the content "Hello world", three read7() returns "Hello w", "orld" and then "".

83. Problem #83 [Medium]: Invert a binary tree.

For example, given the following tree:

```
    a
   / \
  b   c
 / \  /
d 	e f
```

should become:

```
    a
   / \
  c   b
  \  / \
  f  e d
```

84. Problem #84 [Medium]: Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

```
1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
```

85. Problem #85 [Medium]: Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0.

86. Problem #86 [Medium]: Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.

87. Problem #87 [Hard]: A rule looks like this:

```
A NE B
```

This means point A is located northeast of point B.

```
A SW C
```

means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:

```
A N B
B NE C
C N A
```

does not validate, since A cannot be both north and south of C.

```
A NW B
A N B
```

is considered valid.

88. Problem #88 [Medium]: Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.

89. Problem #89 [Medium]: Determine whether a tree is a valid binary search tree. 

A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.

90. Problem #90 [Medium]: Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).

91. Problem #91 [Easy]: What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?

```
functions = []
for i in range(10):
	functions.append(lambda : i)

for f in functions:
	print(f())
```

92. Problem #92 [Hard]: We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].

93. Problem #93 [Hard]: Given a tree, find the largest tree/subtree that is a BST.

Given a tree, return the size of the largest tree/subtree that is a BST.

94. Problem #94 [Easy]: Given a binary tree of integers, find the maximum path sum between two nodes. The path must go through at least one node, and does not need to go through the root.

95. Problem #95 [Hard]: Given a number represented by a list of digits, find the next greater permutation of a number, in terms of lexicographic ordering. If there is not greater permutation possible, return the permutation with the lowest value/ordering. 

For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return [2,1,3]. The list [3,2,1] should return [1,2,3]. 

Can you perform the operation without allocating extra memory (disregarding the input memory)?

96. Problem #96 [Easy]: Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1], [3,1,2],[3,2,1]].

97. Problem #97 [Medium]: Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.

It should contain the following methods:

* set(key, value, time): sets key to value for t = time.
* get(key, time): gets the key at t = time.

The map should work like this. If we set a key at a particular time, it will maintain that value forever or until it gets set at a later time. In other words, when we get a key at a time, it should return the value that was set for that key set at the most recent time.

Consider the following examples:

```
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
d.get(1, 1) # get key 1 at time 1 should be 1
d.get(1, 3) # get key 1 at time 3 should be 2

d.set(1, 1, 5) # set key 1 to value 1 at time 5
d.get(1, 0) # get key 1 at time 0 should be null
d.get(1, 10) # get key 1 at time 10 should be 1

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
d.get(1, 0) # get key 1 at time 0 should be 2
```

98. Problem #98 [Easy]: Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:

```
[
	['A','B','C','E'],
	['S','F','C','S'],
	['A','D','E','E']
]
```
exists(board, "ABCCED") returns true, 

exists(board, "SEE") returns true,

exists(board, "ABCB") returns false.

99. Problem #99 [Medium]: Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

100. Problem #100 [Easy]: You are in an infinite 2D grid where you can move in any of the 8 directions:

```
(x,y) to
(x+1, y),
(x-1, y),
(x, y+1),
(x, y-1),
(x-1, y-1),
(x+1,y+1),
(x-1,y+1),
(x+1,y-1)
```

You are given a sequence of points and the order in which you need to cover the points. 

Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

```
Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
```

It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).