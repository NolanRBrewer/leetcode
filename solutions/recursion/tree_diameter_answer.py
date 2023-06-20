'''
Given a binary tree, find the length of its diameter. 
The diameter of a tree is the number of nodes on the longest path between any two leaf nodes. 
The diameter of a tree may or may not pass through the root.
'''
'''
Create treenode class

create a tree diameter class
# if the current node doesn't have a left or right subtree, we can't have
# a path passing through it, since we need a leaf node on each side

# diameter at the current node will be equal to the height of left subtree +
# the height of right sub-trees + '1' for the current node
# update the global tree diameter

# height of the current node will be equal to the maximum of the heights of
# left or right subtrees plus '1' for the current node
'''
class TreeNode:
  def __init__(self,val, left= None, right=None):
    self.val = val
    self.left = left
    self.right = right

class TreeDiameter:
  def __init__(self):
    self.tree_diameter = 0
  
  def find_diameter(self, root):
    self.calculate_height(root)
    return self.tree_diameter
    
  def calculate_height(self, currentNode):
    # the end of each branch gives a base height of 0
    if currentNode is None:
      return 0 
    # recurse down each subtree
    leftHeight = self.calculate_height(currentNode.left)
    rightHeight = self.calculate_height(currentNode.right)
    # if the currentNode is at the bottom of the tree we can calulate heights starting from here
    if leftHeight != 0 and rightHeight != 0:
      # calculate diameter from the heights plus one for 
      diameter = leftHeight + rightHeight + 1
      # update the global diameter variable when a greater height is found
      self.tree_diameter = max(self.tree_diameter, diameter)
    # height of the node will be the greater of the two heights plus one for the currentNode
    return max(leftHeight, rightHeight) + 1


def main():
  treeDiameter = TreeDiameter()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
#   should == 5
  root.left.left = None
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  root.right.left.right.left = TreeNode(10)
  root.right.right.left.left = TreeNode(11)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
# should == 7


main()