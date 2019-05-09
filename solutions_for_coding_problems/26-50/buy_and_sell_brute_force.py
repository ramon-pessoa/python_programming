'''
Problem #47 [Easy]: Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
'''

'''
The brute force solution here is to iterate over our list of stock prices, and for each price, find the largest profit you can make from selling that stock price (with the formula future ‑ current), and keep track of the largest profit we can find. 

That would look like below.

This would take O(N^2) time.
'''

def buy_and_sell(arr):
	max_profit = 0
	for i in range(len(arr) - 1):
		for j in range(i, len(arr)):
			buy_price, sell_price = arr[i], arr[j]
			max_profit = max(max_profit, sell_price - buy_price)
	return max_profit


print("Maximum profit you could have made from buying and selling the stock [9, 11, 8, 5, 7, 10] once: %s" % buy_and_sell([9, 11, 8, 5, 7, 10]))
