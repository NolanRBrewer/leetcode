
class Solution(object):
    
    def combinationSum(self, candiates, target):
        res = []
        self.backtracking(candiates,target, 0, [], res)
        return res
    
    def backtracking(self, candidates, target, pos, comb, res):

        if target == 0:
            # make a deep copy!!!
            res.append(list(comb))
            # do i need to backtrack here? No.
            return 
        # range of current position to end of array shrink the window
        for i in range(pos, len(candidates)):
            if candidates[i] > target:
                continue
            else:
                comb.append(candidates[i])
                # subtract candidate from target to approach base case
                self.backtracking(candidates, target - candidates[i], i, comb, res)
                # remember to backtrack
                comb.pop()

def main():
    # Test case 1
    candidates = [2, 3, 6, 7]
    target = 7
    s = Solution()
    print(s.combinationSum(candidates, target))  # expected output: [[2, 2, 3], [7]]

    # Test case 2
    candidates = [2, 3, 5]
    target = 8
    s = Solution()
    print(
        s.combinationSum(candidates, target)
    )  # expected output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    # Test case 3
    candidates = []
    target = 8
    s = Solution()
    print(s.combinationSum(candidates, target))  # expected output: []

    # Test case 4
    candidates = [5, 10, 15]
    target = 20
    s = Solution()
    print(
        s.combinationSum(candidates, target)
    )  # expected output: [[5,5,5,5], [5,5,10], [5,15], [10,10]]

    # Test case 5
    candidates = [2, 4, 6, 8]
    target = 10
    s = Solution()
    print(
        s.combinationSum(candidates, target)
    )  # expected output: [[2,2,2,2,2], [2,2,2,4], [2,2,6], [2,4,4], [2,8], [4,6]]

    # Test case 6
    candidates = [2, 3, 5]
    target = 0
    s = Solution()
    print(s.combinationSum(candidates, target))  # expected output: [[]]


main()
