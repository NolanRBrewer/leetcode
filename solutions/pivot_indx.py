nums = [2, 1, -1]


def pivot_index(nums: list[int]) -> int:
    p_index = 0
    while p_index < len(nums):
        if sum(nums[0: p_index]) == sum(nums[p_index: -1]):
            return p_index
        else:
            p_index += 1
    if p_index == len(nums):
        return -1
    elif p_index == 0:
        return 0


print(pivot_index(nums))
