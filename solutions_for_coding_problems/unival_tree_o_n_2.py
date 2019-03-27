'''
Problem #8 [Easy]: A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''

'''
To start off, we should go through some examples.

  a
 / \
a   a
    /\
   a  a
       \
        A
This tree has 3 unival subtrees: the two 'a' leaves, and the one 'A' leaf. 
The 'A' leaf causes all its parents to not be counted as a unival tree.

  a
 / \
c   b
    /\
   b  b
        \
         b

This tree has 5 unival subtrees: the leaf at 'c', and every 'b'.

We can start off by first writing a function that checks whether a tree is unival or not. 
Then, perhaps we could use this to count up all the nodes in the tree.

To check whether a tree is a unival tree, we must check that every node in the tree has the same value. 
To start off, we could define an is_unival function that takes in a root to a tree. 
We would do this recursively with a helper function. 
Recall that a leaf qualifies as a unival tree.

And then our function that counts the number of subtrees could simply use the function: count_unival_subtrees

However, this runs in O(n^2) time. For each node of the tree, we're evaluating each node in its subtree again as well. 
We can improve the runtime by starting at the leaves of the tree, and keeping track of the unival subtree count and value 
as we percolate back up. This should evaluate each node only once, making it run in O(n) time.
'''

def is_unival(root):
	return unival_helper(root, root.value)

def unival_helper(root, value):
	if root is None:
		return True
	if root.value == value:
		return unival_helper(root.helper, value) and unival_helper(root.right, value)
	return False

def count_unival_subtrees(root):
	if root is None:
		return 0
	left = count_unival_subtrees(root.left)
	right = count_unival_subtrees(root.right)
	return 1 + left + right if is_unival(root) else left + right