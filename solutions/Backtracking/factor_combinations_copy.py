'''
Square root

sqrt = int(num ** 0.5)
'''
def getAllFactors(num, start, curr, result):

    for i in range(start, int(num**0.5) + 1):
        if num % i == 0:
            curr.append(i)
            result.append(list(curr + [num //i]))

            getAllFactors(num//i, i, curr, result)
            # backtrack
            curr.pop()

    return result

def getFactors(num):
    return getAllFactors(num, 2, [], [])

# test cases
print(getFactors(8))  # expected: [[2, 2, 2], [2, 4]]
print(getFactors(12))  # expected: [[2, 2, 3], [2, 6], [3, 4]]
print(getFactors(16))  # expected: [[2, 2, 2, 2], [2, 2, 4], [2, 8], [4, 4]]
print(getFactors(20))  # expected: [[2, 2, 5], [2, 10], [4, 5]]
print(getFactors(1))  # expected: []