class Solution:
    def maxUniqueSplit(self,string):
        return self.splitCount(string, 0, set())
    
    def splitCount(self, string, start, unique):
        if start == len(string):
            return len(unique)
        # add one to create inclusion for range function
        count = 0
        for i in range(start + 1, len(string) + 1):
            substring = string[start: i]

            if substring not in unique:
                unique.add(substring)
                count = max(count, self.splitCount(string, i, unique))
                # backtrack
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
