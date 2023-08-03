class Solution:
    def maxUniqueSplit(self, s):
        return self.maxCount(s, 0,set())

    def maxCount(self, s, start, unique):

        # base case
        if start == len(s):
            return len(unique)
        
        count = 0
        # looking from start pos to end of string
        for i in range(start + 1, len(s) + 1):
            substring = s[start: i]

            if substring not in unique:
                unique.add(substring)
                # set count variable to recursive call of maxCount
                count = max(count, self.maxCount(s, i, unique))

                unique.remove(substring)
        return count
    
def main():
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

main()
