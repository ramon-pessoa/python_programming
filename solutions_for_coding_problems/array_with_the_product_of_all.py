def get_array_with_the_product_of_all(arr):
    new_arr = []
    for i in arr:
        prod = 1
        for j in arr:
            if i != j:
                prod = prod * j
        new_arr.append(prod)
    return new_arr

arr1 = [3, 2, 1]
new_arr = get_array_with_the_product_of_all(arr1)
# New array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i
print("New array using [3, 2, 1] input array: ", new_arr)
arr2 = [1, 2, 3, 4, 5]
new_arr = get_array_with_the_product_of_all(arr2)
print("New array using [1, 2, 3, 4, 5] input array: ", new_arr)
