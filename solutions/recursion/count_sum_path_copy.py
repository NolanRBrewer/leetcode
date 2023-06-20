class TreeNode:
    def __init__(self,val, left= None, right= None):
        self.val = val
        self.left = left
        self.right = right

def find_path(root, S):
    return find_path_recurr(root, S, [])

def find_path_recurr(currentNode, S, currentPath):
    # check for node
    if currentNode is None:
        return 0
    # add node to list
    currentPath.append(currentNode.val)

    path_count = 0
    path_sum = 0
    # see if any part of the current path adds up to S
    for i in range(len(currentPath)-1,-1,-1):
        path_sum += currentPath[i]
        if path_sum == S:
            path_count += 1
    # recursively call down each sub-tree
    else:
        path_count += find_path_recurr(currentNode.left, S, currentPath)
        path_count += find_path_recurr(currentNode.right, S, currentPath)
    # backtrack
    del currentPath[-1]

    return path_count



# main()
def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(find_path(root, 11)))


main()

    