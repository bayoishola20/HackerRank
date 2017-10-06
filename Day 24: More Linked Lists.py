#==================== GIVEN CODE ======================#
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
        p = Node(data)        
        if head==None:
            head=p
        elif head.next==None:
            head.next=p
        else:
            start=head
            while(start.next!=None):
                 start=start.next
            start.next=p
        return head 
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next        
#===================== END =========================#

    def removeDuplicates(self,head):
        #Write your code here
        node = head
        while node and node.next:
            while node.next and node.data is node.next.data:
                 node.next = node.next.next
            node = node.next
        return head # return head

#==================== GIVEN CODE ======================#
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)   
head=mylist.removeDuplicates(head)
mylist.display(head); 
        
#===================== END =========================#