from collections import deque

class TreeNode:
    def __init__(self, val, left= None, right= None) -> None:
        self.val = val
        self.left = left
        self.right = right
    
def traverse(root):
    result = deque()
    if not root:
        return result

    queue = deque() 
    queue.append(root)

    while queue:
        temp = []
        for i in range(len(queue)):
            currentNode = queue.popleft()
            temp.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        result.appendleft(temp) 
    
    return result #[::-1]

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()