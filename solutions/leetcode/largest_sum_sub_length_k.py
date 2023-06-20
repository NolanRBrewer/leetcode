# the largest sum of a subsequence of length K
import more_itertools
nums = [2, 1, 3, 3]
k = 2


def max_subsequence(nums: list[int], k: int) -> list[int]:
    numbers = list(more_itertools.windowed(nums, k))
    sums = [sum(subsequence) for subsequence in numbers]
    return max(sums)


print(max_subsequence(nums, k))
