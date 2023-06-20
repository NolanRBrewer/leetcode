class TreeNode:
    def __init__(self, val, left= None, right= None):
        self.val = val
        self.left = left
        self.right = right

def find_path(root, sequence):
    sequence_index = 0
    return find_path_recursive(root, sequence, sequence_index)

def find_path_recursive(root, sequence, sequence_index):
    # check for a root
    if not root:
        return False
    
    # if we are checking outside of our sequence size or the value doesn't exist inside of the 
    if sequence_index > len(sequence) or root.val != sequence[sequence_index]:
        return False
    
    # if at the bottom of the tree and we have yet to exceed the sequence length or trigger other arguments
    # we have found a matching sequence
    if root.right == None and root.left == None and sequence_index == (len(sequence) - 1):
        return True
    
    # recursively call children branchs 
    return find_path_recursive(root.left, sequence, sequence_index + 1) or find_path_recursive(root.right, sequence, sequence_index + 1)

def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
