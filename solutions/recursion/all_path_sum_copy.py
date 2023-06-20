'''
Create TreeNode

Create Function

Create Recursive Function

Create Main function
    instance

'''

class TreeNode:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self. right = right

def find_paths(root, required_sum):
    allPaths = []
    find_paths_recursive(root,required_sum,[], allPaths)
    return allPaths

def find_paths_recursive(currentNode, required_sum, currentPath, allPaths):
    if currentNode is None:
        return None #return when all nodes have been deleted
    # add the current node value to the path
    currentPath.append(currentNode.val)

    if currentNode.val == required_sum and currentNode.left == None and currentNode.right == None:
        allPaths.append(list(currentPath)) # append current path to all paths list
    
    else:
        # recurse down all paths with children until none are left
        find_paths_recursive(currentNode.left, required_sum - currentNode.val, currentPath, allPaths)
        find_paths_recursive(currentNode.right, required_sum - currentNode.val, currentPath, allPaths)

    # delete last item in the path to back track
    del currentPath[-1]

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)   
    print(find_paths(root, 23))

main()