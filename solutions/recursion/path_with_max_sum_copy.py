# imports
import math

# explanation

# classes
class TreeNode:
    def __init__(self,val,left= None, right= None) -> None:
        self.val = val
        self.left = left
        self.right = right

class MaximumPathSum:
    def find_max_path_sum(self, root):
        self.globalMaxSum = -math.inf
        self.find_max_path_sum_recurr(root)
        return self.globalMaxSum
    def find_max_path_sum_recurr(self,currentNode):
        # node check
        if currentNode is None:
            return 0
        # recurse
        sumFromLeft = self.find_max_path_sum_recurr(currentNode.left)
        sumFromRight = self.find_max_path_sum_recurr(currentNode.right)

        # ignore negatives
        sumFromLeft = max(sumFromLeft, 0)
        sumFromRight= max(sumFromRight, 0)

        localMaxSum = sumFromLeft + sumFromRight + currentNode.val

        self.globalMaxSum = max(self.globalMaxSum, localMaxSum)

        return max(sumFromLeft, sumFromRight) + currentNode.val
    

def main():
  maximumPathSum = MaximumPathSum()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)

  print("Maximum Path Sum: " + str(maximumPathSum.find_max_path_sum(root)))
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  print("Maximum Path Sum: " + str(maximumPathSum.find_max_path_sum(root)))

  root = TreeNode(-1)
  root.left = TreeNode(-3)
  print("Maximum Path Sum: " + str(maximumPathSum.find_max_path_sum(root)))


main()
