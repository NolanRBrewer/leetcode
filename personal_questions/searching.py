numbers = [4,5,7,2,9,1]
"""
`def binary_search(x):`
1. Compare x with the middle element.
2. If x matches with the middle element, we return the mid index.
3. Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
4. Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.
"""
sorted_numbers = sorted(numbers)
print(sorted_numbers)

def binary_search(array, item):
    start_index = 0
    end_index = len(array) - 1
    while start_index <= end_index:
        middle_index = (end_index + start_index) // 2
        if item == array[middle_index]:
            return middle_index
        elif item > array[middle_index]:
            start_index = middle_index + 1
        elif item < array[middle_index]:
            end_index = middle_index - 1
    return None
        
        
# print(sorted_numbers.index(0))
print(binary_search(sorted_numbers, 7))