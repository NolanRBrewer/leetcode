# nums = [2, 1, -1]
# nums = [1, 7, 3, 6, 5, 6]
# nums = [1, 2, 3]


def running_sum(nums: list[int]) -> list[int]:

    left_sum, right_sum = 0, sum(nums)

    for index, num in enumerate(nums):
        # calculate sum right side of index
        right_sum -= num
        # check for equal sums
        if left_sum == right_sum:
            return index
        left_sum += num
    # after iteration return -1 when if statement is never satisfied
    return -1


print(running_sum(nums))
