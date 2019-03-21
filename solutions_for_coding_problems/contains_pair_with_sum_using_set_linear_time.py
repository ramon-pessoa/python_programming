'''
Problem #1 [Easy]: Given a list of numbers and a number k, return whether any two numbers from the list add up to k. 
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17. 
Bonus: Can you do this in one pass?
'''

'''
This solution uses a set to remember the numbers we've seen so far. 
Then for a given number, we can check if there is another number that, if added, would sum to k. 
This would be O(N) since lookups of sets are O(1) each.
'''
def contains_pair_with_sum(list1, k):
    seen = set()
    for num in list1:
    	if k - num in seen:
    		return True
    	seen.add(num)
    return False


list1 = [10, 15, 3, 7]
k = 17
contains_sum = contains_pair_with_sum(list1, k)
print("Contains pair with sum list={10, 15, 3, 7}, k=17? ", contains_sum)

list2 = [10, 15, 3, 6]
contains_sum = contains_pair_with_sum(list2, k)
print("Contains pair with sum list={10, 15, 3, 6}, k=17? ", contains_sum)
