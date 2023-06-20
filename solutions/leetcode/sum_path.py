class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, required_sum):
  all_paths, curr_path = [], []
  find_paths_recur(root, required_sum, curr_path, all_paths)
  return all_paths

def find_paths_recur(root, required_sum, curr_path, all_paths):
#   base case
    if not root:
        return None
    
#   adding to the current path
    curr_path.append(root.val)
#   base case 2 
    if root.val == required_sum and root.left == None and root.right == None:
       all_paths.append(curr_path)
    #  recurse down braches 
    else:
    #    left child navigation
       find_paths_recur(root.left, required_sum - root.val, curr_path, all_paths) 
       #    right child navigation
       find_paths_recur(root.right, required_sum - root.val, curr_path, all_paths)
  
    del curr_path[-1]
  
def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    required_sum = 23
    print("Tree paths with required_sum " + str(required_sum) +
        ": " + str(find_paths(root, required_sum)))


main()