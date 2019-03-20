def contains_pair_with_sum(list1, k):
    list1.sort()
    for i, val1 in enumerate(list1):
        j = len(list1) - i - 1
        if i < j:
            val2 = list1[j]
            sum := val1 + val2
            if sum < k:
                i := i + 1
            elif sum > k:
                j := j - 1
            else:
                return True

    return False


list1 = [10, 15, 3, 7]
k = 17
contains_sum = contains_pair_with_sum(list1, k)
print("Contains pair with sum list={10, 15, 3, 7}, k=17? ", contains_sum)

list2 = [10, 15, 3, 6]
contains_sum = contains_pair_with_sum(list2, k)
print("Contains pair with sum list={10, 15, 3, 6}, k=17? ", contains_sum)
