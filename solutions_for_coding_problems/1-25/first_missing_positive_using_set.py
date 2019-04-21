'''
Problem #4 [Hard]: Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

'''
Without the linear time constraint restriction, we could just sort the array, while filtering out negative numbers, 
and iterate over the sorted array and return the first number that doesn't match the index. 
However, sorting takes O(n log n), so we can't use that here.

Another way to solve this problem is by adding all the numbers to a set, and then use a counter initialized to 1. 
Then continuously increment the counter and check whether the value is in the set.
This is much simpler, but runs in O(N) time and space, whereas the "first_missing_positive.py" algorithm uses no extra space.
'''

def first_missing_positive(nums):
    s = set(nums)
    print("current set = ", s)
    i = 1
    while i in s:
        i += 1
    return i


v1 = [3, 4, -1, 1]
print("first_missing_positive([3, 4, -1, 1]) = ", first_missing_positive(v1), "\n")

v2 = [1, 2, 0]
print("first_missing_positive([1, 2, 0]) = ", first_missing_positive(v2), "\n")


v3 = [1, 2, 3, 4]
print("first_missing_positive([1, 2, 3, 4]) = ", first_missing_positive(v3), "\n")
