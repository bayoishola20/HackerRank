#==================== GIVEN ======================#
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next
#===================== END =========================#

    def insert(self,head,data): 
    #Complete this method
        if head is None:
            head = Node(data)
            #basically repeating the display function, but enabled to append the next data
        else:
            current = head
            while current.next:
                current = current.next
            current.next = Node(data)
        return head

#==================== GIVEN ======================#
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);
#===================== END =========================#