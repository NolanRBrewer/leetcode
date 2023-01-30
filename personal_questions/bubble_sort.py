numbers = [4,5,7,2,9,1]

def bubble_sort(nums):
    swaps = True
    while swaps:
        swaps = False
        for index in range(len(nums)-1):
            if nums[index] > nums[index + 1]:
                nums[index],nums[index + 1] = nums[index + 1], nums[index]
                swaps = True

    return nums

print(bubble_sort(numbers))