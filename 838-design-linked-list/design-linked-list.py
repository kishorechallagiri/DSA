class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class MyLinkedList(object):
    def __init__(self):
        self.head=None
        self.size=0
    def get(self, index):
        if index<0 or index>=self.size:
            return -1
        current=self.head    
        for i in range(index):
            current=current.next
        return current.val    
    def addAtHead(self, val):
        newnode=Node(val)
        newnode.next=self.head
        self.head=newnode
        self.size+=1
    def addAtTail(self, val):
        newnode=Node(val)
        if not self.head:
            self.head=newnode 
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=newnode
        self.size+=1
    def addAtIndex(self, index, val):
        if index<0 or index>self.size:
            return
        if index==0:
            self.addAtHead(val)
        elif index==self.size:
            self.addAtTail(val)  
        else:         
            newnode=Node(val)    
            current=self.head
            for i in range(index-1):
                current=current.next
            newnode.next=current.next
            current.next=newnode 
            self.size+=1   
    def deleteAtIndex(self, index):
        if index<0 or index>=self.size:
            return 
        if index==0:
            self.head=self.head.next
        else:
            curr=self.head
            for i in range(index-1):
                curr=curr.next
            curr.next = curr.next.next
        self.size-=1   
        
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)