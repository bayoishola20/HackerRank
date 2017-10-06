#==================== GIVEN CODE ======================#
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

    def getHeight(self,root):
        #Write your code here
        left = 0 #initial position
        right = 0 #initial position
        if root:
            if root.right:
                right = 1 + self.getHeight(root.right)
            if root.left:
                left = 1 + self.getHeight(root.left)
            return max(right, left)

#==================== GIVEN CODE ======================#
T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print height 
    
        
#===================== END =========================#