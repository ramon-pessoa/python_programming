Some programming examples in Python
===========================

## Contents

1. [Solutions for coding problems](#solutions-for-coding-problems)

## Solutions for coding problems

55. Problem #55 [Easy]: Implement a URL shortener with the following methods:

	* shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
	* restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.

	* Hint: What if we enter the same URL twice?

	a. Solution (Python) [url_shortener.py]: Generating a shortened url and store it in a dictionary where the shortened url is the key and the actual url is the value. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/51-75/url_shortener.py)

	b. Solution (Python) [url_shortener_same_url_twice.py]: Create a second dict that maps urls to shortened urls and update that appropriately. When we see a url we've seen before, we can just then just re-use that shortened url. (https://github.com/ramon-pessoa/python_programming/blob/master/solutions_for_coding_problems/51-75/url_shortener_same_url_twice.py)

Go back to [Contents](#contents).
