'''
Create a TreeNode class:
Create a TreeDiameterclass:
    initialize:
        treediameter 
    function = find diameter:
        call for calculate height
        return treediameter
    function = calculate height: recursive
        BASE CASE
        check for current node 
            none nodes are height 0

        recurse down sub trees
        
        if left and right nodes exist aka left and right nodes exist:
            calculate diameter 
                left height and right height plus one for the height of rhe current node
            
            replace the tree diameter with
                the greater of the current tree diameter and the calculated diameter
                
        return greater of the two heights + 1 for the height of the current node

'''
class TreeNode:
    def __init__(self,val, left=None, right=None) -> None:
       self.val = val
       self.left = left
       self.right = right

class TreeDiameter:
    def __init__(self) -> None:
       self.tree_diameter = 0
    
    def find_diameter(self,root):
       self.calculate_height(root)
       return self.tree_diameter

    def calculate_height(self,node):
        if node is None:
           return 0
        
        leftHeight = self.calculate_height(node.left)
        rightHeight = self.calculate_height(node.right)

        if leftHeight != 0 and rightHeight != 0:
        #    calculate diameter
            diameter = leftHeight + rightHeight + 1

            self.tree_diameter = max(self.tree_diameter, diameter)
        
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