class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = next


def count_paths(root, S):
    if not root:
        return 0

    return count_paths_recursive(root, S, [])

def count_paths_recursive(current_node, S, current_path):
    if current_node is None:
        return 0
    # add the current node to the path
    current_path.append(current_node.val)

    # check if there is a path that ends at the current node
    path_count = 0
    path_sum = 0
    for i in range(len(current_path)-1, -1, -1):
        path_sum += current_path[i]
        if path_sum == S:
            path_count += 1

    # traverse the left and right sub-trees
    path_count += count_paths_recursive(current_node.left, S, current_path)
    path_count += count_paths_recursive(current_node.right, S, current_path)

    # remove the current node from the path to backtrack
    del current_path[-1]

    return path_count


# main()
def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()