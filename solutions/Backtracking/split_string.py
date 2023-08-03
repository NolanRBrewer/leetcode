'''
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings 
forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "aab"  
Output: 2  
Explanation: Two possible ways to split the given string into maximum unique 
substrings are: ['a', 'ab'] & ['aa', 'b'], both have 2 substrings; 
hence the maximum number of unique substrings in which the given string can be split is 2.
'''

class Solution:
  def maxUniqueSplit(self, s: str) -> int:
    return self.splitAndCount(s, 0, set())

  def splitAndCount(self, s: str, start: int, set) -> int:
    # base case, if we have reached the end of the input string, return the size of the set
    if start == len(s):
      return len(set)

    count = 0
    # loop through all substrings starting from the current start position
    for i in range(start + 1, len(s) + 1):
      string = s[start:i]
      # if the substring is not in the set, add it and recursively call the function with the new start position
      if string not in set:
        set.add(string)
        count = max(count, self.splitAndCount(s, i, set))
        set.remove(string)  # remove the substring from the set and backtrack

    return count  # return the maximum count of unique substrings found


if __name__ == "__main__":
  sol = Solution()

  # Test Case 1
  input1 = "abcabc"
  output1 = sol.maxUniqueSplit(input1)
  print("maxUniqueSplit(" + input1 + ") = " + str(output1))  # Expected: 4

  # Test Case 2
  input2 = "aab"
  output2 = sol.maxUniqueSplit(input2)
  print("maxUniqueSplit(" + input2 + ") = " + str(output2))  # Expected: 2

  # Test Case 3
  input3 = "ababab"
  output3 = sol.maxUniqueSplit(input3)
  print("maxUniqueSplit(" + input3 + ") = " + str(output3))  # Expected: 4

  # Test Case 4
  input4 = ""
  output4 = sol.maxUniqueSplit(input4)
  print("maxUniqueSplit(" + input4 + ") = " + str(output4))  # Expected: 0

  # Test Case 5
  input5 = "a"
  output5 = sol.maxUniqueSplit(input5)
  print("maxUniqueSplit(" + input5 + ") = " + str(output5))  # Expected: 1
