'''
Numbers can be regarded as the product of their factors.

For example, 8 = 2 x 2 x 2 = 2 x 4.

Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

Example 1:

Input: n = 8  
Output: [[2, 2, 2], [2, 4]]   
'''

def getAllFactors(n, start, curr, result):
  # Iterate through all integers i from start to the square root of n + 1
  # This loop is used to find all the factors of the input number n
  for i in range(start, int(n**0.5) + 1):
    # If n is divisible by i, add i to the curr list of factors
    # curr is used to store the current factors being calculated
    if n % i == 0:
      curr.append(i) # Found a factor, append it to the list of factors
      # Append the current factors and the corresponding factor of n // i to the result list
      result.append(list(curr + [n // i]))
      # Recursively call the function with n // i as the new input, i as the new start value, and curr and result as the current factors and results
      getAllFactors(n // i, i, curr, result)
      curr.pop() # Pop the last element from curr to backtrack and find other factors
  return result


def getFactors(n):
  return getAllFactors(n, 2, [], [])


# test cases
print(getFactors(8))  # expected: [[2, 2, 2], [2, 4]]
print(getFactors(12))  # expected: [[2, 2, 3], [2, 6], [3, 4]]
print(getFactors(16))  # expected: [[2, 2, 2, 2], [2, 2, 4], [2, 8], [4, 4]]
print(getFactors(20))  # expected: [[2, 2, 5], [2, 10], [4, 5]]
print(getFactors(1))  # expected: []
