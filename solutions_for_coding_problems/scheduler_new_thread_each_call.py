'''
Problem #10 [Medium]: Implement a job scheduler which takes in a function f and an integer n, 
and calls f after n milliseconds.
'''

'''
One straightforward solution is to spin off a new thread on each function we want to delay, 
sleep the requested amount, and then run the function. It might look something like the code below.

While this works, there is a huge problem with this method: we spin off a new thread each time we call delay! 
That means the number of threads we use could easily explode. 
'''

import threading
from time import sleep


class Scheduler:
	def __init__(self):
		pass


	def delay(self, f, n):
		def sleep_then_call(n):
			sleep(n / 1000)
			f()
		t = threading.Thread(target=sleep_then_call)
		t.start()
