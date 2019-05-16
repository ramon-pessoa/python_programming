'''
A linked list is a sequence of data elements, which are connected together via links. 
Each data element contains a connection to another data element in form of a pointer. 
Python does not have linked lists in its standard library. 
We implement the concept of linked lists using the concept of nodes as discussed in the previous chapter. 
We have already seen how we create a node class and how to traverse the elements of a node. 
In this chapter we are going to study the types of linked lists known as singly linked lists. 
In this type of data structure there is only one link between any two data elements. 
We create such a list and create additional methods to insert, update and remove elements from the list.
'''


class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None


class NumLinkedList:
	def __init__(self):
		self.head = None


	def at_beginning(self, data_in):
		new_node = Node(data_in)
		new_node.next = self.head
		self.head = new_node
	

	def in_between(self,middle_node,newdata):
		if middle_node is None:
			print("The mentioned node is absent")
			return

		new_node = Node(newdata)
		new_node.next = middle_node.next
		middle_node.next = new_node


	def at_end(self, newdata):
		new_node = Node(newdata)
		if self.head is None:
			self.head = new_node
			return
		last = self.head
		while(last.next):
			last = last.next
		last.next = new_node


	def remove_node(self, remove_key):

		head_val = self.head

		if (head_val is not None):
			if (head_val.data == remove_key):
				self.head = head_val.next
				head_val = None
				return

		while (head_val is not None):
			if head_val.data == remove_key:
				break
			prev = head_val
			head_val = head_val.next

		if (head_val == None):
			return

		prev.next = head_val.next

		head_val = None

	def print_linked_list(self):
		print_val = self.head
		while (print_val):
			print(print_val.data),
			print_val = print_val.next


llist1 = NumLinkedList()
llist1.at_end(3)
llist1.at_end(7)
llist1.at_end(8)
llist1.at_end(10)
llist1.print_linked_list()

print("\n")

# Test in_between and remove
llist2 = NumLinkedList()
llist2.head = Node(1)
e2 = Node(2)
e3 = Node(4)
llist2.head.next = e2
e2.next = e3
llist2.in_between(llist2.head.next, 3)
llist2.print_linked_list()
llist2.remove_node(2)
print("\n")	
llist2.print_linked_list()