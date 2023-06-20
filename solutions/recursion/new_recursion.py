class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def has_path(root, total= int)-> bool:
#   base case
    if not root:
       return False
    # base case 2
    if root.val ==  total and root.left == None and root.right == None:
       return True
    # recurse for both children nodes
    return has_path(root.left, total - root.val) or has_path(root.right, total - root.val)

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)    
  print("Tree has path: " + str(has_path(root, 23)))
  print("Tree has path: " + str(has_path(root, 16)))


main()
