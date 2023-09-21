# subsets.py

def generate_subsets_recursive(nums, index=0, current_subset=[], subsets=[]):
    """
    Recursive function to generate all possible subsets of an array.
    """
    if index == len(nums):
        subsets.append(current_subset[:])  # Append a copy of the current_subset
        return

    # Include the current element in the subset
    current_subset.append(nums[index])
    generate_subsets_recursive(nums, index + 1, current_subset, subsets)

    # Exclude the current element from the subset
    current_subset.pop()
    generate_subsets_recursive(nums, index + 1, current_subset, subsets)

def generate_subsets(nums):
    """
    Wrapper function to generate all possible subsets of an array.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")

    if len(nums) == 0:
        return []

    subsets = []
    generate_subsets_recursive(nums, 0, [], subsets)
    return subsets
