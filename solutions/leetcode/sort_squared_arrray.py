# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.
nums = [-4, -1, 0, 3, 10, 23]


class Solution:

    def sorted_squares(self, nums: list[int]) -> list[int]:
        return sorted([num * num for num in nums])


solution = Solution()
print(solution.sorted_squares(nums))
