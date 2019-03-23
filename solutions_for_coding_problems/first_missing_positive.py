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

Clearly we have to use some sort of trick here to get it running in linear time. Since the first missing positive number 
must be between 1 and len(array) + 1, we can ignore any negative numbers and numbers bigger than len(array). The basic 
idea is to use the indices of the array itself to reorder the elements to where they should be. We traverse the array and 
swap elements between 0 and the length of the array to their value's index. We stay at each index until we find that 
index's value and keep on swapping.

By the end of this process, all the first positive numbers should be grouped in order at the beginning of the array. 
We don't care about the others. This only takes O(N) time, since we swap each element at most once. Then we can iterate 
through the array and return the index of the first number that doesn't match, just like before.
'''

def first_missing_positive(nums):
    if not nums:
        return 1
    print("\toriginal array = ", nums)
    for i, num in enumerate(nums):
        print("\tindex, number = ", i, num)
        while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
            v = nums[i]
            nums[i], nums[v - 1] = nums[v - 1], nums[i]
            print("\tcurrent array = ", nums)
            if nums[i] == nums[v - 1]:
                break
    print("\tfinal array = ", nums)
    for i, num in enumerate(nums, 1):
        if num != i:
            return i
    return len(nums) + 1


v1 = [3, 4, -1, 1]
print("first_missing_positive([3, 4, -1, 1]) = ", first_missing_positive(v1), "\n")

v2 = [1, 2, 0]
print("first_missing_positive([1, 2, 0]) = ", first_missing_positive(v2), "\n")


v3 = [1, 2, 3, 4]
print("first_missing_positive([1, 2, 3, 4]) = ", first_missing_positive(v3), "\n")
