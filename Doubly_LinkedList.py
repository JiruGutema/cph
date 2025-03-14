class ListNode:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.left=ListNode(0)
        self.right=ListNode(0)
        self.left.next=self.right
        self.right.prev=self.left

    def get(self, index: int) -> int:
        curr=self.left.next
        while curr and index>0:
            curr=curr.next
            index-=1
        if curr and curr!=self.right and index==0:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        new_node,prev,next=ListNode(val),self.left,self.left.next
        new_node.next=next
        new_node.prev=prev
        prev.next=new_node
        next.prev=new_node

    def addAtTail(self, val: int) -> None:
        new_node,prev,next=ListNode(val),self.right.prev,self.right
        new_node.next=next
        new_node.prev=prev
        prev.next=new_node
        next.prev=new_node

    def addAtIndex(self, index: int, val: int) -> None:
        curr=self.left.next
        while curr and index>0:
            curr=curr.next
            index-=1
        if curr and index==0:
            new_node,prev,next=ListNode(val),curr.prev,curr
            new_node.next=next
            new_node.prev=prev
            prev.next=new_node
            next.prev=new_node   
        

    def deleteAtIndex(self, index: int) -> None:
        curr=self.left.next
        while curr and index>0:
            curr=curr.next
            index-=1
        if curr and curr!=self.right and index==0:
            prev,next=curr.prev,curr.next
            prev.next=next
            next.prev=prev
        



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)





