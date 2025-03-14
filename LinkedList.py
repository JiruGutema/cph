class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        count = 0
        curr = self.head
    
        while curr:
            if count == index:
                return curr.val
            curr = curr.next
            count += 1
        return -1
        
    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        
    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        
        curr = self.head
        count = 0
        while curr and count < index - 1:
            curr = curr.next
            count += 1
        
        if not curr:
            return
        
        newNode = Node(val)
        newNode.next = curr.next
        curr.next = newNode
        
    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        
        if index == 0:
            self.head = self.head.next
            return
        
        curr = self.head
        count = 0
        while curr.next and count < index - 1:
            curr = curr.next
            count += 1
        
        if not curr.next:
            return
        
        curr.next = curr.next.next


    def __str__(self):
        curr = self.head
        result = ""
        while curr is not None:
            result += str(curr.val)
            if curr.next:
                result += "-->"
            curr = curr.next
        return result

    def __len__(self):
        count = 0
        curr = self.head
        while curr is not None:
            curr = curr.next
            count += 1 
        return count
def helper():
 
if __name__ == "__main__":
    helper()


