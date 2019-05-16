'''
Problem #16 [Easy]: You run an e-commerce website and want to record the last N order ids in a log. 
Implement a data structure to accomplish this, with the following API:

* record(order_id): adds the order_id to the log
* get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
'''

'''
It seems like an array would be the perfect fit for this problem. 
We can just initialize the array to have size N, and index it in constant time. 
Then, when we record any orders, we can pop off the first order and append it to the end. 
Getting the ith last order would then just be indexing the array at length - i.
'''

class Log(object):
	def __init__(self, n):
		self._log = []
		self.n = n


	def record(self, order_id):
		if len(self._log) >= self.n:
			self._log.pop(0)
		self._log.append(order_id)


	def get_last(self, i):
		return self._log[-i]