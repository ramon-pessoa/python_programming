'''
Problem #47 [Easy]: Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
'''

'''
The solution in buy_and_sell_brute_force.py runs in O(N^2) time. We can speed this up.

The maximum profit comes from the greatest difference between the highest price and lowest price, where the higher price must come after the lower one. 
But if we see a high price x and then a higher price y afterwards, then we can always discard x. 
So, if we keep track of the highest price in the future for each variable, we can immediately find how much profit buying at that price can make.

That means we can look at the array backwards and always keep track of the highest price we've seen so far. 
Then, at each step, we can look at the current price and check how much profit we would have made buying at that price by comparing with our maximum price in the future.
Then we only need to make one pass!

This runs in O(N) time and O(1) space.
'''

def buy_and_sell(arr):
	current_max, max_profit = 0, 0
	for price in reversed(arr):
		current_max = max(current_max, price)
		potential_profit = current_max - price
		max_profit = max(max_profit, potential_profit)
	return max_profit


print("Maximum profit you could have made from buying and selling the stock [9, 11, 8, 5, 7, 10] once: %s" % buy_and_sell([9, 11, 8, 5, 7, 10]))
