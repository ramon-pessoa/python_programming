Some programming examples in Python
===========================

## Contents

1. [Problems from 51 to 75](#problems-from-51-to-75)

2. [All solutions for coding problem](https://github.com/ramonfigueiredopessoa/python_programming#solutions-for-coding-problems)

## Problems from 51 to 75

53. Problem #53 [Medium]: Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.

	a. Solution (Python): [queue_using_two_stacks.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/51-75/queue_using_two_stacks.py)

55. Problem #55 [Easy]: Implement a URL shortener with the following methods:

	* shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
	* restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.

	* Hint: What if we enter the same URL twice?

	a. Solution (Python) - Generating a shortened url and store it in a dictionary where the shortened url is the key and the actual url is the value: [url_shortener.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/51-75/url_shortener.py)

	b. Solution (Python) - Create a second dict that maps urls to shortened urls and update that appropriately. When we see a url we've seen before, we can just then just re-use that shortened url: [url_shortener_same_url_twice.py](https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/51-75/url_shortener_same_url_twice.py)

Go back to [Contents](#contents).
