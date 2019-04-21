'''
Problem #33 [Easy]: Compute the running median of a sequence of numbers. 
That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
'''

'''
For this problem, the trick is to use two heaps: a min-heap and a max-heap. 

We keep all elements smaller than the median in the max-heap and all elements larger than the median 
in the min-heap. We'll keep these heaps balanced so that the median is always either the root of the 
min-heap or the max-heap (or both).

When we encounter a new element from the stream, we'll first add it to one of our heaps: 
the max-heap if the element is smaller than the median, or the min-heap if it's bigger. We can make the 
max-heap the default heap if they're equal or there are no elements.

Then we re-balance if necessary by moving the root of the larger heap to the smaller one. 
It's only necessary if the a heap is larger than the other by more than 1 element.

Finally, we can print out our median: it will just be the root of the larger heap, or the average of 
the two roots if they're of equal size.

Since Python has really terrible support for heaps, we'll pretend we have some heap objects that have 
the standard interface.

This runs in O(N) space. In terms of time, each new element takes O(log N) time to manipulate the heaps, 
so this will run in O(N log N) time.
'''
