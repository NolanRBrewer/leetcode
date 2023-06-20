class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  # TODO: Write your code here
  sequence_idx = 0
  return find_path_recurr(root, sequence, sequence_idx)

def find_path_recurr(root, sequence, sequence_idx):
  if not root:
    return None

  if sequence_idx >= len(sequence) or root.val != sequence[sequence_idx]:
    return False

  if not root.left and not root.right and sequence_idx == len(sequence) - 1:
    return True

  return find_path_recurr(root.left, sequence, sequence_idx + 1) or find_path_recurr(root.right, sequence, sequence_idx + 1)

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
