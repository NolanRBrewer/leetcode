chars = "aabbcc"
k = 3
# Output: 2
# Explanation: Max substring can be any one from {“aa” , “bb” , “cc”}.


def max_length_substring(chars: str, k: int) -> int:
    start_index = 0
    end_index = start_index + k
    counter = 0

    while end_index < len(chars):
        if len(set(chars[start_index:end_index])) == k:
            if end_index - start_index > counter:
                counter = end_index - start_index
            end_index += 1
        elif len(set(chars[start_index:end_index])) < k:
            end_index += 1
        elif len(set(chars[start_index:end_index])) > k:
            start_index += 1
    return counter


print(max_length_substring(chars, k))
