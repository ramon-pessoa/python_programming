'''
Problem #55 [Easy]: Implement a URL shortener with the following methods:

* shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
* restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?
'''

'''
We can improve the solution in url_shortener.py a bit. 

What if we shorten the same url twice? 

We could potentially re-use the existing shortened url, but we don't know how to access it without querying all values in our dict!

So we can create a second dict that maps urls to shortened urls and update that appropriately. 

When we see a url we've seen before, we can just then just re-use that shortened url.
'''

import random
import string

class URLShortener:
	
	def __init__(self):
		self.short_to_url = {}
		self.url_to_short = {}


	def _generate_short(self):
		return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))


	def _generate_unused_short(self):
		t = self._generate_short()
		while t in self.short_to_url:
			t = self._generate_short()
		return t


	def shorten(self, url):
		short = self._generate_unused_short()
		if url in self.url_to_short:
			return self.url_to_short[url]
		self.short_to_url[short] = url
		self.url_to_short[url] = short
		return short


	def restore(self, short):
		return self.short_to_url.get(short, None)


urlShortener = URLShortener()

url1 = urlShortener._generate_short()
print("_generate_short(): url1 = {}".format(url1))

url2 = urlShortener._generate_unused_short()
print("_generate_unused_short(): url2 = {}".format(url2))

url3 = urlShortener.shorten(url1)
print("urlShortener.shorten(url1): url3 = {}".format(url3))

url4 = urlShortener.restore(url3)
print("urlShortener.restore(url3): url4 = {}".format(url4))