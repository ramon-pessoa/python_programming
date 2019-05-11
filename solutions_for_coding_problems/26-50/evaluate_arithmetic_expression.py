'''
Problem #50 [Easy]: Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'. 

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

   *
  / \
 +   +
/ \ / \
3 2 4 5

You should return 45, as it is (3 + 2) * (4 + 5).
'''

'''
This problem should be straightforward from the definition. It will be recursive.
We check the value of the root node.
If it's one of our arithmetic operators, then we take the evaluated value of our node's children and apply the operator on them.
If it's not an arithmetic operator, it has to be a raw number, so we can just return that.
'''

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __str__(self):
		return "Node(val = {0}, left = {1}, right = {2})".format(self.val, self.left, self.right)

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evaluate(root):
	if root.val == PLUS:
		return evaluate(root.left) + evaluate(root.right)
	elif root.val == MINUS:
		return evaluate(root.left) - evaluate(root.right)
	elif root.val == TIMES:
		return evaluate(root.left) * evaluate(root.right)
	elif root.val == DIVIDE:
		return evaluate(root.left) / evaluate(root.right)
	else:
		return root.val

'''
   *
  / \
 +   +
/ \ / \
3 2 4 5
'''

nodeList = []

n7 = Node(5, None, None)
n6 = Node(4, None, None)
n5 = Node("+", n6, n7)
n4 = Node(2, None, None)
n3 = Node(3, None, None)
n2 = Node("+", n3, n4)
n1 = Node("*", n2, n5)

nodeList.append(n1);
nodeList.append(n2);
nodeList.append(n3);
nodeList.append(n4);
nodeList.append(n5);
nodeList.append(n6);
nodeList.append(n7);

print("Input tree:")
for n in nodeList:
	print(n)

print("\nArithmetic result of the tree: {0}".format(evaluate(n1)))