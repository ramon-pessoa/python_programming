'''
Problem #1 [Easy]: Given a list of numbers and a number k, return whether any two numbers from the list add up to k. 
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17. 
Bonus: Can you do this in one pass?
'''

'''
Brute force solution:  Involve a nested iteration to check for every pair of numbers.
This solution is O(N^2).
'''
def contains_pair_with_sum(list1, k):
    for i in range(len(list1)):
        for j in range(len(list1)):
            if i != j and list1[i] + list1[j] == k:
                return True
    return False


list1 = [10, 15, 3, 7]
k = 17
contains_sum = contains_pair_with_sum(list1, k)
print("Contains pair with sum list={10, 15, 3, 7}, k=17? ", contains_sum)

list2 = [10, 15, 3, 6]
contains_sum = contains_pair_with_sum(list2, k)
print("Contains pair with sum list={10, 15, 3, 6}, k=17? ", contains_sum)
