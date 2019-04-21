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
The solution in unival_tree_o_n_2.py this runs in O(n^2) time. For each node of the tree, we're evaluating each node in its 
subtree again as well. 
We can improve the runtime by starting at the leaves of the tree, and keeping track of the unival subtree count and value 
as we percolate back up. This should evaluate each node only once, making it run in O(n) time.
'''

def count_unival_subtrees(root):
	count, _ = helper(root)
	return count


# Also returns number of univesal subtrees, and whether it is itself a unival subtree.
def helper(root):
	if root is None:
		return 0, True

	left_count, is_left_unival = helper(root.left)
	right_count, is_right_unival = helper(root.right)
	total_count = left_count + right_count

	if is_left_unival and is_right_unival:
		if root.left is not None and root.value != root.left.value:
			return total_count, False
		if root.right is not None and root.value != root.right.value:
			return total_count, False
		return total_count + 1, True
	return total_count, False