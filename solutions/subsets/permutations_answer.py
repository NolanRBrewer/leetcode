'''
Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. 
For example, {1, 2, 3} has the following six permutations:

{1, 2, 3} {1, 3, 2} {2, 1, 3} {2, 3, 1} {3, 1, 2} {3, 2, 1} If a set has ‘n’ distinct elements 
it will have n!n! permutations.
'''
from collections import deque


def find_permutations(nums):
  numsLength = len(nums)
  result = []
  permutations = deque()
  permutations.append([])
  for currentNumber in nums:
    # we will take all existing permutations and add the current number to create 
    # new permutations
    n = len(permutations)
    for _ in range(n):
      oldPermutation = permutations.popleft() # first in first out for the deque
      
      for j in range(len(oldPermutation)+1):
        # create a new permutation by adding the current number at every position
        newPermutation = list(oldPermutation) #create a deep copy of the  old permutation
        newPermutation.insert(j, currentNumber)# add the cuurrent number to the j position
        if len(newPermutation) == numsLength:
           # append the permutation as a valid answer
          result.append(newPermutation)
        else:
          # append the peremutation for to be "sent back through the proces"
          permutations.append(newPermutation)
          

  return result


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()
