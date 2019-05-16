'''
Problem #16 [Easy]: You run an e-commerce website and want to record the last N order ids in a log. 
Implement a data structure to accomplish this, with the following API:

* record(order_id): adds the order_id to the log
* get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
'''

'''
The solution in log_record_get_last_linear_time.py takes O(N) time to run the record function.

What we can do to avoid having to moving every element down by 1 is to keep a current index and move it up each time we record something. 

For get_last, we can simply take current - i to get the appropriate element. 

Now, both record and get_last should take constant time.

This solution is called a ring buffer or circular buffer!
'''

class Log(object):
	def __init__(self, n):
		self.n = n
		self._log = []
		self._cur = 0


	def record(self, order_id):
		if len(self._log) == self.n:
			self._log[self._cur] = order_id
		else:
			self._log.append(order_id)
		self._cur = (self._cur + 1) % self.n


	def get_last(self, i):
		return self._log[self._cur - i]
