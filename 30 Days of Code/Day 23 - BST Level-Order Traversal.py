#==================== GIVEN CODE ======================#
import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root        
#===================== END =========================#

    def levelOrder(self,root):
  	     #Write your code here
        if root:
            order = [root]
            while order:
                node = order.pop(0)
                print node.data, # the comma is to get it to sit horizontally
                if node.left:
                    order.append(node.left)
                if node.right:
                    order.append(node.right) 

#==================== GIVEN CODE ======================#
T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
myTree.levelOrder(root) 
        
#===================== END =========================#