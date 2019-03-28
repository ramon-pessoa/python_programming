'''
Problem #10 [Medium]: Implement a job scheduler which takes in a function f and an integer n, 
and calls f after n milliseconds.
'''

'''
While the solution in scheduler_new_thread_each_call.py works, there is a huge problem with this method: 
we spin off a new thread each time we call delay! That means the number of threads we use could easily explode. 

We can get around this by having only one dedicated thread to call the functions, and storing the functions we 
need to call in some data structure. In this case, we use a list. We also have to do some sort of polling now 
to check when to run a function. We can store each function along with a unix epoch timestamp that tells it 
when it should run by. Then we'll poll some designated tick amount and check the list for any jobs that are 
due to be run, run them, and then remove them from the list.

Some extra work we can consider are:

Extend the scheduler to allow calling delayed functions with variables
Use a heap instead of a list to keep track of the next job to run more efficiently
Use a condition variable instead of polling (it just polls lower in the stack)
Use a threadpool or other mechanism to decrease the chance of starvation 
(one thread not being able to run because of another running thread)
'''

from time import sleep
import threading


class Scheduler:
	def __init__(self):
		self.fns = [] # tuple of (fn, time)
		t = threading.Thread(target=self.poll)
		t.start()


	def poll(self):
		while True:
			now = time() * 1000
			for fn, due in self.fns:
				if now > due:
					fn()
			self.fns = [(fn, due) for (fn, due) in self.fns if due > now]
			sleep(0.01)


	def delay(self, f, n):
		self.fns.append((f, time() * 1000 + n))
