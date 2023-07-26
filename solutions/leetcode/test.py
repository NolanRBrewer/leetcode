# abcd, 2
# a, bcd
# ab, cd
# abc, d

def separate(s):
    # separate string into a number of words
    valid_seperations = []
    start = 0
    stop = len(s)
    for i in range(stop):
        seperation = (s[start:i+1], s[i+1: stop+1])
        if seperation[0] != s and seperation[1] != s:
            valid_seperations.append(seperation)
    return valid_seperations
        

print(separate('abcd'))
