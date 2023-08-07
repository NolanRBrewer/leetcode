# abcd, 2
# a, bcd
# ab, cd
# abc, d
'''
abcd 3
a, b, cd
a, bc, d
ab, c, d
'''

def separate(s, num_seperations):
    # separate string into a number of words
    valid_seperations = []
    start = 0
    stop = len(s)
    # length of the input - number of words - 1 
    for i in range(stop):
        seperation = (s[start:i+1], s[i+1: stop+1])
        
        if seperation[0] != s and seperation[1] != s:
            # check for full string
            valid_seperations.append(seperation)
    return valid_seperations
        

# print(separate('abcd', 3))

def find_seperations(s, num_seperations):
    results = []
    recurr(s, num_seperations, 0,  [], results)
    return results

def recurr(s, target, start, subset, results):
    # base case
    if target == 0:
        results.append(subset)
        return

    substring = s[start:]
    subset.append(substring)
    recurr(s ,target- 1, start +1, subset, results)
