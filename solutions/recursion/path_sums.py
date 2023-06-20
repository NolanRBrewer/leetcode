class TreeNode:
    def __init__(self, val, left=None, right= None) -> None:
        self.val = val
        self.left = left
        self.right = right

def find_sums(root):
    sums = []
    find_sum_recursive(root,sums,0)
    return sums 

def find_sum_recursive(currentNode, sums, currentSum= 0):
    # return when at the end of a branch
    if currentNode is None:
        return None
    
    currentSum += currentNode.val 
    # append path sum when at the end leaf node
    if currentNode.left is None and currentNode.right is None:
        sums.append(currentSum)

    else:
        # recursively call down child branches
        find_sum_recursive(currentNode.left, sums, currentSum)
        find_sum_recursive(currentNode.right, sums, currentSum)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has sums: " + str(find_sums(root)))

main()