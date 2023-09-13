'''
Input:
solution.solution("abccbaabccba")
Output:
    2
Input:
('abcabcabc')
output: 3
Input:
solution.solution("abcabcabcabc")
Output:
    4
'''
def solution(s):
    valid_splits = 1
    start = 0
    for end in range(start + 1, len(s)):
        # safe guard from not evenly divisible possibilities
        if len(s) % end != 0:
            continue
        # substring for comparison
        substring = s[start:end]

        window_size = end
        if substring == s[end: end + window_size]:
            valid_splits = int(len(s)/window_size)
            if s == substring * valid_splits:
                return valid_splits

    return valid_splits


        

print(solution("abccbaabccba")) # 2
print(solution("abcabcabcabc")) # 4
print(solution("abcabcabc")) # 3
print(solution("abcabd")) # 1
print(solution("a")) #1 