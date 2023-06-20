# the largest sum of a subsequence of length K
# without itertools

nums = [-1, -2, 4, 3]

k = 3


def max_subsequence(nums: list[int], k: int) -> list[int]:
    # itereate over nums and remove smallest valuse until the sequence is length k
    augmented_nums = nums.copy()
    for i in range(len(augmented_nums)-k):
        augmented_nums.remove(min(augmented_nums))
    return augmented_nums


print(max_subsequence(nums, k))
print(nums)
